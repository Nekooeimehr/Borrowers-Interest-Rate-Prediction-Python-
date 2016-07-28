
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("name {} is {}" .format(i, name))

# How many friends contain the letter 'a' ?
count_a = 0
for name in friends:
    if "a" in name:
        count_a += 1

print ("%f percent of the names contain an 'a'" % (count_a/len(friends)*100))


# Say hi to all friends
def print_hi(name, greeting='hello'):
    print ("%s %s" % (greeting, name))

[print_hi(names) for names in friends]

# Print sorted names out
Sorted_Friends = sorted(friends)
print (Sorted_Friends)


'''
    Calculate the factorial N! = N * (N-1) * (N-2) * ...
'''

def factorial(x):
    """
    Calculate factorial of number
    :param N: Number to use
    :return: x!
    """
    if x==1: return 1
    return (x*factorial(x-1))

print ("The value of 5! is", factorial(5))

