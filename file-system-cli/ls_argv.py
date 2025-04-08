# import module like sys, pathlib(path)
import sys
from pathlib import Path

# defined args_count and assigned it to length of sys.argv
if(args_count:=len(sys.argv))>2:
    print(f" Expected One Argument, received {args_count-1}")
    raise SystemExit(2)

elif args_count<2:
    print(f'You must specify target directory')
    raise SystemExit(2)

# get the target_dir using Path obj
target_dir = Path(sys.argv[1])

# check if the tar_dir is valid
if not target_dir.is_dir():
    print(f"Not a valid directory")
    raise SystemExit(1)

# iterate over the dir
for entry in target_dir.iterdir():
    print(entry.name)
