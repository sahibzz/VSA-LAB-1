class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Əlavə olundu (əvvəl): {data}")

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Əlavə olundu (son): {data}")
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        print(f"Əlavə olundu (son): {data}")

    # Delete node
    def delete_node(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            print(f"Silindi: {key}")
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
            print(f"Silindi: {key}")

    # Search node
    def search_node(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                print(f"Tapıldı: {key}")
                return True
            curr = curr.next
        print(f"Tapılmadı: {key}")
        return False

    # Reverse list
    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
        print("Siyahı tərsinə çevrildi.")

# Test hissəsi
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.search_node(20)
    ll.delete_node(10)
    ll.reverse_list()
