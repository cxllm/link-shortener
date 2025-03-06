import sys
import os
import importlib

try:
    _, command, *_ = sys.argv
    c = importlib.import_module(f"commands.{command}")
    c.execute()
except:
    print("Available commands")
    for i in os.listdir("commands"):
        if i != "__pycache__":
            print(i.replace(".py", ""))
