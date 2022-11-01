from cipher_ey2335 import cipher_ey2335

# Importing pytest
import pytest

## Testing single letter word
def test_singleword_cipher():
    singleword = ['a','b','c'] # Generate set of single word to be tested
    expected = ['c','d','e'] # Generate expected return
    # Iterate a set of test for every member in `singleworld``
    for i in range(0,3):
        assert cipher_ey2335.cipher(singleword[i], shift=2) == expected[i]