import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_file(file, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)

    # Get the absolute path of the app directory
    app_dir = os.path.abspath(os.path.dirname(__file__))

    # Specify the absolute path where you want to save the encrypted file
    encrypted_path = os.path.join(app_dir, 'static', 'encrypted', 'encrypted_' + file.filename)

    with open(encrypted_path, 'wb') as f_out:
        f_out.write(cipher.iv)
        while True:
            chunk = file.read(1024 * cipher.block_size)
            if len(chunk) == 0:
                break
            elif len(chunk) % cipher.block_size != 0:
                chunk = pad(chunk, cipher.block_size)
            f_out.write(cipher.encrypt(chunk))

    return encrypted_path

def decrypt_file(file, key):
    # Get the absolute path of the app directory
    app_dir = os.path.abspath(os.path.dirname(__file__))
     # Specify the absolute path where you want to save the encrypted file
    decrypted_path = os.path.join(app_dir, 'static', 'encrypted', '' + file.filename)
    print(decrypted_path)
    with open(decrypted_path, 'rb') as f_in:
        iv = f_in.read(16)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)

        # Get the absolute path of the app directory
        app_dir = os.path.abspath(os.path.dirname(__file__))

        # Specify the absolute path of the encrypted file
        encrypted_file_path = os.path.join(app_dir, 'static', 'encrypted', file.filename)

        # Specify the absolute path of the decrypted file
        decrypted_file_path = os.path.join(app_dir, 'static', 'decrypted', 'decrypted_' + file.filename)

        with open(encrypted_file_path, 'rb') as encrypted_file, open(decrypted_file_path, 'wb') as decrypted_file:
            while True:
                chunk = encrypted_file.read(1024 * cipher.block_size)
                if len(chunk) == 0:
                    break
                decrypted_chunk = cipher.decrypt(chunk)
                if len(decrypted_chunk) < len(chunk):
                    decrypted_chunk = unpad(decrypted_chunk, cipher.block_size)
                decrypted_file.write(decrypted_chunk)

    return decrypted_file_path