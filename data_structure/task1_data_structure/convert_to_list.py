def convert_to_list(linked_list):
    """Convert linked list object to python list
    Take each value from linked list and append it to python list

    :argument linked_list: LinkedList
    :return python list"""
    current = linked_list.head
    python_list = []
    while current:
        python_list.append(current.value)
        current = current.pointer
    return python_list
