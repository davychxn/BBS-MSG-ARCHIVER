"""
Author: Davy (Dawei) Chen
Email: cndv3996@163.com
Location: Guangzhou, China
Date: 2024-11-04
Usage: To Archive BBS Message
"""

import os
from Archiver import Archiver

if __name__ == "__main__":
    archiver = Archiver()
    archiver.cleanup_output_only()
