"""

​Write a Binary Search Tree (BST) class. The class should have a "value" property set to be an integer, as well as "left" and "right" properties, both of which should point to either the None (null) value or to another BST. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. The BST class should support insertion, searching, and removal of values. The removal method should only remove the first instance of the target value.

Sample input:
            10
          /       \
        5         15
      /  \\     /   \\
    2      5  13     22
  /             \\
1                14


Sample output (after inserting 12):
             10
          /       \
        5         15
      /   \\     /   \\
    2      5   13     22
  /             / \\
1             12    14


Sample output (after removing 10):
            12
          /     \
​        5         15
      /   \\     /   \
    2      5   13     22
  /               \
1                  14
Sample output (after searching for 15): True
"""


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		curNode = self
		while curNode != None:
			    parentNode = curNode
                if curNode.value <= value:
				    	curNode = curNode.right
						#to check if node is left or right child
						left= False
				elif curNode.value > value:
					    curNode = curNode.left
						left = True
				if curNode == None:
						if left != True:
					        parentNode.right = BST(value)
						else:    
			                parentNode.left  =  BST(value)
						break
        return self

    def contains(self, value):
        # Write your code here.
        curNode = self
		while curNode != None:
			if curNode.value < value :
				  curNode = curNode.right
			elif curNode.value > value:
				  curNode = curNode.left
			else:
				  return True
		return False
			

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        curNode = self
		while curNode != None:
				if curNode.value > value:
					    curNode = curNode.left
				elif curNode.value <= value:
					    curNode = curNode.right
				if curNode == None:
					    break
				if curNode.value == value:
					    #case when node to be deleted is leaf node
						if curNode.left == None and curNode.right == None:
							    curNode = None
								
						#case when right subtree doesnt exist
						elif curNode.right == None :
							    parentNode = curNode
							    curNode  = curNode.left
							    while curNode.right!= None:
									   curNode = curNode.right
								parentNode.value = curNode.value
								curNode.remove(curNode.value)
					    #all other cases   
						else:
								parentNode = curNode
							    curNode  = curNode.right
							    while curNode.left!= None:
									   curNode = curNode.left
								parentNode.value = curNode.value
								curNode.remove(curNode.value)
					
			
		return self
