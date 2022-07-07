#!/usr/bin/python

import sys
import os
import subprocess

import folgezettel

folder = sys.argv[1]
current_note = sys.argv[2].replace('.md', '')

notes = sorted(subprocess
    .run(['zk', 'list', '--quiet', '--format', 'path', '--delimiter', '|'], stdout=subprocess.PIPE)
    .stdout
    .decode("utf-8")
    .strip()
    .split('|')
)

notes = [ n.replace('.md', '') for n in notes ]

next_sibling = folgezettel.get_next_sibling(current_note, notes)

print(next_sibling)
