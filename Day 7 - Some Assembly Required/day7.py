# -- Day 7: Some Assembly Required ---
# 
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic
# gates! Unfortunately, little Bobby is a little under the recommended age
# range, and he needs help assembling the circuit.
# 
# Each wire has an identifier (some lowercase letters) and can carry a
# 16-bit signal (a number from 0 to 65535). A signal is provided to each wire
# by a gate, another wire, or some specific value. Each wire can only get a
# signal from one source, but can provide its signal to multiple destinations.
# A gate provides no signal until all of its inputs have a signal.
# 
# The included instructions booklet describes how to connect the parts
# together: x AND y -> z means to connect wires x and y to an AND gate, and
# then connect its output to wire z.
# 
# For example:
# 
#     123 -> x means that the signal 123 is provided to wire x.
#     x AND y -> z means that the bitwise AND of wire x and wire y is provided
#         to wire z.
#     p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2
#         and then provided to wire q.
#     NOT e -> f means that the bitwise complement of the value from wire e
#         is provided to wire f.
# 
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
#     If, for some reason, you'd like to emulate the circuit instead, almost
#     all programming languages (for example, C, JavaScript, or Python)
#     provide operators for these gates.
# 
# For example, here is a simple circuit:
# 
#   123 -> x
#   456 -> y
#   x AND y -> d
#   x OR y -> e
#   x LSHIFT 2 -> f
#   y RSHIFT 2 -> g
#   NOT x -> h
#   NOT y -> i
# 
# After it is run, these are the signals on the wires:
# 
#   d: 72
#   e: 507
#   f: 492
#   g: 114
#   h: 65412
#   i: 65079
#   x: 123
#   y: 456
# 
# In little Bobby's kit's instructions booklet (provided as your puzzle input),
# what signal is ultimately provided to wire a?

import re



#############################################################################
def parseFile(fname):

    cmdList = []
    
    f = open(fname, 'r')
    
    for line in f:
        # op, operand1, operand2, dest
        op = None
        operand1 = None
        operand2 = None
        dest = None
        
        string = line.split(' -> ')

        dest = string[1].strip('\n')

        string = string[0].split(' ')

        if len(string) == 1:  # STORE Operation (e.g. 123 -> a)
            op = 'sto'
            operand1 = typecast(string[0])

        elif len(string) == 2: # NOT Operation (e.g. NOT 123 -> a)
            op = 'not'
            operand1 = typecast(string[1])

        elif len(string) == 3: # Binary operation (e.g. 123 AND 456 -> a)
            if string[1] == 'AND':
                op = 'and'
                
            elif string[1] == 'OR':
                op = 'or'
        
            elif string[1] == 'LSHIFT':
                op = 'lsh'

            elif string[1] == 'RSHIFT':
                op = 'rsh'

            operand1 = typecast(string[0])
            operand2 = typecast(string[2])

        listItem = [op, operand1, operand2, dest]

        cmdList.append(listItem)

    return cmdList
#############################################################################
def typecast(value):
    if not(re.search('[a-z]{1,2}',value)):
        return int(value)
    else:
        return str(value)
    
    
#############################################################################
def recurList(circuit, result):
    # find result in circuit
    for row in circuit:
        if row[3] == result:
           print 'FOUND: {}\t(Row {})'.format(row, circuit.index(row))            
           circuit.remove(row)

        # Recur if operand1 is not a value
           lookup = dictionary.get(row[1]) 
           if lookup:
               op1 = lookup
               print '\t OP1 -- FOUND {} : {} in dictionary...'.format(row[1], lookup)

           elif isinstance(row[1], str):
               print '\t RECURRING on OP1: {}...'.format(row[1])
               op1 = recurList(circuit, row[1])

           else:
               print '\t USING {} for OP1...'.format(row[1])
               op1 = row[1]

        # Recur if operand2 (if required) is not a value 
           if row[2] != None:
               lookup = dictionary.get(row[2]) 
               if lookup:
                   op2 = lookup
                   print '\t OP2 -- FOUND {} : {} in dictionary...'.format(row[2], lookup)

               elif (isinstance(row[2], str)):
                   print '\t RECURRING on OP2: {}...'.format(row[2])
                   op2 = recurList(circuit, row[2])
               else:
                   print '\t USING {} for OP2...'.format(row[2])
                   op2 = row[2]
           else:
               op2 = None
                   
        # Base case: result can be evaluated
           result = evaluate([row[0], op1, op2])
           print '\t EVALUATED {} {} {} -> {}'.format(row[0], op1, op2, result)

           dictionary[row[3]] = result
           # print '\t DICTIONARY {}'.format(dictionary)
           return result

#############################################################################    
def evaluate(line):

    op = line[0]
    operand1 = line[1]
    operand2 = line[2]

    ## print '\t\tEvaluating {}...'.format(line)

    if op == 'sto':
        return operand1

    elif op == 'and':
        result = operand1 & operand2

    elif op == 'or':
        result = operand1 | operand2

    elif op == 'not':
        result = ~ operand1

    elif op == 'lsh':
        result = (operand1 << operand2) & 0xFFFF # Drop the overflow

    elif op == 'rsh':
        result = operand1 >> operand2

    ## print '\t\tOP: {}\tRES: {}'.format(op, result)
    return result

#############################################################################
def main():

    file = 'input.txt'
    circuit = parseFile(file)
    result = 'a'
    global dictionary

    dictionary = {}

    recurList(circuit, result)

if __name__ == '__main__':
    main()
