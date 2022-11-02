# cipher_ey2335
[![Documentation Status](https://readthedocs.org/projects/cipher-yazid-ega/badge/?version=latest)](https://cipher-yazid-ega.readthedocs.io/en/latest/?badge=latest)

A great package for hw07! It is the tool to encrypt and decrypt text using Caesar Cipher.

## Installation

```bash
$ pip install cipher_ey2335
```

## Usage

Encrypt text using Caesar Cipher method. 
    It converts each letter by certain shifts.

#### Parameters
    text : Text or string type parameter.
        Text that you would like to encrypt. It should be alphabet only.
        Number and symbol cannot be encrypted.
    shift : Integer type parameter. It can be positive or negative value.
        A number letter shift you expect to change the original text.
    encrypt: A boolean type parameter. The default is True.
        If it is True, then the text will be encrypted. 
        If the value is False, the function will decrypt the text.
    
#### Returns
    String type output. Encrpyted text by how many shifts that determined.

#### Examples
    Encryption:
    >>> from cipher_yazid_ega import cipher_ey2335
    >>> cipher_ey2335.cipher(text='wallnut', shift=1, encrypt=True)
        Output : 'xbmmvu'

    Decryption:
    >>> from cipher_yazid_ega import cipher_ey2335
    >>> cipher_ey2335.cipher(text='xbmmvu', shift=1, encrypt=True)
        Output : 'wallnut'

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`cipher_ey2335` was created by Ega Kurnia Yazid. It is licensed under the terms of the MIT license.

## Credits

`cipher_ey2335` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
