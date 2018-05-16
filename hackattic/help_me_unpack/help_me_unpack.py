#! /usr/bin/env python3

import argparse
import base64
import json
import urllib.request

import requests

PROBLEM_URL = 'https://hackattic.com/challenges/help_me_unpack'


def byte_val_signed(bits):
    unsigned_part = int(bits[1:], base=2)
    return unsigned_part if bits[0] == '0' else -128 + unsigned_part


def byte_val_unsigned(bits):
    return int(bits, base=2)


def to_int(bits):
    byte_0 = bits[0:8]
    byte_1 = bits[8:16]
    byte_2 = bits[16:24]
    byte_3 = bits[24:32]
    return byte_val_unsigned(byte_0) + 256 * byte_val_unsigned(byte_1) + \
        256**2 * byte_val_unsigned(byte_2) + 256**3 * byte_val_signed(byte_3)


def to_uint(bits):
    four_bytes = [bits[byte_num * 8:(byte_num + 1) * 8] for byte_num in range(4)]
    four_bytes = list(map(lambda byte_01: int(byte_01, base=2), four_bytes))
    four_bytes = [four_bytes[byte_num] * 256**byte_num for byte_num in range(4)]
    return sum(four_bytes)


def to_short(bits):
    byte_0 = bits[0:8]
    byte_1 = bits[8:16]
    return byte_val_unsigned(byte_0) + 256 * byte_val_signed(byte_1)


def to_float(bits):
    # Little Endian made me do it
    bits = bits[24:32] + bits[16:24] + bits[8:16] + bits[0:8]
    # _sign_ seems to be in_sign_ificant
    exponent = bits[1:9]
    mantissa = bits[9:32]
    mantissa_value = sum(
        [(1 / 2) ** (bit_num + 1) * int(mantissa[bit_num]) for bit_num in range(0, 23)]
    )
    exponent = int(exponent, base=2)
    return (1 + mantissa_value) * 2**(exponent - 127)


def to_double(bits):
    byte_list = [bits[b_num * 8:(b_num + 1) * 8] for b_num in range(8)]
    bits_with_bytes_reversed = ''.join(reversed(byte_list))
    return to_big_endian_double(bits_with_bytes_reversed)


def to_big_endian_double(bits):
    exponent = bits[1:12]
    mantissa = bits[12:64]
    mantissa_value = sum(
        [(1 / 2) ** (bit_num + 1) * int(mantissa[bit_num]) for bit_num in range(0, 52)]
    )
    exponent = int(exponent, base=2)
    return (1 + mantissa_value) * 2**(exponent - 1023)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', required=True)
    args = parser.parse_args()
    json_input = urllib.request.urlopen(
        f'{PROBLEM_URL}/problem?access_token={args.token}'
    )
    b64_bytes_input = json.loads(json_input.read())['bytes']
    raw_bytes = base64.standard_b64decode(b64_bytes_input)
    raw_bits = [b[2:].rjust(8, '0') for b in map(bin, bytearray(raw_bytes))]
    bit_blob = ''.join(raw_bits)
    # int is 32-bit wide
    int_part = bit_blob[0:32]
    # uint is also 32-bit wide
    uint_part = bit_blob[32:64]
    # short is 16-bit wide, but right after it there's 16 bits of whitespace (?)
    short_part = bit_blob[64:80]
    # float is 32-bit wide
    float_part = bit_blob[96:128]
    # double is 64-bit wide
    double_part = bit_blob[128:192]
    # big endian(ed) double is also 64-bit wide
    big_endian_double_part = bit_blob[192:256]
    results = {
        'int': to_int(int_part),
        'uint': to_uint(uint_part),
        'short': to_short(short_part),
        'float': to_float(float_part),
        'double': to_double(double_part),
        'big_endian_double': to_big_endian_double(big_endian_double_part)
    }
    json_results = json.dumps(results)
    post_url = f'{PROBLEM_URL}/solve?access_token={args.token}'
    response = requests.post(post_url, data=bytes(json_results, 'utf-8'))
    print(response.status_code)
    print(response.text)
