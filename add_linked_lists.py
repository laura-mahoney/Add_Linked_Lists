#add linked lists 
#we will make a node class for the linked lists

"""Given two linked lists, treat them like numbers and add them together.

This should take two linked lists in "reverse-digit" format, sum them up,
and return the head of a new linked list in "reverse-digit" format.

A list is in reverse-digit format if it is each digit as a node, in
least-significant-place-first order. For example, "123", would become
the list 3->2->1.

Let's add 1 + 2::

    >>> l1 = Node(1)
    >>> l2 = Node(2)
    >>> add_linked_lists(l1, l2).as_rev_string()
    '3'

Let's add 123 + 456::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '579'

Let's make sure we carry: 144 + 456:

    >>> l1 = Node(4, Node(4, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '600'

Let's make sure it works with mismatched lengths: 123 + 89::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(9, Node(8))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '212'

"""


class Node(object):
    """ Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """ Represent data for this node and its successsors as a string 

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat them like numbers and add together 

    l1: the head node of a linked list in 'reverse digit' format
    l2: the head node of another 'reverse digit' format

    Returns: head node of linked list in 'reverse digit' format 

    """



#looping over both lists until they don't exist, adding digits together, if done list doesn't have data, 
# 0 is used to caluclate total 

    out_head = out_tail = None
    carried_over_digit = 0
    #white there are items in either list
    while l1 or l2:
        #if there are items in list l1, assign to digit1, or else give it 0 value
        if l1:
            digit_1 = l1.data 
            l1 = l1.next 
        else:
            digit_1 = 0

        #if there are items in list l2, assign to digit2, else give it 0 value
        if l2:
            digit_2 = l2.data
            l2 = l2.next
        else:
            digit_2 = 0

        #adding digits together, carrying over and determine new carry over
        new_digit = digit_1 + digit_2 + carried_over_digit
        carried_over_digit , new_digit = divmod(new_digit, 10)

        #add to the end of the LL
        if not out_head:
            out_head = out_tail = Node(new_digit)

        else:
            out_tail.next = Node(new_digit)
            out_tail = out_tail.next

#if we have any carry left over, add a new place for it
    if carried_over_digit:
        out_tail.next = Node(carried_over_digit)

    return out_head 


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
