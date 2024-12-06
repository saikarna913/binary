# bit_count.py
#
# Copyright 2023-2024 Isabelle Jackson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Library for working out binary and decimal values. Using the same file for both
def bit_count(input):
    bits = []
    mult = 1

    # Work out how many bits the binary input is, and work out the largest bits value
    for count in range (len(input) -1):
        mult = mult * 2

    # For each bit, add a value to the bit counter
    for char in input:
        if char == '1':
            bits.append(int(mult))
        mult = mult / 2

    bit_str = ""
    for x in bits:
        bit_str += f"{x} + "

    # use a try catch loop to check that the input is actually binary
    try:
        bit_str = bit_str[:-2] + f"= {int(input)}"
    except:
        pass

    return bit_str

def to_twos_complement(binary_str):
    # Step 1: Invert all the bits
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)

    # Step 2: Add 1 to the inverted binary number
    twos_complement = bin(int(inverted, 2) + 1)[2:]

    # Ensure the result has the same length as the original binary string
    return twos_complement.zfill(len(binary_str))
