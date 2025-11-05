# BBS MESSAGE ARCHIVER

## Overview
Many BBS services don't support Archive Operations yet. When you have the need to Archive some messages you posted, but prefer not removing right away. This project provides a solution to Encrypt your message. You could update your post with Ciphered Message, and keep the Key somewhere for later Decryption. This project, for your convenience, takes a natual language text string as the Key instead of a HEX string.

## Techinal Details
```
(Natual Language Key String) --- [SHA256] --- [HEX Array] --- 
                                                             | --- [AES-256-CTR Cipher] --- 
                                               (IV Value) ---                              | --- (Archived Message)
                                                                     (Original Message) --- 
```

### CyberChef Recipe
1. [Definition for Encryption](./cyberchef/CyberChef_Encrypt_Recipe.txt)
2. [Definition for Decryption](./cyberchef/CyberChef_Decrypt_Recipe.txt)

## Environment Preparation
1. Clone the Project to your local drive.
2. (Optional) Install Python dependent packages:
```
python -m pip install --upgrade pip
python -m pip install cryptography
```

## Archive Operations
1. Copy `Original Message` to `./encrypt_input.txt`.
2. Write your Natual Language `Key String` to `./key.txt`.
3. (Optional) `Environment Preparation`.
4. Run in System Cmd Console:
```python
python bbs_msg_archiver.py
```
5. Get `Archived Cipher Message` from `./archive_output.txt` in Section:
```
-- ARCHIVED TEXT --
ARCHIVED TEXT (base64):
```
6. Update to your BBS Post.

## De-Archive Operations
1. Copy `Archived Cipher Message` to `./encrypt_output.txt`.
2. Write your Natual Language `Key String` to `./key.txt`.
3. (Optional) `Environment Preparation`.
4. Run in System Cmd Console:
```python
python bbs_msg_dearchiver.py
```
5. Get `Original Message` from `./decrypt_output.txt`.

## Cleanup Operations

### Cleanup Outputs
Run in System Cmd Console:
```python
python cleanup_output_only.py
```

### Cleanup Outputs + Truncate Input & Key To 0 Size
Run in System Cmd Console:
```python
python cleanup_all.py
```

## Contribution
Contributions are welcome! Please submit a pull request for any enhancements or bug fixes.
