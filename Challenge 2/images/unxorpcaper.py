from scapy.all import *
from itertools import cycle
import os

def xor_binary_strings(binary_str1, binary_str2):
    xor_iterator = cycle(binary_str2)
    result = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(binary_str1, xor_iterator))
    return result

def binary_string_to_file(binary_str, output_path):
    byte_data = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
    with open(output_path, 'wb') as file:
        file.write(byte_data)

def extract_images_from_pcap(pcap_file, output_folder, xor_key):
    packets = rdpcap(pcap_file)
    os.makedirs(output_folder, exist_ok=True)

    for i, packet in enumerate(packets):
        if Raw in packet and ICMP in packet:
            # Extract raw data from ICMP packets
            raw_data = packet[Raw].load

            # Convert raw data to binary string
            binary_str1 = ''.join(format(byte, '08b') for byte in raw_data)

            # XOR operation
            result = xor_binary_strings(binary_str1, xor_key)

            # Save the image to the output folder
            output_path = os.path.join(output_folder, f'reformed_image_{i + 1}.jpg')
            binary_string_to_file(result, output_path)

# Replace 'hola.pcap' with the path to your pcap file
pcap_file = 'xored_images_in_pcap.pcap'

# Replace '01101110...' with the correct XOR key
xor_key = ''.join(format(ord(char), '08b') for char in "nite{4lmo5t_th3re_bu+_n0t_yet!}")

# Replace 'reformed' with the desired name for your output folder
output_folder = 'reformed'

# Extract images from the pcap file and save them to the output folder
extract_images_from_pcap(pcap_file, output_folder, xor_key)
