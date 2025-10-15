from Node import Node

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head

        if self.head is not None:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_begin(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        if self.head is not None:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, target, data):

        if self.head is None:
            print("List is empty.")
            return
        cur = self.head
        for _ in range(self.count_nodes()):
            if cur.data == target:
                new_node = Node(data)
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next
        print(f"Node with value {target} not found.")

    def delete_node(self, key):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        p = None

        if current.data == key:
            if current.next == self.head:
                self.head = None
                return
            
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = current.next
            self.head = current.next
            return

        while current.next != self.head:
            p = current
            current = current.next
            if current.data == key:
                p.next = current.next
                return

        print(f"Node with value {key} not found.")

    def search(self, key):
        if self.head is None:
            return False
        cur = self.head
        while True:
            if cur.data == key:
                return True
            cur = cur.next
            if cur == self.head:
                break
        return False

    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        p = None
        current = self.head
        start = self.head

        while True:
            nxt = current.next
            current.next = p
            p = current
            current = nxt
            if current == start:
                break

        start.next = p
        self.head = p

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        cur = self.head
        r = []
        while True:
            r.append(str(cur.data))
            cur = cur.next
            if cur == self.head:
                break
        print(" -> ".join(r) + " -> (back to head)")

    def count_nodes(self):
        if self.head is None:
            return 0
        count = 0
        cur = self.head
        while True:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def clear(self):
        self.head = None

'''
I TRIED MAKING A NEW  FILE FOR MAIN BUT IT WAS SHOWING A ERROR AGAIN AND AGAIN AND 
EVEN AFTER PUTTING THEM IN SAME FOLDER I WASN'T ABLE TO CALL THE CIRCULARLINKEDLIST

'''
if __name__ == "__main__":

    c1 = CircularLinkedList()

    c1.insert_end(10)
    c1.insert_end(20)
    c1.insert_end(25)
    c1.insert_end(30)
    c1.insert_begin(5)

    print("Circular Linked List:")
    c1.display()

    print("\nDeleting node with value 10...")
    c1.delete_node(10)
    c1.display()

    print("\nSearching for 25:", c1.search(25))
    print("Searching for 100:", c1.search(100))
          
    print("\nReversing the list...")
    c1.reverse()
    c1.display()

    print("\nTotal nodes:", c1.count_nodes())

    print("\nClearing the list...")
    c1.clear()
    c1.display()

