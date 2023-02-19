from flask import Flask, render_template, request, send_file
from app.encryption import encrypt_file, decrypt_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['file']
    key = request.form['key']
    print(file)

    encrypted_file = encrypt_file(file, key)

    return send_file(encrypted_file, as_attachment=True)

@app.route('/decrypt_file_func', methods=['POST'])
def decrypt_file_func():
    file = request.files['file']
    key = request.form['key']

    print(file)

    decrypted_file_path = decrypt_file(file, key)

    return send_file(decrypted_file_path, as_attachment=True)
