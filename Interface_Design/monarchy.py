class Person:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.children = []


class Monarchy:
    def __init__(self, king):
        self.king = Person(king)
        self._persons = {self.king.name: self.king}

    def birth(self, child_name, parent_name):
        parent = self._persons[parent_name]
        new_child = Person(child_name)
        parent.children.append(new_child)
        self._persons[child_name] = new_child

    def death(self, name):
        person = self._persons.get(name)
        if person is None:
            return
        person.is_alive = False

    def get_order_of_succession(self):
        order = []
        self._dfs(self.king, order)
        return order

    def _dfs(self, current_person, order):
        if current_person.is_alive:
            order.append(current_person.name)
        for child in current_person.children:
            self._dfs(child, order)


if __name__ == "__main__":
    monarchy = Monarchy("King Arthur")
    monarchy.birth("Prince Charles", "King Arthur")
    monarchy.birth("Prince William", "Prince Charles")
    monarchy.birth("Prince Harry", "Prince Charles")
    monarchy.birth("Prince George", "Prince William")

    monarchy.death("Prince Charles")

    order_of_succession = monarchy.get_order_of_succession()
    print(order_of_succession)
