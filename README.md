# flask-AES-256-encryption-webapp
This is a simple Flask web application that allows you to encrypt and decrypt files using the AES encryption algorithm. The app is built using Python 3, Flask, and the PyCryptodome library.

## Getting started
To run the application locally, follow these steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/<username>/<repository>.git

```
2. Install the required dependencies using pip:
```
pip install -r requirements.txt

```
3. Start the Flask development server:
```
python run.py

```
4. Navigate to `http://localhost:5000/` in your browser.

## Usage
To use the application, follow these steps:

1. Upload a file that you want to encrypt by clicking on the "Upload" button on the homepage.
2. Enter an encryption key and click on the "Encrypt File" button to encrypt the file. The encrypted file will be downloaded automatically.
3. To decrypt a file, click on the "Decrypt" button in the top navigation menu. Upload the encrypted file and enter the decryption key, then click on the "Decrypt File" button. The decrypted file will be downloaded automatically.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
This project was inspired by the Flask Mega-Tutorial by Miguel Grinberg. Special thanks to the PyCryptodome team for providing a great library for AES encryption in Python.

I hope this helps! Let me know if you have any further questions.

