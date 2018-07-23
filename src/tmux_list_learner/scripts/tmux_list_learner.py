#!/usr/bin/env python

import click
import sys
import random
from collections import OrderedDict

window_names = OrderedDict([
    ('fates-graces', ['Atropos', 'Clotho', 'Lachesis', 'Aglaea', 'Euphrosyne', 'Thalia', 'F/G']),
    ('muses', ['Calliope', 'Clio', 'Erato', 'Euterpe', 'Melpomene', 'Terpsichore', 'Thalia', 'Polyhymnia', 'Urania', 'M']),
    ('wisdoms', ['Nous', 'Sophia', 'Techne', 'Episteme', 'Phronesis', 'W']),
    ('humors', ['Choleric', 'Melancholic', 'Sanguine', 'Phlegmatic', 'H']),
    ('sins', ['Avarice', 'Wrath', 'Lust', 'Envy', 'Greed', 'Sloth', 'Pride', 'S']),
    ('network-top', ['Application', 'Presentation', 'Session', 'Transport', 'Network', 'Data-Link', 'Physical'])
])
window_names['network-bottom'] = list(window_names['network-top'])
window_names['network-bottom'].reverse()

@click.command()
@click.argument('server_start')
@click.argument('session_name')
@click.argument('window_index', type=int)
def cli(server_start, session_name, window_index):
    if session_name[-1].isdigit() and int(session_name[-1]) < len(window_names) - 1:
        n = int(session_name[-1])
    else:
        n = random.randint(0, len(window_names) - 1)

    random.seed(server_start)

    keys = list(window_names.keys())
    random.shuffle(keys)
    key = keys[n]

    window_name = window_names[key][min(window_index, len(window_names[key]) - 1)]

    print(window_name)
