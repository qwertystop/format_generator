"""
Generator function producing formatted strings from template string and directed-graph pattern.
"""


"""
The MIT License (MIT)

Copyright (c) 2016 David Heyman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def format_generator(template, *args):
    """
    Generate strings according to template by formatting recursively.
    format() fields must be numbered. Other format() syntax not intentionally supported.
    Use of curly braces not intended as format() fields is not supported.

    :param template: Template string to be filled in by format
    :param args: processed as follows
        If empty, yield template, end.
        If 0th element is string, insert into template with format() and recur on rest of list.
        If 0th element is tuple, branch using each element as to_insert[0] in turn.
        If 0th element is list, unpack that list (allows tuples to contain sequences of insertions)
    """



    temp = _clear_fields(template)

    for res in _rec_gen(temp, *args):
        yield res

def _rec_gen(template, *args):
    """
    Defined separately so parsing the fields only needs to happen once
    """
    if not to_insert:
        yield template
    elif isinstance(to_insert[0], basestring):
        gen = format_generator(template.format(to_insert[0]), to_insert[1:])
        for res in gen:
            yield res
    elif isinstance(to_insert[0], tuple):
        for elt in to_insert[0]:
            gen = format_generator(template, [elt]+to_insert[1:])
            for res in gen:
                yield res
    elif isinstance(to_insert[0], list):
        gen = format_generator(template, *to_insert[0]+to_insert[1:])
        for res in gen:
            yield res
    else:
        raise TypeError('Invalid argument to string_generator')

def _clear_fields(template):
    """
    Converts {0}, {1}, {2}, etc to {}, {{}}, {{{{}}}}, etc. to allow recursive formatting.
    """

    import re

    matcher = r'\{(\d+)\}'
    fit = re.finditer(matcher, template)
    res = template
    for inst in fit:
        num = int(inst[1:-1])
        res = res.replace(inst, ('{' * (2**num))+('}' * (2**num)), 1)
    return res
