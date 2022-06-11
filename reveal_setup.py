#!/usr/bin/python
"""Simple setup script for reveal.js presentations."""
import os
import sys
import shutil
import argparse
import subprocess as sp

"""Install function"""
def install(dir):
    """Installs reveal.js into dir via git"""
    print(f":: Installing reveal.js base repo into '{dir}'...")
    git = sp.Popen([f"git clone https://github.com/hakimel/reveal.js.git {dir}"], shell=True)
    git.wait()

    # Remove unneccessary stuff
    print(f":: Removing superfluous files...")
    
    # Directories
    for d in [".git", ".github", "test", "examples"]:
        shutil.rmtree(f"{dir}/{d}")
    
    # Files
    for f in [".gitignore", ".npmignore", "LICENSE", "demo.html", "gulpfile.js",
    "package.json", "package-lock.json", "README.md"]:
        os.remove(f"{dir}/{f}")
    
    # Copy sensible index.html
    print(f":: Installing sensible index.html template...")
    os.remove(f"{dir}/index.html")
    shutil.copyfile("index.html", f"{dir}/index.html")

    print(":: Done!")

"""Boiler plate"""
if __name__ == "__main__":
    """Command line argument parsing"""
    parser = argparse.ArgumentParser(description="Simple setup script for reveal.js presentations")
    parser.add_argument("dir", type=str, help="directory to setup presentation in")
    args = parser.parse_args()
    args.dir = os.path.abspath(args.dir)

    """Directory safety checks"""
    if not os.path.isdir(args.dir):
        if os.path.isfile(args.dir):
            raise Exception(":: Path provided points to a file")
        chc = input(f":: No directory exists at '{args.dir}'!\n" +
                    ":: Should a new directory be created? [Y/n] ")
        if chc.lower() == "y" or len(chc) == 0:
            print(f":: Creating '{args.dir}' ...")
            os.mkdir(args.dir)
            install(args.dir)
        elif chc.lower() == "n":
            sys.exit()
        else:
            raise ValueError
    else:
        if not len(os.listdir(args.dir)) == 0:
            chc = input(f":: Directory at '{args.dir}' is not empty!\n" +
                        ":: WARNING: Proceeding with installation may compromise existing content!\n" +
                        ":: Proceed with installation? [y/N] ")
            if chc.lower() == "n" or len(chc) == 0:
                sys.exit()
            elif chc.lower() == "y":
                install(args.dir)
            else:
                raise ValueError
        else:
            install(args.dir)
