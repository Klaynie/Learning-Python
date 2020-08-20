"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""


class Kangaroo(object):
    """Store objects of any type and put it into a pouch
       
    attributes: pouch_contents
    """
    def __init__(self, pouch_contents = None):
            if pouch_contents == None:
                pouch_contents = []
            self.pouch_contents = pouch_contents

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        """return a string representation of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

def print_attributes(obj):
    for attr in obj.__dict__:
        print(attr, getattr(obj, attr))

if __name__ == '__main__':
    kanga = Kangaroo()
    roo = Kangaroo()

    kanga.put_in_pouch('foo')
    kanga.put_in_pouch('bar')

    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)