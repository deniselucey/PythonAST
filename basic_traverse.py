#Prints the type and fields for each node in the AST tree of the given code.

import ast

def basic_traverse(node, depth = 0):
    print(" " * depth, "Node type %s " % node)
    print(" " * depth, "-fields: %s" % str(node._fields))
    children = ast.iter_child_nodes(node)
    for c in children:
        basic_traverse(c, depth + 1)

code = \
"""
def factorial( n ):
   if n <1:   # base case
       return 1
   else:
       return n * factorial( n - 1 )  # recursive call

factorial(4)
"""

root = ast.parse(code)
basic_traverse(root, 0)