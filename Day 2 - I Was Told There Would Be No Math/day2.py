# --- Day 2: I Was Told There Would Be No Math ---
# The elves are running low on wrapping paper, and so they need to submit an 
# order for more. They have a list of the dimensions (length l, width w, and
# height h) of each present, and only want to order exactly as much as they 
# need.

# Fortunately, every present is a box (a perfect right rectangular prism), 
# which makes calculating the required wrapping paper for each gift a little 
# easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
# The elves also need a little extra paper for each present: the area of the 
# smallest side.

# For example:

# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet 
# 	of wrapping paper plus 6 square feet of slack, for a total of 58 square 
#	feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet
# 	of wrapping paper plus 1 square foot of slack, for a total of 43 square 
#	feet.

# All numbers in the elves' list are in feet. How many total square feet of
# 	wrapping paper should they order?

def computeArea(dim = []):
	
	l = dim[0]
	w = dim[1]
	h = dim[2]
	
	# Compute the area of the box
	area = (2*l*w) + (2*w*h) + (2*h*l)
	
	# Add the slack (smallest side)
	l = min(dim)
	dim.remove(l)
	h = min(dim)
	
	area += l * h
	
	return area

def main():
	sum = 0
	bx = 0
	f = open('input.txt', 'r')
	
	for line in f:
		bx += 1
		line = line.strip('\n')
		line = line.split('x')
		
		for i in range(len(line)):
			line[i] = int(line[i])
		
		sum += computeArea(line)
		print 'Box {}\tSum: {}'.format(bx, sum)
	
	print '\n\n***** The elves need {} sq ft of wrapping paper for {} boxes*****'.format(sum, i)
	
if __name__ == '__main__':
    main()