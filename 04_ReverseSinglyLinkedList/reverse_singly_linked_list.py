import singly_linked_list as sll

'''
This is a static method that:
input: takes as argument a SLL
output: None
what will happen: reverses SSL
'''


def reverse_singly_linked_list(linked_list: sll.SinglyLinkedList) -> None:
    # First look if list is not empty
    if not linked_list.empty():
        '''
        Need 3 references:
        1. to old head
        2. to new head
        3. to next head
        '''
        old_head = None
        new_head = linked_list.get_head()
        next_head = new_head.n_ref
        while next_head is not None:
            '''
            In loop the following will happen:
            1. the reference of new head will change from next to old head
            2. ref old head points to new head
            3. pointer new_head points to next head
            4. pointer next_head points to next ref of new_head's node
            '''
            new_head.n_ref = old_head
            old_head = new_head
            new_head = next_head
            next_head = new_head.n_ref
        '''
        After loop:
        new_head.n_ref still points to None,
        so let it point to old_head
        finally set linked_list.head to the new_head
        '''
        new_head.n_ref = old_head
        linked_list.head = new_head


if __name__ == "__main__":
    my_sll = sll.SinglyLinkedList()
    for i in range(10):
        my_sll.unshift(i)
    print(my_sll)
    reverse_singly_linked_list(my_sll)
    print(my_sll)
