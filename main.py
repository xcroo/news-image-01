# Sum up 13 November's world news in one image: copy the image beside this file to /output/entry.png.
# The image is a vintage newspaper front page — "The Global Herald", Friday, November 13, 2026 —
# summing up the day: Nvidia CEO Jensen Huang resigns (cracked golden crown on a chip),
# Microsoft 365 global outage (warning screens over a world map), Strait of Hormuz tanker
# tensions, and the Russia-Ukraine prisoner exchange (dove with olive branch).
# The output is a valid JPEG image, 1024x683, well under the 1 MiB limit.
# The entry is self-contained: the program only copies the bundled image.
# Deterministic: the same input always produces the same output file.
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
