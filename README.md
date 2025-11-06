[![License](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

# BBS MESSAGE ARCHIVER

## Overview
Many BBS services don't support Archive Operations yet. When you have the need to Archive some messages you posted, but prefer not removing right away. This project provides a solution to Encrypt your message. You could update your post with Ciphered Message, and keep the Key somewhere for later Decryption. This project, for your convenience, takes a natual language text string as the Key instead of a HEX string.

## Techinal Details
```
                                  (Original Message) --- [Compression] --- 
                                                                          |
(Natual Language Key String) --- [SHA256] --- [HEX Key] ---               |
                                                           | --- [AES-256-CTR Cipher] --- (Archived Cipher Message)
                                               (HEX IV) ---
```

## Example

### Original Message
```
What's the pursuit of every Clearing Houses?
```

### Key Text
```
No Default !
```

### Archived Cipher Message (Update This To Your BBS Post)
```
ARCHIVE TIME: 2025-11-06 15:52:48
DE-ARCHIVE INSTRUCTION: https://github.com/davychxn/BBS-MSG-ARCHIVER
ENCRYPTION ALGORITHM: AES-256-CTR
PADDING: NONE (stream mode)
NOTE: Compatible with CyberChef (full 16-byte counter, big-endian)

-- KEY --
KEY TEXT: <YOUR KEY TEXT HIDDEN>
KEY (hex): b2b9595e940627cf48ac78c28cf102b90a335b3a3dbd85f6ce17c848e890c8aa

-- IV / NONCE --
FULL IV (hex): 0123456789ABCDEF0123456789ABCDEF

-- ARCHIVED TEXT --
ARCHIVED TEXT (base64):
o3WyjlGiYsfYl3d4b+20Cvkm0MoV6/oD3jZHUf0FABk2dTd2m2rmhFNNIl3BSlXZz9g4+w==
```

### CyberChef Recipe
[Definition of Decryption](./cyberchef/CyberChef_Decrypt_Recipe.txt)

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

3. Copy content of [CyberChef Decryption Recipe](./cyberchef/CyberChef_Decrypt_Recipe.txt) to `Recipe`, and LOAD:
![Fill in CyberChef Decrypt Recipe](./assets/cyberchef/load_decrypt_recipe2.jpg)

4. Do the following values copy:
 ______________________________________________________________________________________________
|  COPY  |        FROM (FILE: archive_output.txt)        |    TO (CyberChef: AES Decrypt UI)   |
|--------|-----------------------------------------------|-------------------------------------|
| FIELDS | `KEY (hex) `                                  | `Key (HEX)`                         |
| FIELDS | `FULL IV (hex)`                               | `IV (HEX)`                          |
| FIELDS | `ARCHIVED TEXT (base64)`                      | `Input`                             |

5. BAKE to Output:
![BAKE !](./assets/cyberchef/decrypt.jpg)

## Show or Hide KEY TEXT In Archived Message
Change input Argument `key_text_replacer` of Class `Archive`'s Constructor in `./bbs_msg_archiver.py` 
 _______________________________________________________________________________________________________________________________________
|        |                key_text_replacer                 |          Functionality            |       Seen In Archived Message        |
|--------|--------------------------------------------------|-----------------------------------|---------------------------------------|
|        | `None`                                           | Show Key Text                     | `<KET TEXT>` (content of `./key.txt`) |
|        | `""` (Empty str)                                 | Hide Key Text                     | `<YOUR KEY TEXT HIDDEN>`              |
|        | `"<Customized Message>"` (Non-Empty str)         | Show Customized Message           | `<Customized Message>`                |

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

## All Input & Output Files Reference
 ______________________________________________________________________________________________________________________________
|  Input/Output  |               Filename                 |                            Usage                                   |
|----------------|----------------------------------------|--------------------------------------------------------------------|
| Input          | `./encrypt_input.txt`                  | `Original Message`                                                 |
| Input          | `./key.txt`                            | `Key String` (Natual Language)                                     |
| Output/Input   | `./encrypt_output.txt`                 | `Archived Cipher Text + IV`                                        |
| Output         | `./encrypt_output_ciphertext_only.txt` | `Archived Cipher Text Only` (Without IV)                           |
| Output         | `./archive_output.txt`                 | `Archived Cipher Text To Update To BBS` (With Decrypt Information) |
| Output         | `./decrypt_output.txt`                 | `De-Archived Original Message`                                     |

## All Cmds Reference

### Archive
```python
python bbs_msg_archiver.py
```
### De-Archive
```python
python bbs_msg_dearchiver.py
```
### Cleanup Outputs Only
```python
python cleanup_output_only.py
```
### Cleanup Both Inputs & Outputs
```python
python cleanup_all.py
```
### Install Python Package Dependents
```
python -m pip install --upgrade pip
python -m pip install cryptography
```

## Contribution
Contributions are welcome! Please submit a pull request for any enhancements or bug fixes.

## Dual Licenses (LGPL-3.0 + Commercial License)

This project is dual-licensed:

1. **Open Source**: Under the [GNU Lesser General Public License v3.0 (LGPL-3.0)](LICENSE) — free for non-commercial and open-source use.
2. **Commercial Use**: A commercial license is available for closed-source projects, enterprise deployment, or relieve from compliance obligations.

[View Commercial License Options](LICENSE-Commercial.md)

If you're using this library in a commercial product and want to:
- Keep your source code private
- Avoid LGPL distribution requirements
- Get professional support

Please contact us: **[davy.chen@1637.com](mailto:davy.chen@1637.com)** (Please remove the greatest numeric char from the email to contact, thanks)
