# Pixel Manipulation for Image Encryption and Decryption

This project provides a simple image encryption tool using pixel manipulation. Users can perform operations like swapping pixel values or applying basic mathematical operations to each pixel to encrypt and decrypt images.

## Features

- Encrypt an image by shuffling its pixel values based on a key.
- Decrypt an encrypted image using the same key to restore the original image.
- Allows user input for selecting the operation (encryption or decryption), image file path, key, and output file path.

## Requirements

- Python 3.6 or higher
- Pillow library
- NumPy library

## Usage

1. Run the script:

    ```bash
    python pixel_manipulation.py
    ```

2. Follow the prompts:

    - Choose whether to encrypt or decrypt the image by entering 'E' or 'D'.
    - Provide the path to the image file.
    - Enter an integer key for encryption/decryption.
    - Specify the output path for the resulting image.
