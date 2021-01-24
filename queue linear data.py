#-------------------------------------------------------------------------------|
#   Title:                  Grocery Line                                        |
#   Assignment:             FIFO/Queue (linear data)                            |
#   Class:                  Programming and Methadologies II                    |
#   Author:                 Arshia Amirsolaimani                                |
#-------------------------------------------------------------------------------|

# implementing Queue Class

class Queue(object):
    def __init__(self):
        
        # defining empty list

        self.item = []
        
    # adding items to the list 

    def enqueue(self,item):
        
        self.item.insert(0,item)
    
    # if list has elements , this uses pop method (removes element)

    def dequeue(self):
        
        if self.item:
            self.item.pop()
        else:
            return None

    # peek method (lets me see the last element within list)

    def peek(self):

        if self.item:
            return self.item[-1]
        else:
            return None

    # isempty method (tells whether the the stack is Empty or not; returns Boolean Value)

    def isempty(self):

        if self.item == []:
            return True
        else:
            return False

    # size method ( tells me the size of my stack) 

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

if __name__ == '__main__':

    queue = Queue()

    # 1st round with Data 

    print('\n-------[Drake, Arshia & Ry Enter the Checkout line In that order]-------')

    queue.enqueue(item = 'drake')

    queue.enqueue(item = 'arshia')

    queue.enqueue(item = 'Ry')

    print(f'Size\t', (queue.size()))

    print(f'Peek\t',(queue.peek()))

    # 2nd round with data

    print('\n-------[Drake Checks Out & Leaves]--------------------------------------')

    queue.dequeue()

    print(f'Size\t\t\t', (queue.size()))

    print(f'Peek\t\t\t',(queue.peek()))

    print(f'Is The Line Empty?\t',(queue.isempty()))

    # 3rd round with data 

    print('\n-------[Arshia and Ry Check Out & Leave in that order]------------------')

    queue.dequeue()

    queue.dequeue()

    print(f'Size\t\t\t', (queue.size()))

    print(f'Peek\t\t\t',(queue.peek()))

    print(f'Is The Line Empty?\t',(queue.isempty()))


