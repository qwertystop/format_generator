# format_generator
Generator function producing formatted strings from template according to a directed-graph structure

Call as follows:
format_generator(template, \*args)

Template can be any string ready for format(), but fields can only be numbered
and otherwise unlabeled: {0}, {1}, etc.

\*args is structured as follows:
Any number of elements, where an element is one of:
- A string
- A list of elements
- A tuple of elements

Interpretation:
args = ('A', 'B', ['C', 'D'] [('E', 'F'), ('G', 'H')])
parses to the structure:

  'A'
   |
  'B'
   ^
  / \
'C' 'D'
   v
   ^
  / \
'E' 'G'
 |   |
'F' 'H'

Which, for template string "{0} {1} {2} {3} {4}", sequentially generates the strings:
"A B C E F"
"A B C G H"
"A B D E F"
"A B D G H"
