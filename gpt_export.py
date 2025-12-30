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

def generate_xml(partitions, output_file="rawprogram_generated.xml"):
    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" ?>\n<program>\n')
        for p in partitions:
            line = (f'  <program filename="{p["name"]}.img" '
                    f'label="{p["name"]}" '
                    f'size_in_kb="{p["size_kb"]}" '
                    f'start_sector="{p["start"]}"/>\n')
            f.write(line)
        f.write('</program>')
    print(f"\n[!] Archivo XML generado: {output_file}")

