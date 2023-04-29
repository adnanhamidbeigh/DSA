class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        if position == 1:
            return self.head

        current = self.head
        count = 1
        while current:
            if position == count:
               return current
            else:
                count += 1
                current = current.next

    def insert(self, new_element, position):
        if position == 1:
            # current = self.head
            # # self.head = new_element
            # new_element.next = current
            # current = new_element
            new_element.next = self.head
            self.head = new_element
        else:
            count = 2
            current = self.head
            while current:
                if position == count:
                    new_element.next = current.next
                    current.next = new_element
                    break
                current = current.next
                count += 1

    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next


# Elements:
element1 = Element(124)
element2 = Element(224)
element3 = Element(332)
element4 = Element(424)

ll = LinkedList(element1)

ll.append(element2)
ll.append(element3)
ll.append(element4)

print(f"Value of Element 1: {ll.get_position(1).value}")
print(f"Value of Element 2: {ll.get_position(2).value}")
print(f"Value of Element 3: {ll.get_position(3).value}")
print(f"Value of Element 4: {ll.get_position(4).value}")

# Insert at beginning:
# new_element = Element(300)
# ll.insert(new_element, 1)
#
# print(f"Value of New Element 1: {ll.get_position(1).value}")
# print(f"Value of New Element 2: {ll.get_position(2).value}")
# print(f"Value of New Element 3: {ll.get_position(3).value}")
# print(f"Value of New Element 4: {ll.get_position(4).value}")
# print(f"Value of New Element 5: {ll.get_position(5).value}")

# Insert at middle
# n_element = Element(300)
# ll.insert(n_element, 2)
# print(f"Value of New Element 1: {ll.get_position(1).value}")
# print(f"Value of New Element 2: {ll.get_position(2).value}")
# print(f"Value of New Element 3: {ll.get_position(3).value}")
# print(f"Value of New Element 4: {ll.get_position(4).value}")
# print(f"Value of New Element 5: {ll.get_position(5).value}")

# Insert at end
# n_element = Element(300)
# ll.insert(n_element, 5)
#
# print(f"Value of New Element 1: {ll.get_position(1).value}")
# print(f"Value of New Element 2: {ll.get_position(2).value}")
# print(f"Value of New Element 3: {ll.get_position(3).value}")
# print(f"Value of New Element 4: {ll.get_position(4).value}")
# print(f"Value of New Element 5: {ll.get_position(5).value}")

# Deletion
# Delete at beginning
# ll.delete(element1.value)
# print(f"Value of New Element 1: {ll.get_position(1).value}")
# print(f"Value of New Element 2: {ll.get_position(2).value}")
# print(f"Value of New Element 3: {ll.get_position(3).value}")

# Delete at middle
# ll.delete(element3.value)
# print(f"Value of New Element 1: {ll.get_position(1).value}")
# print(f"Value of New Element 2: {ll.get_position(2).value}")
# print(f"Value of New Element 3: {ll.get_position(3).value}")

# Delete at end
ll.delete(element4.value)
print(f"Value of New Element 1: {ll.get_position(1).value}")
print(f"Value of New Element 2: {ll.get_position(2).value}")
print(f"Value of New Element 3: {ll.get_position(3).value}")
print(f"Element 4: {ll.get_position(4)}")

