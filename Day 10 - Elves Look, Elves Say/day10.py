# --- Day 10: Elves Look, Elves Say ---
#
# Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the
# previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones",
# which becomes 1221 (1 2, 2 1s).
#
# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each
# step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed
# by the digit itself (1).
#
# For example:
#
#     1 becomes 11 (1 copy of digit 1).
#     11 becomes 21 (2 copies of digit 1).
#     21 becomes 1211 (one 2 followed by one 1).
#     1211 becomes 111221 (one 1, one 2, and two 1s).
#     111221 becomes 312211 (three 1s, two 2s, and one 1).
#
# Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?
#
# Your puzzle input is 1113222113.
#
# --- Part Two ---
#
# Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game
# of Life fame).
#
# Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of
# the new result?




#############################################################################

def lookandsay(line):

    newline = ''
    count = 0

    # print('\tProcessing :   {}').format(line)

    for i in range(0, len(line)):

        if i == 0:
            continue

        if line[i-1] == line[i]:
            count += 1
        else:
            count += 1
            newline = newline + str(count)+line[i-1]
            count = 0

 #       print('Round {}:\t{}').format(i, newline)

    if line[i-1] == line[i]:
        count += 1
        newline = newline + str(count)+line[i]
    else:
        count = 1
        newline = newline + str(count)+line[i]

    # print('\tExiting :      {} ({})').format(newline, len(newline))


    return newline

def main():

    input = '1113222113'

    for i in range(0, 50):
        input = lookandsay(input)
        print('Round {}:\t{}').format(i, len(input))


    print('Result:\t{} ({})').format(input, len(input))

if __name__ == '__main__':
    main()
