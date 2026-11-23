"""Entrypoint: copy the pre-written entry word into the output directory.

Standard library only: no third-party imports, no network, no writes
into this directory.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )
    print("wrote " + os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
