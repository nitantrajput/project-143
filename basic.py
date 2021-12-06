import itertools

# any is predeined function 
# The any() function returns True if any item in an iterable are true, otherwise it returns False.

mylist=[True,False,False]

mytuple = (0, 1, False)
empty=[]
print(any(empty))













# Syntax: itertools.count(start=0, step=1)

# Parameters:
# start: Start of the sequence (defaults to 0)
# step: Difference between consecutive numbers (defaults to 1)
# Returns: Returns a count object whose .__next__() method returns consecutive values.

# for i in itertools.count(0,5):
#     if i == 50:
#         break
#     else:
#         print(i, end="")


# a=[2,2,3,4,5,6,6,5,3,3]
# x=itertools.groupby(a)
# for i,j in x:
#    print(list(j))
