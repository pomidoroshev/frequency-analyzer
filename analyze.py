#!/usr/bin/env python3
"""
Words Frequency Analyzer
"""
import argparse
from collections import defaultdict
import re
import sys


def get_words(string):
    """
    Generate lowercase words from given string
    """
    # TODO: Detect "don't" as one word (now it's "don" and "t")
    for word in re.finditer(r'(\w+)', string, flags=re.U):
        yield word.group(0).lower()


def print_words(filename):
    """
    Print sorted words frequency from file with given filename
    """
    frequency = defaultdict(int)
    for line in open(filename, 'r'):
        for word in get_words(line):
            frequency[word] += 1
    try:
        for item in sorted(frequency.items(), key=lambda x: (-x[1], x[0])):
            sys.stdout.write('%s: %s\n' % item  )
    except (BrokenPipeError, IOError):
        # For piping without exceptions (`./analyze.py <filename> | head`)
        pass
    sys.stderr.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Words Frequency Analyzer')
    parser.add_argument('filename', type=str, help='Input file name')
    args = parser.parse_args()
    print_words(args.filename)
