#Modifies code in AST tree by inserting statements.
#Prints the results of the original and modified code.

import ast
import copy

code = \
"""
x=17
y=23
z=101
print( "x = %i; y = %i, z= %i" % (x,y,z))

"""

original = ast.parse(code)
print('Executing original...')
exec(compile(original, filename = "<ast>", mode = "exec"))

#Create a copy of tree
clone = copy.deepcopy(original)

st1 = ast.parse("x = x+1")
st2 = ast.parse("y = y+1")
st3 = ast.parse("z = z+1")

bdy = clone.body

bdy.insert(3, st3.body[0])
bdy.insert(2, st2.body[0])
bdy.insert(1, st1.body[0])

#Execute the modified code. . .
ast.fix_missing_locations(clone)

print('Executing modified...')
exec(compile(clone, filename = "<ast>", mode = "exec"))