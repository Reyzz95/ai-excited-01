"""Copy the whale-breaching-clouds entry image for the make.fun competition.

The image captures a colossal humpback whale breaching through golden clouds
into a blazing sunset, with a tiny joyful surfer riding its back.
"""

import os
import hashlib
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).with_name("entry.png")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination = output_dir / "entry.png"
    output_dir.mkdir(parents=True, exist_ok=True)
    # Deterministic byte-for-byte copying keeps every run identical.
    shutil.copyfile(source, destination)
    source_hash = hashlib.sha256(source.read_bytes()).digest()
    destination_hash = hashlib.sha256(destination.read_bytes()).digest()
    if destination_hash != source_hash:
        raise SystemExit("integrity check failed: destination hash differs from source")
    print(f"source_size={source.stat().st_size}")
    print(f"destination_size={destination.stat().st_size}")


if __name__ == "__main__":
    main()
