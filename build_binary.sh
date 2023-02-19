#!/bin/bash

# build the binary
pyinstaller --name=file-encryption-app --add-data="app/templates:app/templates" --add-data="app/static:app/static" --add-data="app/encryption.py:app" --add-data="app/__init__.py:app" --add-data="run.py:." --clean --hidden-import="pkg_resources.py2_warn" --onefile run.py

# remove the build directory
rm -rf build

# move the binary to the project directory
mv dist/file-encryption-app .
rm -rf dist