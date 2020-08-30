#!/usr/bin/env python3

def get_file_generator(path):
    """Get a file generator
    That will yield a file line
    """
    with open(path, "r") as file:
        for line in file:
            yield line
