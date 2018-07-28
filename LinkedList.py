class HashListNode:
    def __init__(self, key, val = None):
        """
        DO NOT EDIT
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.value = val
        self.key = key
        self.next = None

    def __str__(self):
        '''
        DO NOT EDIT
        String representation of a linked list node

        :return: String representation
        '''
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        '''
        DO NOT EDIT
        Equality operator
        :return: True if equal, false if not
        '''

        if self and other:
            return self.value == other.value and self.next == other.next \
                   and self.key == other.key
        elif not self and not other:
            return True

        return False

class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None
        self.tail = None

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """

        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next
                temp_other = temp_other.next
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True


    # -------------------------------
    # ----- DO NOT MODIFY ABOVE -----
    # ----- MODIFY BELOW ------------
    # -------------------------------


    def __repr__(self):
        """
        Creates a visual representation of a hash table
        :return: The visual representation
        """
        list = ""
        node = self.head
        if node is None:
            return ""
        while node.next is not self.head:
            list += str(node) + " - "
            node = node.next
        list += str(node)
        return list


    __str__ = __repr__


    def append(self, key, value):
        """
        Adds an item to the linked list
        :param key: The key of the node to be added
        :param value: The value of the node to be added
        :return: None
        """
        if self.head is None:
            self.head = HashListNode(key, value)
            self.tail = self.head
        else:
            node = self.find(key)
            if node is not False:
                node.value = value
                return
            else:
                self.tail.next = HashListNode(key, value)
                self.tail = self.tail.next


    def remove(self, key):
        """
        Removes item from the linked list
        :param key: The key of the item to be removed
        :return: None
        """
        if self.head is None:
            return None
        else:
            node = self.head
            prev = None
            while node is not None:
                if node.key == key:
                    if self.head == node:
                        self.head = node.next
                        return None
                    if self.tail == node:
                        self.tail = prev
                        return None
                    else:
                        prev.next = node.next
                        return None
                prev = node
                node = node.next
            return None

    def find(self, key):
        """
        Finds the node with the given key
        :param key: The key of the item being searched for
        :return: The node that was found or False if no node was found
        """
        if self.head is None:
            return False
        else:
            node = self.head
            while node is not None:
                if node.key == key:
                    return node
                node = node.next
        return False
