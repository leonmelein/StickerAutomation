#!/usr/bin/env python
import os
from pathlib import Path

def test():
    x = Path('./')
    packs = list(filter(lambda y: y.is_dir(), x.iterdir()))
    packs = [pack for pack in packs if not str(pack).startswith((".", "__"))]
    print("Checking packs...")

    for pack in packs:
        os.chdir(pack)
        print("\u001b[30;1mPack: {}\u001b[0m".format(pack))
        errors = 0

        required_files = ["title.txt", "author.txt"]
        for file in required_files:
            try:
                checkFileExists(file)
            except AssertionError:
                print(
                    "\u001b[31m- {} is missing. Please add this file!\u001b[0m".format(file))
                errors = errors + 1
        
        try:
            checkNumberOfFiles()
        except AssertionError:
            print(
                "\u001b[31m- Too many files in pack! Max 30 stickers are allowed.\u001b[0m")
            errors = errors + 1

        try:
            checkNumbering()
        except AssertionError:
            print(
                "\u001b[31m- There are files outside the proper numbering sequence. Please number all stickers 1 through 30 (max).\u001b[0m")
            errors = errors + 1

        checkOrError = "✓" if errors == 0 else "❌"
        color = "\u001b[32m" if errors == 0 else "\u001b[31m"
        print("{}{} Errors found in pack: {} \u001b[0m\n".format(
            color, checkOrError, errors))
        os.chdir("..")

def checkFileExists(file):
    assert os.path.isfile(file) == True

def checkNumberOfFiles():
    assert len(getPackFiles()) <= 33

def checkNumbering():
    ls = getPackFiles()
    allowedFiles = ["{}.webp".format(i) for i in range(1,31)]
    allowedFiles = allowedFiles + ["title.txt", "author.txt", "0.png"]
    
    forbiddenFiles = [item for item in ls if item not in allowedFiles]
    assert len(forbiddenFiles) == 0

def getPackFiles():
    return [item for item in os.listdir() if not item.startswith(".")]


if __name__ == "__main__":
    test()
