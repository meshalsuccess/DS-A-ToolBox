"""Please, refer to the Singly Linked List file for more detailed comments and how to use the code. Doubly Linked Lists are kind of an extension of Singly Linked Lists"""
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return None if self.data == None else "Return value = {}".format(self.data)
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_next(self, new_next):
        self.next = new_next
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def set_prev(self, new_prev):
        self.prev = new_prev

class DLL:
    def __init__(self):
        self.head = None
    ############

    def __repr__(self):
        return "DLL object : data={}".format(self.data)
    #############
    
    def is_empty(self):
        return self.head is None
    ##############
    
    def size(self):
        if self.head == None:
            return 0
        counter = 0
        current = self.head
        while current is not None:
            counter +=1
            current = current.get_next()
        
        return counter
    
    #########    
    def search(self, data):
        if self.head == None:
            return "Empty Linked list so we cannot search it"
        
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            current = current.get_next()

        return False
    
    def add_front(self, data):
        temp = DLLNode(data)
        temp.set_next(self.head) #By this we are adding to before the head
        
        if self.head is not None: #we need to check if the linked list is not empty
            self.head.set_prev(temp)

        self.head = temp #assigning the new node to be the head so we can make sure that the new one is the head
    
    def remove(self, data):
        if self.head == None:
            return "Empty no need to remove"
        
        current = self.head
        found = False
        previoud = None
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A node with that data value is not present"
                else:
                    current = current.get_next()
        
        if current.prev is None:
            self.head = current.get_next()
        else:
            current.prev.set_next(current.get_next())
            current.next.set_prev(current.get_prev())
        