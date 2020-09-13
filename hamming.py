import numpy as np
import math

class Hamming:
    def __init__(self, block_size=16):
        # block_size -> number of bits in a error correction region. must be power of two
        if not self._is_power_of_two(block_size):
            raise ValueError("block size={block_size} must be a power of two")
        self.block_size = block_size
        self.block_overhead = int(math.log(self.block_size, 2) + 1)
        self.block_capacity = self.block_size - self.block_overhead

    def encode(self, bytes_in, padding=0):
        # calculated overhead and output size
        num_blocks = math.ceil(len(bytes_in) * 8 / self.block_capacity)

        # create input structure
        bits_in_padded = np.full((num_blocks * self.block_capacity), padding, dtype=np.uint8)
        bits_in_padded[0:len(bytes_in)*8] = np.unpackbits(bytes_in)
        bits_in_packed = np.reshape(bits_in_padded, (num_blocks, self.block_capacity))

        # create output strcuture
        bits_out_encoded = np.empty(num_blocks * self.block_size, dtype=np.uint8)

        for ii, in_block in enumerate(bits_in_packed):
            lsb = ii * self.block_size
            msb = (ii+1) * self.block_size
            bits_out_encoded[lsb:msb] = self._encode_block(in_block)

        bytes_out_encoded = np.packbits(bits_out_encoded)
        return bytes_out_encoded



    def _encode_block(self, in_block):
        out_block = np.empty(self.block_size, dtype=np.uint8)

        parity_locs = []
        prev_loc = -1
        for ii in reversed(range(self.block_overhead-1)):
            loc = 2**ii + prev_loc
            parity_locs.append( (loc, 2**ii) )
            prev_loc = loc
        parity_locs.append((parity_locs[-1][0]+1, 0))
        in_block_idx = 0
        for ii in range(self.block_size):
            if ii == parity_locs[0][0]:
                _, mask_period = parity_locs.pop(0)
                out_block[ii] = self._compute_parity_bit_using_mask(out_block[0:ii], mask_period)
            else:
                out_block[ii] = in_block[in_block_idx]
                in_block_idx += 1

        return out_block

    def _compute_parity_bit_using_mask(self, in_block, mask_period):
        mask_period_cntr = 0
        counting_region = True
        one_count = 0
        for ii, bit in enumerate(in_block):
            if counting_region:
                one_count += bit

            if mask_period == 0:
                pass
            if mask_period_cntr >= mask_period-1:
                mask_period_cntr = 0
                counting_region = not counting_region
            else:
              mask_period_cntr += 1
        #print(f"{in_block} with mask_period = {mask_period} has one_count = {one_count & 1}")
        return one_count & 1
            


            
            

            

    def decode(self, bytes_in, padding=0):
        bits_in = np.unpackbits(bytes_in)

        


    def _is_power_of_two(self, val):
        exp = int(math.log(val, 2))
        return val == 2**exp





#   i             0 1 2 3 4 5 6 7 
#   coverage            a   b c
#   a             X X X X - - - -
#   b             X X - - X X - -
#   c             X - X - X - X -
#   
#   a = 2**2 - 1
#   b = a + 2**1
#   c = b + 2**0




