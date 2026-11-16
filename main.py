"""Copy the competition entry image: a colossal whale breaching golden sunset
clouds, with a tiny joyful surfer riding on its back.
"""

import os
import hashlib
from pathlib import Path
import shutil


def main():
    source = Path(__file__).resolve().with_name("entry.png")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"

    shutil.copyfile(source, destination)
    # Copying fixed input bytes keeps every run deterministic.
    source_hash = hashlib.sha256(source.read_bytes()).digest()
    destination_hash = hashlib.sha256(destination.read_bytes()).digest()
    if source_hash != destination_hash:
        raise SystemExit("Copied entry image failed its SHA-256 integrity check")

    print(f"source_size={source.stat().st_size}")
    print(f"destination_size={destination.stat().st_size}")


if __name__ == "__main__":
    main()
