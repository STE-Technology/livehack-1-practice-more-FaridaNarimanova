"""
Given the ages of the youngest and middle children,
 what is the age of the oldest child?
 
"""
# Ask user for ages of youngest and middle child.

young_child = int(input("How old is young child?: "))
middle_child = int(input("How old is middle child: "))

# Subtract to find differences, and add them to age of middle child

difference = (middle_child - young_child)

oldest_child = difference + middle_child

print(oldest_child)




      