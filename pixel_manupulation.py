from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key, output_path='encrypted_image.png'):
    img = Image.open(image_path)
    img_array = np.array(img)
    np.random.seed(key)
    indices = np.arange(img_array.size)
    np.random.shuffle(indices)
    flat_img_array = img_array.flatten()
    encrypted_flat_array = flat_img_array[indices]
    encrypted_array = encrypted_flat_array.reshape(img_array.shape)
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as '{output_path}'")

def decrypt_image(encrypted_image_path, key, output_path='decrypted_image.png'):
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_img)
    np.random.seed(key)
    indices = np.arange(encrypted_array.size)
    np.random.shuffle(indices)
    flat_encrypted_array = encrypted_array.flatten()
    decrypted_flat_array = np.zeros_like(flat_encrypted_array)
    decrypted_flat_array[indices] = flat_encrypted_array
    decrypted_array = decrypted_flat_array.reshape(encrypted_array.shape)
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as '{output_path}'")

def main():
    choice = input("Do you want to encrypt or decrypt the image? (E/D): ").strip().upper()
    image_path = input("Enter the path of the image file: ").strip()
    key = int(input("Enter the key (integer value): ").strip())
    
    if choice == 'E':
        output_path = input("Enter the output path for the encrypted image (default: encrypted_image.png): ").strip()
        if os.path.isdir(output_path):
            output_path = os.path.join(output_path, 'encrypted_image.png')
        elif not output_path:
            output_path = 'encrypted_image.png'
        encrypt_image(image_path, key, output_path)
    elif choice == 'D':
        output_path = input("Enter the output path for the decrypted image (default: decrypted_image.png): ").strip()
        if os.path.isdir(output_path):
            output_path = os.path.join(output_path, 'decrypted_image.png')
        elif not output_path:
            output_path = 'decrypted_image.png'
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
