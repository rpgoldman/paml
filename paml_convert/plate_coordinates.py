"""
Generic helper functions for dealing with plate coordinates
"""

from string import ascii_letters
import re

def num2col(num: int):
    """
    Get the alpha column string from the index.
    - 1 -> A
    - 26 -> Z
    - 27 -> AA
    - 52 -> AZ
    - etc
    """
    if num < 1:
        raise ValueError("Cannot convert num to column, num is too small.")
    col = ""
    while True:
        if num > 26:
            num, r = divmod(num - 1, 26)
            col = chr(r + ord('A')) + col
        else:
            return chr(num + ord('A') - 1) + col


def col2num(col: str):
    """
    Get the index of the alpha column string.
    - A -> 1
    - Z -> 26
    - AA -> 27
    - AZ -> 52
    - etc
    """
    num = 0
    for c in col:
        if c in ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        else:
            raise Exception(f"Invalid character: {c}")
    return num


def coordinate_to_row_col(coord: str):
    m = re.match('^([a-zA-Z]+)([0-9]+)$', coord)
    if m is None:
        raise Exception(f"Invalid coordinate: {coord}")
    # convert column to index and then adjust to zero-based indices
    return (col2num(m.group(1)) - 1), (int(m.group(2)) - 1)


def coordinate_rect_to_row_col_pairs(coords: str):
    parts = coords.split(':')
    if len(parts) != 2:
        raise Exception(f"Invalid coordinates: {coords}")
    fcol, frow = coordinate_to_row_col(parts[0])
    scol, srow = coordinate_to_row_col(parts[1])

    indices = []
    for i in range(fcol, scol + 1):
        for j in range(frow, srow + 1):
            indices.append((j, i))
    return indices
