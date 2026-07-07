import sys
from .transpiler import transpile_source

file = sys.argv[1]
run = "--run" in sys.argv

source = open(file, encoding="utf-8").read()

py = transpile_source(source)

print("Generated Python:\n")
print(py)

if run:
    exec(py)