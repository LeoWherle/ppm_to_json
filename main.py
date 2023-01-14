#!/usr/bin/env python3
import sys;
from ppm_to_json import ppm_to_json;

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    ppm_to_json(input_file)

if __name__ == '__main__':
    main()


