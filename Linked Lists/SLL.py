'''This is a singley linked list construction file. I will construct Linked Lists and make nodes so we can acutally make a linked list
    when we create a new node it does not point to anything, therefore we will call the method set_next to assign the next value'''
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None #we intialize this to none at the beginning beause it is pointing to nothing yet
    
    def __repr__(self):
        return "SLLNode object : data={}".format(self.data)

    def get_data(self):
        #Allows us to access self.data
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Changing the self.data attribute's value by replacing it with the new data parameter"""
        self.data = new_data

    def get_next(self): #this will help us to traverse through the linked list later in the SLL class
        """Return self.next attribute"""
        return self.next

    def set_next(self, new_next): #this is the companion of get_next
        """Replacing the existing value of the self.next attribute with the new_next"""
        self.next = new_next

"""When a node is created we can create an SLL then assign the head to of it to a node created using the class above"""
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __repr__(self):
        return "SLL object : data={}".format(self.data)
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        #Also we can say --> return self.head is None --> this will return a boolean
    
    def add_front(self, new_data):
        temp = SLLNode(new_data)
        temp.set_next(self.head) #By this we are adding to before the head
        self.head = temp #assigning the new node to be the head so we can make sure that the new one is the head
    
    def size(self):
        """"Traverses the linked list and return the number of nodes
                This method is actualy of time complexity O(n) and the memory is O(1)"""
        if self.head == None:
            return 0
        
        count = 0
        temp = self.head
        while temp is not None:
            #I will start traversing the nodes till the next is none
            #If the next is None then break, else we can on increasing the counter by 1 everytime
            temp = temp.get_next()
            count +=1

        return count
    
    def search(self, data):
        """This method traverses the linked list and return True if the one of the nodes matches what we want, else returns False
                The time complexity is O(n), space is O(1)"""
                
        if self.head == None:
            return "Linked List is empty so no nodes to search"
        current = self.head
        while current is not None:
            #handle 2 cases. 
            #case 1: the node data is what we want
            if current.get_data() == data:
                return True
            #case 2: is not what we want
            else:
                current = current.get_next()
        return False

    def remove(self, data):
        """Remove the first occurance of the node that contains data argument as its self.data variable. Return Nothing
                O(n) becuase we might run through the entire list"""
        if self.head is None:
            return "The linked list is empty, no node to remove"
        
        current = self.head #starting from the head of the linked list
        prev = None 
        found = False #boolean for the while loop

        while not found:
            if current.get_data() == data: #we found the value to remove
                found = True #breaks the while loop
            else: #we did not find it
                if current.get_next() == None: #we reached the tail of the linked list
                    return "A node with that data is not present"
                else: #we did not find the node we are looking for but we are not at the end of linked list
                    prev = current #updating prev
                    current = current.get_next() #updating current 
        
        if prev is None: #That means we found the node we are looking for and it is the head of the linked list
            self.head = current.get_next() #Now we need to assign the next value to the head to be the head of the linked list
        else: #We found it and it is not the head of the linked list, could be tail and that is not the issue
            prev.set_next(current.get_next()) #To remove the node we need to remove its connection to the next node in the list and that will make it lost from the Singly linked list