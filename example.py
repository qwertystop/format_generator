"""
An example of usage of the format_generator
"""
from format_generator import format_generator

namelist = ['Sarah', 'Ellen', 'Frederick', 'Robert the Seventeenth',
            'Mister Plibble', 'Nobody', 'Sparky', 'Bob']

paired = [(n, n[0]) for n in namelist]

gen = format_generator('{0} is a{2} name, and it starts with {1}.',
                       paired, [' good', 'n excellent'])

for sentence in gen:
    print sentence

