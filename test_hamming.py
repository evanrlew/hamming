from hamming import Hamming
import numpy as np

def test_hamming_single_block_encode_only():
#   i             0 1 2 3 4 5 6 7 
#   data = 11     1 0 1 - 1
#   coverage            a   b c
#   a             X X X S - - - -
#   b             X X - - X S - -
#   c             X - X - X - S -
#   result        1 0 1 0 1 0 1 0

    ham = Hamming(block_size=8)
    in_block = np.unpackbits(np.array([0b1011], dtype=np.uint8)) #4'b1011
    bits = ham._encode_block(in_block[4:8])
    expected_bits = np.unpackbits(np.array([0b10101010], dtype=np.uint8))
    assert (bits == expected_bits).all()

def test_hamming_multiple_block_encode_only():
    ham = Hamming(block_size=16)
    in_block = bytearray(b"e")
    bits = ham.encode(in_block)
    assert len(bits) == 2

#def test_hamming_simply_reconstruction():
#    ham = Hamming()
#    bits_ecc = ham.encode(bits)
#    bits_reconstructed, _ = ham.decode(bits_ecc)
#
#    assert bits == bits_reconstructed
#
#
#def test_hamming_error_detection():
#    ham = Hamming()
#    bits_ecc = ham.encode(bits)
#    # corrupt bits
#    corruption_loc = None 
#    bad_bits = bits_ecc # FIXME
#    bits_reconstructed, errs = ham.decode(bad_bits)
#
#    assert bits == bits_reconstructed
#    assert errs == corruption_loc
#
#def test_hamming_double_error_detection():
#    pass
