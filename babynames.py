#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
"""
author: jodi08 aka Jo Anna Mollman with help from Amanda Yonce
"""

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""




import sys
import re
import argparse

def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    with open(filename, 'r') as f:  # open file
        names = []  # for later storage of final list
        baby_dict = {}
        read_file = f.read()  # store file in variable
    # print(read_file)  # print file and place it outside function to close file
    # regex pattern to search for 1990
        pattern = re.compile(r'Popularity in ')
        year = pattern.finditer(read_file)
        for num in year:
            date = num.span()
            names.append(read_file[date[1]:date[1] + 4])
        # print(names)
    with open(filename, 'r') as f:
        for line in f:  # loop through file to find matches for year
            # assign baby_year to pattern regex
            baby_name = re.findall(
                r'"right"><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>', line)
            for name in baby_name:  # for a year in baby_year print year
                if name[1] not in baby_dict:
                    baby_dict[name[1]] = name[0]
                if name[2] not in baby_dict:
                    baby_dict[name[2]] = name[0]
    for item in sorted(baby_dict):
        names.append(item + " " + baby_dict[item])
    return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).
    for filename in file_list:
        extracted_names = extract_names(filename)
        if not create_summary:
            print(*extracted_names, sep="\n")
        else:
            new_file = filename + ".summary"
            a = open(new_file, 'w')
            for each in extracted_names:
                a.write(each + '\n')
            a.close()


if __name__ == '__main__':
    main(sys.argv[1:])
