#!/usr/bin/env python3
import sys
import base64
import os
import tempfile

def xor_encrypt(data, key):
    key_bytes = key.encode()
    result = bytearray()
    for i, byte in enumerate(data):
        result.append(byte ^ key_bytes[i % len(key_bytes)])
    return bytes(result)

def xor_decrypt(data, key):
    return xor_encrypt(data, key)

def encrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        data = f.read()
    encrypted = xor_encrypt(data, key)
    encoded = base64.b64encode(encrypted)
    with open(output_path, 'wb') as f:
        f.write(encoded)

def decrypt_file(input_path):
    with open(input_path, 'rb') as f:
        encoded = f.read()
    encrypted = base64.b64decode(encoded)
    decrypted = xor_decrypt(encrypted, key)
    return decrypted

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python locker.py <encrypt|decrypt> <input> <key> [--keep]")
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]
    key = sys.argv[3] if len(sys.argv) > 3 else None
    keep = '--keep' in sys.argv

    if mode == 'encrypt':
        if len(sys.argv) < 5:
            print("Usage: python locker.py encrypt <input> <output> <key>")
            sys.exit(1)
        output_file = sys.argv[3]
        key = sys.argv[4]
        encrypt_file(input_file, output_file, key)
        print(f"Encrypted: {input_file} -> {output_file}")

    elif mode == 'decrypt':
        with tempfile.NamedTemporaryFile(mode='wb', suffix='.md', delete=False) as tmp:
            tmp_path = tmp.name

        with open(input_file, 'rb') as f:
            encoded = f.read()
        encrypted = base64.b64decode(encoded)
        decrypted = xor_decrypt(encrypted, sys.argv[3])

        with open(tmp_path, 'wb') as f:
            f.write(decrypted)

        with open(tmp_path, 'rb') as f:
            content = f.read()

        if not keep:
            os.unlink(tmp_path)
            sys.stdout.buffer.write(content)
        else:
            print(tmp_path)

    else:
        print("Mode must be 'encrypt' or 'decrypt'")
        sys.exit(1)
