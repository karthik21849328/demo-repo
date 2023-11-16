#CREATING NODE

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

# CREATING AN EMPTY LINKED LIST
class linkedlist:
    def __init__(self):
        self.head=None  
    def printll(self):    #printing the elements in the linkedlist and also called as traversin the linked list 
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_begin(self,data):            #function to add node in the beginig of the linked list
        new_node=Node(data)   #creating a new node
        new_node.ref=self.head  #we are adding ref to newly created node by assigning the value of head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)   #creating a new node to add at the end of ll
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("Element not found in the list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node 

    # deleting the node in the begining of the linked list
    def del_begin(self):
        if self.head == None:
            print("linked list is empty")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head==None:                           #if my linked list is empty
            print("linked list is empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not  None:
                n=n.ref
            n.ref=None

    def delete_node(self,ele):
        if self.head==None:
            print("linked list is empty")
        elif ele==self.head.data:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==ele:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found in the linked list")
            else:
                n.ref=n.ref.ref

    def reversell(self):
        prev,curr=None,self.head
        while curr!=None:
            temp=curr.ref
            #lets change the pointer 
            curr.ref=prev
            #lets swap the pointers
            prev=curr
            curr=temp
        self.head=prev

    def find_max(self):
        n=self.head
        key=n.data
        while n.ref is not None:
            if n.data >= key:
                key=n.data
            n=n.ref
        return key

     

    
            


ll1=linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_begin(40)
max=ll1.find_max()
print(f"max element in the linked lsit is {max}")
#ll1.printll()
#ll1.reversell()  

ll1.printll() 