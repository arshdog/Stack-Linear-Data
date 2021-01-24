#-------------------------------------------------------------------------------|
#   Title:                  Pizza Delivery                                      |
#   Assignment:             LIFO/Stacking (linear data)                                  |
#   Class:                  Programming and Methadologies II                    |
#   Author:                 Arshia Amirsolaimani                                |
#-------------------------------------------------------------------------------|

# implementing Stack class

class Stack(object):

    # defining constructor 

    def __init__(self):
        
        #defining list

        self.item = []

    # push method (pushes elements at the last index; returns None)

    def push(self, item):

        self.item.append(item)

    # pop method  (will remove last item; returns none)

    def pop(self):

        self.item.pop()
        pass

    # peek method (lets me see the last element within list)

    def peek(self):

        if self.item:
            return self.item[-1]
        else:
            return None

    # size method ( tells me the size of my stack) 

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None 

    # isempty method (tells whether the the stack is Empty or not; returns Boolean Value)

    def isempty(self):

        if self.item == []:
            return True
        else:
            return False

if __name__ == "__main__":

    # 1st round of doing stuff with data 

    print('\n-------[You Stacked a pepperoni, cheese & meat lovers pizza on top of eachother in that order ]-------')

    stack = Stack()

    stack.push('pepperoni')

    stack.push('cheese')

    stack.push('meat lovers')

    print(f'Size\t', (stack.size()))
    
    print(f'Peek\t', (stack.peek()))

    # 2nd round of doing stuff with data 

    print('\n-------[You deliver the 1st pizza ontop]--------------------------------------------------------------')

    stack.pop()

    print(f'Size\t', (stack.size()))

    print(f'Peek\t', (stack.peek()))

    print(f'Empty?\t',(stack.isempty()))

    # 3rd round of doing stuff with data

    print('\n-------[You deliver the remaining pizzas]------------------------------------------------------------')

    stack.pop()

    stack.pop()

    print(f'Size\t', (stack.size()))

    print(f'Peek\t', (stack.peek()))

    print(f'Empty?\t',stack.isempty())













    


      