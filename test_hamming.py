from hamming import Hamming

def test_hamming_simply_reconstruction():
    ham = Hamming()
    bits_ecc = ham.encode(bits)
    bits_reconstructed, _ = ham.decode(bits_ecc)

    assert bits == bits_reconstructed


def test_hamming_error_detection():
    ham = Hamming()
    bits_ecc = ham.encode(bits)
    # corrupt bits
    corruption_loc = None 
    bad_bits = bits_ecc # FIXME
    bits_reconstructed, errs = ham.decode(bad_bits)

    assert bits == bits_reconstructed
    assert errs == corruption_loc

def test_hamming_double_error_detection():
    pass



