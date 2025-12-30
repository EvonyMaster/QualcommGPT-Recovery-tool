Qualcomm/Xiaomi GPT Partition Recovery Tool
A specialized Python utility designed to parse and recover the GPT (GUID Partition Table) structure from Xiaomi/Qualcomm official firmware images (e.g., gpt_backup0.bin).

This tool was specifically developed to handle the byte-alignment shifts and offset displacements often found in Xiaomi Mi 4i (Ferrari) official fastboot images, which typically cause standard tools like gdisk or sgdisk to fail or display corrupted data.

Features
Auto-Alignment: Detects and corrects 1-byte offsets that cause UTF-16 partition names to appear as corrupted/Chinese characters.

Brute-Force Scanning: Scans the binary byte-by-byte to locate valid Partition Entry Arrays even when headers are missing or non-standard.

Qualcomm Optimized: Recognized common partition labels (sbl1, rpm, tz, aboot, modem, system, etc.).

Precise LBA Calculation: Provides exact Start/End LBA, sector counts, and human-readable sizes in MB.

Technical Context
In many Xiaomi firmwares, the gpt_backup0.bin file does not start at LBA 0 of a disk image. Instead, it is a raw dump of the partition entries. Standard parsers expect a specific header at byte 0; this script bypasses that requirement by validating the data structures themselves.

Usage
Clone or download the script to your local development environment.

Run the script by pointing it to your GPT binary file:

Bash

python3 gpt_reveal.py ~/path/to/your/images/gpt_backup0.bin
Example Output
Plaintext

[+] Clean Partition Table: gpt_backup0.bin
ID   Name            Start LBA    End LBA      Size      
-----------------------------------------------------------------
0    sbl1            34           4129             2.00 MB
1    sbl1bak         4130         8225             2.00 MB
...
33   system          917504       4325375       1664.00 MB
34   cache           4325376      5111807        384.00 MB
Requirements
Python 3.x

No external dependencies (uses standard libraries: struct, sys, os).

License
This project is licensed under the MIT License.

Copyright (c) 2024 Florin Mitroi (digitart3.0@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the software without restriction. See the LICENSE file for more details.
