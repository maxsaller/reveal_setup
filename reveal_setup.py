#!/usr/bin/python
"""Simple setup script for reveal.js presentations."""
import os
import sys
import argparse
import subprocess as sp

"""Install function"""
def install(dir):
    """Installs reveal.js into dir via git"""

    print("INSTALL...")

"""Boiler plate"""
if __name__ == "__main__":
    """Command line argument parsing"""
    parser = argparse.ArgumentParser(description="Simple setup script for reveal.js presentations")
    parser.add_argument("dir", type=str, help="directory to setup presentation in")
    args = parser.parse_args()

    """Directory safety checks"""
    if not os.path.isdir(args.dir):
        if os.path.isfile(args.dir):
            raise Exception("Path provided points to a file")
        chc = input(f"No directory exists at '{args.dir}'!\n" +
                    "Should a new directory be created? [Y/n] ")
        if chc.lower() == "y" or len(chc) == 0:
            print(f"Creating '{args.dir}' ...")
            os.mkdir(args.dir)
            install(args.dir)
        elif chc.lower() == "n":
            sys.exit()
        else:
            raise ValueError
    else:
        if not len(os.listdir(args.dir)) == 0:
            chc = input(f"Directory at '{args.dir}' is not empty!\n" +
                        "WARNING: Proceeding with installation may compromise existing content!\n" +
                        "Proceed with installation? [y/N] ")
            if chc.lower() == "n" or len(chc) == 0:
                sys.exit()
            elif chc.lower() == "y":
                install(args.dir)
            else:
                raise ValueError
        else:
            install(args.dir)
