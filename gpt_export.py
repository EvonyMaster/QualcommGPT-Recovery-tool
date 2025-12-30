import struct
import sys
import os

def generate_xml(partitions, output_file="rawprogram_generated.xml"):
    with open(output_file, 'w') as f:
        f.write('<?xml version="1.0" ?>\n<program>\n')
        for p in partitions:
            # Creamos la línea XML siguiendo el estándar de Qualcomm
            line = (f'  <program filename="{p["name"]}.img" '
                    f'label="{p["name"]}" '
                    f'size_in_kb="{p["size_kb"]}" '
                    f'start_sector="{p["start"]}"/>\n')
            f.write(line)
        f.write('</program>')
    print(f"\n[!] Archivo XML generado: {output_file}")

# (Integrar esto en tu script actual capturando los datos en una lista de diccionarios)
