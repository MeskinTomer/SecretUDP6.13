"""
Author: Tomer Meskin
Date: 16/02/24
Client of secret communication above UDP
"""

# Imports
from scapy.all import *
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send


def handle_message(message):
    """
    Formats the message accordingly and sends it
    :param message: The message from the client
    :return None
    """
    server_ip = input("Enter the other's IP address: ")
    for char in message:
        ascii_val = ord(char)
        packet = IP(dst=server_ip) / UDP(dport=ascii_val)
        send(packet)


def main():
    message = input("Enter your message here: ")
    print("Handling message")
    handle_message(message)
    print("Message sent")


if __name__ == '__main__':
    main()
