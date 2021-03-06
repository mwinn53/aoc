# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and
# then an elf at the North Pole calls him via radio and tells him where to move
# next. Moves are always exactly one house to the north (^), south (v),
# east (>), or west (<). After each move, he delivers another present to the
# house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and
# so his directions are a little off, and Santa ends up visiting some houses
# more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the
#	east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house
#	at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only
#	2 houses.

def main():

    f = open('input.txt', 'r')
    pos = [0, 0]    # x, y coordinates in a 2-dimensional grid
    map = {}
    i = 0

    string = f.read()

    for char in string:
        i += 1

        if char == '^':
            pos[0]+=1
        elif char == 'v':
            pos[0]-=1
        elif char == '<':
            pos[1]-=1
        elif char == '>':
            pos[1]+=1

        house = str(pos[0]) + ',' + str(pos[1]) # Can't store a list as a dictionary key, so convert it to a string

        if map.has_key(house):
            map[house] += 1
        else:
            map[house] = 1

        # print 'Step {}: {} \t House {} : Count {}'.format(i, pos, house, map[house]) # Debugging output

    # print map.items() # Debugging output
    print 'There were {} houses that received at least one present'.format(len(map))

if __name__ == '__main__':
    main()