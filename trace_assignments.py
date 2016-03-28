#Inserts a print statement after every assignment
#in subtree rooted at node

import ast

def traverse( node, parent ) :
    if (isinstance( node, ast.Assign )):
        #Extract variable name (assume one var. on LHS)
        var_name = node.targets[0].id

        #Find node's child number wrt parent
        indx = parent.body.index(node)

        #Create appropriate print statement
        print_stmt_text = \
            "print('%s <-', %s)" \
            % (var_name, var_name)
        print_stmt_tree = \
            ast.parse(print_stmt_text).body[0]

        #Graft print 'statement' immediately after assignment
        parent.body.insert(indx+1, print_stmt_tree)

        #Recurse
        children = ast.iter_child_nodes(node)
        for c in children:
            traverse( c, node )

code = \
"""
LIMIT = 20
PERLINE = 10

numPrimes = 0

for n in range(2, LIMIT+1):
    possiblePrime = True

    #set possiblePrime to false if n composite
    for c in range(2, n):
        if n % c == 0:
            possiblePrime = False
            break

    #print n if prime, linebreak every 10th prime
    if possiblePrime:
        print("%i is a prime number" % n)
        numPrimes = numPrimes + 1
        if numPrimes % PERLINE == 0:
            print ("")
"""

#Generate the AST
root = ast.parse(code)

#Traverse tree and modify
traverse(root, root)

#Repair line and column numbers
ast.fix_missing_locations(root)

#Execute "fixed" code
exec(compile(root, filename="<ast>", mode="exec"))