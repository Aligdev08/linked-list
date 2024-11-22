from typing import Any


class LinkedList:
    def __init__(self, linked_list: dict[Any, int]):
        self.linked_list = linked_list
        current_pointer: int = 0

    def __str__(self):  # -> dict[Any: int]:
        return str(self.linked_list)

    def _check_item_in_linkedlist(self, item: Any) -> bool:
        for any_item in self.linked_list.items()[0]:
            if any_item == item:
                return True
        else:
            return False

    def _find_pointer(self, item: Any):
        if any(node.value == item for node in self.linked_list):
            pass # finish here

    def traverse(self, pointer: int) -> Any:
        for node in self.linked_list.items():  # node is tuple
            if node[1] == pointer:
                return node[0]

    def delete(self, item: Any) -> int:  # returns pointer for that item



animal_list = LinkedList({
    "rabbit": 1,
    "dog": 2
})
print(animal_list.traverse(2))
