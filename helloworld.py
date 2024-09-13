import sys

if len(sys.argv) != 2:
    print("Usage: python helloworld.py [name]")
    sys.exit(1)

name = sys.argv[1]
#
print(f"Hello, {name}!")