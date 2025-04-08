import argparse
from pathlib import Path


# create a parser object of the argumentparser class of argparse module
parser=argparse.ArgumentParser()

# use parser obj to call method add_argument
parser.add_argument("path")

# parse arguments using parse_args and store it in args
args=parser.parse_args()

# create targ_dir by passing the args.path through Path module
targ_dir=Path(args.path)

if not targ_dir.is_dir():
    print(f"The Directory is invalid")
    raise SystemExit(1)

for entry in targ_dir.iterdir():
    print(entry.name)