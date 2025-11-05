"""
Author: Davy (Dawei) Chen
Email: cndv3996@163.com
Location: Guangzhou, China
Date: 2024-11-04
Usage: To Archive BBS Message
"""

import os
import base64
from hashlib import sha256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from datetime import datetime

class Archiver:
    def __init__(self, iv_hex = "0123456789ABCDEF0123456789ABCDEF"):
        self.KEY_PATH = "./key.txt"
        self.ENCRYPT_INPUT_PATH = "./encrypt_input.txt"
        self.ENCRYPT_OUTPUT_PATH = "./encrypt_output.txt"
        self.ARCHIVE_PATH = "./archive_output.txt"
        self.DECRYPT_OUTPUT_PATH = "./decrypt_output.txt"
        self.FULL_IV_HEX = iv_hex
        
    def encrypt(self):
        """
        AES-256-CTR compatible with CyberChef
        Uses full 16-byte IV as counter block, increments entire block
        """
        # Read key and plaintext
        with open(self.KEY_PATH, "rb") as f:
            key_material = f.read()
        key_material = key_material.rstrip(b'\r\n \t')  # Remove trailing whitespace
        key = sha256(key_material).digest()

        with open(self.ENCRYPT_INPUT_PATH, "rb") as f:
            plaintext = f.read()

        # Use full 16-byte IV
        full_iv = bytes.fromhex(self.FULL_IV_HEX)
        if len(full_iv) != 16:
            raise ValueError("IV must be 16 bytes")
        
        # Convert IV to integer for counter operations
        initial_counter = int.from_bytes(full_iv, byteorder='big')
        
        ciphertext = bytearray()
        block_size = 16
        num_blocks = (len(plaintext) + block_size - 1) // block_size

        for i in range(num_blocks):
            # Create counter block for this iteration
            current_counter = initial_counter + i
            current_counter_block = current_counter.to_bytes(16, byteorder='big')

            # Encrypt counter block (ECB mode)
            cipher_obj = Cipher(algorithms.AES(key), modes.ECB())
            encryptor = cipher_obj.encryptor()
            keystream = encryptor.update(current_counter_block) + encryptor.finalize()

            # XOR with plaintext
            start = i * block_size
            end = start + block_size
            plain_block = plaintext[start:end]
            cipher_block = bytes(b ^ k for b, k in zip(plain_block, keystream))
            ciphertext.extend(cipher_block)

        ciphertext = bytes(ciphertext)

        # For blob output: we still output the original 16-byte IV (for compatibility with your format)
        iv_for_blob = full_iv  # Keep original 16-byte IV in blob
        blob = iv_for_blob + ciphertext
        blob_b64 = base64.b64encode(blob)
        ciphertext_b64 = base64.b64encode(ciphertext)

        # Write outputs (same as before)
        with open(self.ENCRYPT_OUTPUT_PATH, "wb") as f:
            f.write(blob_b64)

        ct_only_path = os.path.splitext(self.ENCRYPT_OUTPUT_PATH)[0] + "_ciphertext_only.txt"
        with open(ct_only_path, "w", encoding="utf-8") as f:
            f.write(f"IV (hex): {full_iv.hex()}\n")
            f.write(f"IV (base64): {base64.b64encode(full_iv).decode()}\n")
            try:
                f.write(f"IV (ascii): {full_iv.decode('ascii')}\n")
            except Exception:
                f.write("IV (ascii): (non-printable)\n")
            f.write("\nCIPHERTEXT (base64):\n")
            f.write(ciphertext_b64.decode() + "\n")

        key_hex = key.hex()
        # key_b64 = base64.b64encode(key).decode()  # No longer needed

        with open(self.ARCHIVE_PATH, "w", encoding="utf-8") as af:
            af.write(f"ARCHIVE TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            af.write("DE-ARCHIVE INSTRUCTION: https://github.com/davychxn/BBS-MSG-ARCHIVER\n")
            af.write("ENCRYPTION ALGORITHM: AES-256-CTR\n")
            af.write("PADDING: NONE (stream mode)\n")
            af.write("NOTE: Compatible with CyberChef (full 16-byte counter, big-endian)\n")
            af.write("\n-- KEY --\n")
            af.write(f"KEY (hex): {key_hex}\n")
            af.write("\n-- IV / NONCE --\n")
            af.write(f"FULL IV (hex): {self.FULL_IV_HEX}\n")
            af.write("\n-- ARCHIVED TEXT --\n")
            af.write("ARCHIVED TEXT (base64):\n")
            af.write(ciphertext_b64.decode() + "")

    def decrypt(self):
        """Decrypt using same CyberChef-compatible CTR logic"""
        with open(self.KEY_PATH, "rb") as f:
            key_material = f.read()
        key_material = key_material.rstrip(b'\r\n \t')
        key = sha256(key_material).digest()

        with open(self.ENCRYPT_OUTPUT_PATH, "rb") as f:
            blob = base64.b64decode(f.read().strip())
        if len(blob) < 16:
            raise ValueError("Input blob too short")
        full_iv = blob[:16]
        ciphertext = blob[16:]

        # Same logic as encryption
        initial_counter = int.from_bytes(full_iv, byteorder='big')

        plaintext = bytearray()
        block_size = 16
        num_blocks = (len(ciphertext) + block_size - 1) // block_size

        for i in range(num_blocks):
            # Create counter block for this iteration
            current_counter = initial_counter + i
            current_counter_block = current_counter.to_bytes(16, byteorder='big')

            # Encrypt counter block (ECB mode) - same operation as encryption
            cipher_obj = Cipher(algorithms.AES(key), modes.ECB())
            encryptor = cipher_obj.encryptor()
            keystream = encryptor.update(current_counter_block) + encryptor.finalize()

            # XOR with ciphertext
            start = i * block_size
            end = start + block_size
            cipher_block = ciphertext[start:end]
            plain_block = bytes(c ^ k for c, k in zip(cipher_block, keystream))
            plaintext.extend(plain_block)

        plaintext = bytes(plaintext)

        with open(self.DECRYPT_OUTPUT_PATH, "wb") as f:
            f.write(plaintext)
