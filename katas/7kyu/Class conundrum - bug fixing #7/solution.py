# Class conundrum - Bug Fixing #7
# Oh no! Timmy's List Class has broken! Can you help timmy and fix his class?
# Timmy has a List class he has created, this is used for type strict arrays (which timmy calls Lists).
# When timmy calls the Count property of the list it still remains at 0 when adding items.
# Also it fails when timmy trys to chain the adds e.g.
# ```javascript myList.add(0).add(1) ```
# ```python my_list.add(0).add(1) ```
# ```ruby my_list.add(0).add(1) ```


class List:
    def __init__(self, kind):
        self.kind = kind
        self.items = []
        self.count = 0

    def add(self, item):
        if type(item) != self.kind:  # pylint:disable=unidiomatic-typecheck
            return f'This item is not of type: {self.kind.__name__}'
        self.items.append(item)
        self.count += 1
        return self
