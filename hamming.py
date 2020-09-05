import numpy as np
import math

class Hamming:
    def __init__(self, block_size=16):
        # block_size -> number of bits in a error correction region. must be power of two
        if not self._is_power_of_two(block_size):
            raise ValueError("block size={block_size} must be a power of two")
        self.block_size = block_size
        self.block_overhead = math.log(self.block_size, 2) + 1
        self.block_capacity = self.block_size - self.block_overhead

    def encode(self, bytes_in, padding=0):
        # calculated overhead and output size
        num_blocks = math.ceil(len(bytes_in) * 8 / block_capacity)

        # create input structure
        bits_in_padded = np.full((num_blocks * block_capacity), padding, dtype=np.uint8)
        bits_in_padded[0:len(bytes_in)] = np.unpackbits(bytes_in)
        bits_in_packed = np.reshape(bytes_in_padded, (num_blocks, block_capacity))

        # create output strcuture
        bits_out_encoded = np.empty(num_blocks * self.block_size)

        for in_block in bytes_in_packed:
            bits_out_encoded[?] = self._encode_block(in_block)



    def _encode_block(self, in_block):

        for ii in range(self.block_size):

            

    def decode(self, bits):
        pass


    def _is_power_of_two(self, val):
        exp = int(math.log(val, 2))
        return val == 2**exp





i             0 1 2 3 4 5 6 7 
coverage            a   b c
a             X X X X - - - -
b             X X - - X X - -
c             X - X - X - X -
