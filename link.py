#   Doubly Linked List Project File
#   Structure of linked list  ( Null - Node - Node - Node - Null )
#   Push head, Insert at the end of the list, insert after any node, remove, and traversing
#   Created By Baig b0y
#   Thanks to Mustajab xD


class Node:
    def __init__(self, data=None, next_data=None, prev=None):
        self.next = next_data
        self.prev = prev
        self.data = data


class List:
    def __init__(self):
        self.head = None  # Initial condition

    def insert(self, data):  # at the end of the node (Tail)
        insert_data = Node(data)  # insert_data will be new node
        if self.head:  # if there is already head there, it will add value next to add
            temp = self.head  # creating a temp pointer
            while temp.next is not None:  # traversing point till we get to the final node where tail is null
                temp = temp.next  # it will stop  increasing the value of temp
            temp.next = insert_data  # and temp.next will be the desired node insert_data
            insert_data.prev = temp

        else:  # if there is no head, means list is new. this will create a head with previous value none(Null)
            self.head = insert_data
            insert_data.prev = None

    def remove(self, data):
        remove_data = data  # defining the data value to remove_data
        temp = self.head  # creating a temporary pointer
        prev = None  # defining prev = none, not mandatory
        if remove_data == temp.data:  # if the value of data is in head
            self.head = temp.next  # the new head will be the next value which is temp.next

        else:
            while temp:  # if the value exist after head, this while loop will run
                if temp.data == remove_data:  # When value = remove_data, the will loop break
                    break  # When Break, the value from last loop of prev will be previous value of remove_data
                prev = temp  # <----------------
                if temp.next is None:  # if the value is not in the list, it will break the loop otherwise
                    print('Desired value is not in the list')  # without this code, it will show error
                    break
                else:
                    temp = temp.next
            prev.next = temp.next  # <------------ Assigning prev.next which was remove_data to remove_data.next

    def insert_after(self, insert_after, data):
        insert_data = Node(data)  # creating a new node for the given data
        temp = self.head  # creating a new pointer temp
        while temp:  # while temp is not none
            if temp.data == insert_after:  # if pointer value matches insert data value
                temp1 = temp.next  # save temp1 to the next value
                break  # break the loop
            elif temp.next is None:  # if temp.next is none, means its before tail of the list
                break  # break the loop
            else:
                temp = temp.next  # to continue the loop
        if temp.next is None:
            print('the given node is not in the list\n')  # if the given value is not there, loop will end with print
            pass
        else:
            temp.next = insert_data  # temp.next pointer next value to insert data
            insert_data.prev = temp  # insert data previous value to the value of insert_after
            insert_data.next = temp1  # temp 1, which was the next value of temp, will now point to insert_data next
            temp1.prev = insert_data  # temp1.prev value will change to insert_data

    def push_head(self, data):
        insert_data = Node(data)
        temp = self.head  # storing the default pointer to temp
        self.head = insert_data  # creating insert data our new head
        self.head.next = temp  # giving next value of new head to the old head
        temp.prev = self.head  # giving previous value of old head to the new head

    def traverse(self):
        temp = self.head  # creating temporary pointer temp
        a = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n           Linked List             \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        while temp is not None:
            temp1 = temp.prev
            if temp1 is None:
                a = a + 'Current Value:' + str(temp.data) + '  Previous Value:-' + '\n'
            else:
                a = a + 'Current Value:' + str(temp.data) + '  Previous Value:' + str(temp1.data) + '\n'
            temp = temp.next
        a = a + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print(a)


s = List()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)
s.insert(6)
s.insert(7)
s.insert_after(1, 8)
s.push_head(3)
s.traverse()
