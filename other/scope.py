class Difference:
    def __init__(self, a):
        self.__elements = a
	# Add your code here
    def computeDifference (self):
        self.maximumDifference = float('-inf')
        for elt1 in self.__elements:
            for elt2 in self.__elements:
                if elt1 == elt2:
                    pass #fails if all elements are same as everything is passed
                else:
                    diff = abs(elt1 - elt2)
                    if max(diff, self.maximumDifference) == diff:
                    self.maximumDifference = diff
                        
# End of Difference class

_ = 5
a = [8, 8, 8, 8, 8]

d = Difference(a)
d.computeDifference()


print(d.maximumDifference)
