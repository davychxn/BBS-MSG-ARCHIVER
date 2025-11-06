# BBS MESSAGE ARCHIVER

## Overview
Many BBS services don't support Archive Operations yet. When you have the need to Archive some messages you posted, but prefer not removing right away. This project provides a solution to Encrypt your message. You could update your post with Ciphered Message, and keep the Key somewhere for later Decryption. This project, for your convenience, takes a natual language text string as the Key instead of a HEX string.

## Techinal Details
```
                                                    (Original Message) --- 
                                                                          |
(Natual Language Key String) --- [SHA256] --- [HEX Key] ---               |
                                                           | --- [AES-256-CTR Cipher] --- (Archived Cipher Message)
                                               (HEX IV) ---
```

### CyberChef Recipes
1. [Definition of Encryption](./cyberchef/CyberChef_Encrypt_Recipe.txt)
2. [Definition of Decryption](./cyberchef/CyberChef_Decrypt_Recipe.txt)

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
3. (Optional) [Environment Preparation](#environment-preparation).
4. Run in System Cmd Console:
```python
python bbs_msg_archiver.py
```
5. Update complete content of `./archive_output.txt` to your BBS Post.

## De-Archive Operations
1. Copy `Archived Cipher Message` only from Field `ARCHIVED TEXT (base64)` of `./archive_output.txt` to `./encrypt_output.txt`:
```
-- ARCHIVED TEXT --
ARCHIVED TEXT (base64):
[[[ARCHIVED CIPHER MESSAGE HERE]]]
```
2. Write your Natual Language `Key String` to `./key.txt`.
3. (Optional) [Environment Preparation](#environment-preparation).
4. Run in System Cmd Console:
```python
python bbs_msg_dearchiver.py
```
5. Get `Original Message` from `./decrypt_output.txt`.

## De-Archive Operations With Online AES Decrypt Tools

### CyberChef Example
1. Open CyberChef: https://gchq.github.io/CyberChef/

2. Load CyberChef Decrypt Recipe here:
![Load CyberChef Decrypt Recipe](./assets/cyberchef/load_decrypt_recipe.jpg)

3. Copy content of [CyverChef Decryption Recipe](./cyberchef/CyberChef_Decrypt_Recipe.txt) to `Recipe`, and LOAD:
![Fill in CyberChef Decrypt Recipe](./assets/cyberchef/load_decrypt_recipe2.jpg)

4. Do the following values copy:
 ______________________________________________________
|  COPY  |       FROM (FILE)       |   TO (CyberChef)  |
|--------|-------------------------|-------------------|
| ENTITY | archive_output.txt      | AES Decrypt UI    |
| FIELDS | KEY (hex)               | Key (HEX)         |
| FIELDS | FULL IV (hex)           | IV (HEX)          |
| FIELDS | ARCHIVED TEXT (base64)  | Input             |

5. BAKE to Output:
![BAKE !](./assets/cyberchef/decrypt.jpg)

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
