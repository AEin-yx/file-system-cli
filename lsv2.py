import argparse
from pathlib import Path
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("-l", '--long', action='store_true')
args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print(f'No Such Directory called {target_dir} exists')
    raise SystemExit(1)

def output_format(entry, long=False):
    """
        Format the output of a directory entry.

    Args:
        entry (Path): A Path object representing the file or directory.
        long (bool): If True, includes the file size and last modified date.

    Returns:
        str: A formatted string with its size, modification date and filename.
    """
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime("%b %d %H:%M:%S")
        return f'{size:>6d} {date} {entry.name}'
    return entry.name

for entry in target_dir.iterdir():
    print(output_format(entry, long=args.long))
