import re

def get_leaf_type(note):
    return 'a' if note[-1].isalpha() else 'n'


def get_parent(note):
    leaf_type = get_leaf_type(note)

    if (leaf_type == 'a'):
        parent = re.search('(.*)[a-z]+', note).groups()[0]
    else:
        if(re.search('^[0-9]+$', note)):
            parent = ""
        else:
            parent = re.search('(.*)[0-9]+', note).groups()[0]

    return parent


def get_siblings(note, notes):

    leaf_type = get_leaf_type(note)
    parent = get_parent(note)

    if (leaf_type == 'a'):
        siblings = [ n for n in notes if re.search(f'^{parent}[a-z]+$', n) ]
    else:
        siblings = [ n for n in notes if re.search(f'^{parent}([0-9]+)$', n) ]
        siblings = [ n[len(parent):] for n in siblings ]
        siblings = sorted([ int(n) for n in siblings ])

    return siblings

def get_next_sibling(note, notes):

    leaf_type = get_leaf_type(note)
    parent = get_parent(note)
    siblings = get_siblings(note, notes)

    if (leaf_type == 'a'):
        last = siblings[-1]
        next_sibling = parent+chr(ord(last[len(parent):])+1)
    else:
        last = siblings[-1]
        next_sibling = parent+str(last+1)

    return next_sibling

def get_children(note, notes):
    leaf_type = get_leaf_type(note)

    if (leaf_type == 'a'):
        children = [ n for n in notes if re.search(f'^{note}[0-9]+$', n) ]
        children = [ n[len(note):] for n in children ]
        children = sorted([ int(n) for n in children ])
        children = [ note+str(n) for n in children ]
    else:
        children = [ n for n in notes if re.search(f'^{note}([a-z]+)$', n) ]

    return children


def get_next_child(note, notes):
    leaf_type = get_leaf_type(note)
    parent = get_parent(note)
    children = get_children(note, notes)

    if (leaf_type == 'a'):
        next_child = get_next_sibling(note+"1", notes)
    else:
        next_child = get_next_sibling(note+"a", notes)

    return next_child
