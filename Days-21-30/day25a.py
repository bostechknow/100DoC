#!/usr/bin/env python3

# Implement the following in this script:
# - Take command line input
# - Use f-string to create character sheet

import argparse

parser = argparse.ArgumentParser(description='Personal information')
parser.add_argument('--name', dest='name', type=str, help='Name of the candidate')
parser.add_argument('--age', dest='age', type=int, help='Age of the candidate')
parser.add_argument('--prof', dest='prof', type=str, help='Profession of the candidate')

args = parser.parse_args()
print(f"Name:        {args.name}")
print(f"Age:         {args.age}")
print(f"Profession:  {args.prof}")