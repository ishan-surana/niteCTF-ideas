from scapy.all import *
from itertools import cycle

def image_to_bits(image_path):
    with open(image_path, 'rb') as image_file:
        # Read the entire content of the image file
        image_data = image_file.read()

    # Convert each byte to its binary representation
    bits_list = [format(byte, '08b') for byte in image_data]

    # Concatenate the binary strings to get the bits
    bits_string = ''.join(bits_list)

    return bits_string

def xor_binary_strings(binary_str1, binary_str2):
    # Use itertools.cycle to create an iterator for the shorter string
    xor_iterator = cycle(binary_str2)

    # XOR each pair of corresponding bits
    result = ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(binary_str1, xor_iterator))

    return result

# Replace 'output.pcap' with the desired name for your output file
output_filename = 'xored_images_in_pcap.pcap'

# Replace '192.168.1.1' and '192.168.1.2' with appropriate source and destination IP addresses
source_ip = '192.168.1.1'
destination_ip = '192.168.1.2'

# Create a list of packets with XORed images
xored_packets = []

def bitstostring(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

binary_str2 = ''.join(format(ord(char), '08b') for char in "nite{4lmo5t_th3re_bu+_n0t_yet!}")

# Loop through images from 1.jpg to 190.jpg
for i in range(1, 191):
    image_path = f'source/{i}.jpg'
    # Get the bits from the image file
    image_bits = image_to_bits(image_path)

    # XOR with the provided binary string
    result = xor_binary_strings(image_bits, binary_str2)

    # Create packet with XORed image data
    xor_image_data = bytes(int(result[i:i+8], 2) for i in range(0, len(result), 8))
    packet = IP(src=source_ip, dst=destination_ip) / ICMP() / Raw(load=xor_image_data)
    xored_packets.append(packet)

# Wrapping the list of packets in a PcapWriter context to write to a pcap file
with PcapWriter(output_filename, append=True, sync=True) as pcap_writer:
    for packet in xored_packets:
        pcap_writer.write(packet)
