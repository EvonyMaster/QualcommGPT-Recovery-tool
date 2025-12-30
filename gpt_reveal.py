#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Qualcomm/Xiaomi GPT Partition Table Recovery Tool
# Optimized for Xiaomi Mi 4i (Ferrari) and similar platforms.
#
# Developed by: Florin Mitroi aka digitart3.0@gmail.com
# License: MIT License (https://opensource.org/licenses/MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files, to deal in the software
# without restriction, including the copyright notice.
# ----------------------------------------------------------------------------
import struct
import sys
import os

def clean_gpt(filename):
    if not os.path.exists(filename): return
    
    SECTOR_SIZE = 512
    with open(filename, 'rb') as f:
        data = f.read()
    print(f"\n# ----------------------------------------------------------------------------")
    print(f"\n# GPT Recovery Tool for Xiaomi/Qualcomm")
    print(f"\n# Copyright (c) 2024 Florin Mitroi aka digitart3.0@gmail.com")
    print(f"\n# Licensed under the MIT License.")
    print(f"\n# ----------------------------------------------------------------------------")
    print(f"\n[+] Tabla de Particiones Limpia: {os.path.basename(filename)}")

    print(f"{'ID':<4} {'Nombre':<15} {'Inicio LBA':<12} {'Fin LBA':<12} {'Tamaño':<10}")
    print("-" * 65)

    count = 0
    for i in range(0, len(data) - 128, 128):
        name_data = data[i+56:i+128].split(b'\x00\x00\x00')[0]
        
        try:
            name = name_data.replace(b'\x00', b'').decode('ascii', errors='ignore').strip()
            
            if len(name) > 1 and name.isprintable():
                start_lba = struct.unpack('<Q', data[i+32:i+40])[0]
                end_lba = struct.unpack('<Q', data[i+40:i+48])[0]
                
                if 0 < start_lba < 0xFFFFFFFF:
                    size_mb = ((end_lba - start_lba) + 1) * SECTOR_SIZE / (1024 * 1024)
                    print(f"{count:<4} {name:<15} {start_lba:<12} {end_lba:<12} {size_mb:>8.2f} MB")
                    count += 1
        except:
            continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 gpt_clean_reveal.py <archivo.bin>")
    else:
        clean_gpt(sys.argv[1])
