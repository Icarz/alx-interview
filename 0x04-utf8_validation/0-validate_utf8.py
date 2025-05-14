#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Returns True if data is a valid UTF-8 encoding, else False.
    data: list of integers representing bytes (0 <= x <= 255)
    """
    remaining_bytes = 0

    for byte in data:
        # Only keep the last 8 bits
        byte = byte & 0xFF

        if remaining_bytes == 0:
            # Count how many leading 1's
            if (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            elif (byte >> 7) == 0b0:
                remaining_bytes = 0
            else:
                return False
        else:
            # Continuation bytes must start with '10'
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
