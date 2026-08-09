# ====================
# === Manage Files ===
# ====================

import os

def file_exists(filename):
    return os.path.exists(filename)


def read_file(filename):

    with open(filename, "r") as file:
        return file.readlines()


def write_file(filename, text):

    with open(filename, "w") as file:
        file.write(text)


def append_file(filename, text):

    with open(filename, "a") as file:
        file.write(text)
        
# _________________________________________________________________________________________________