"""
Author: Tomer Meskin
Date: 16/02/24
Server of secret communication above UDP
"""

# Imports
from scapy.all import *
from scapy.layers.inet import UDP, IP


def is_empty(packet):
    """
    Determines if the packet's payload is empty
    :param packet: the UDP packet to be checked
    :return: True - if packet is empty
             False - if packet has data
    """
    empty = False
    payload = packet[UDP].payload
    if isinstance(payload, Padding) and payload.load == b'\x00' * len(payload.load):
        empty = True
    return empty


def sniff_packets(packet):
    """
    Turns the packets into a message
    :param packet: The intended UDP packet to decode
    :return: None
    """
    if packet.haslayer(UDP) and is_empty(packet):
        port = packet.dport
        char_ascii = chr(port)
        print(char_ascii, end="")


def main():
    sniff(prn=sniff_packets, filter='udp')


if __name__ == '__main__':
    # Asserts
    sample_packet = IP(dst="0.0.0.0") / UDP(dport=53421) / Raw(b"Hello World!")
    assert not is_empty(sample_packet)
    main()
