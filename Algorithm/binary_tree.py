class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        # print(self.value)  # процедура обработки 'префиксный'
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию
        print(self.value)  # процедура обработки 'инфиксный'  Сначала рекурсией перебирает левый и воводит
        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию
        # print(self.value)  # процедура обработки 'постфексный'


A_node = BinaryTree('A').insert_left('B').insert_right('C')

node_root = BinaryTree('2 Root').insert_left('7').insert_right('5')
node_7 = node_root.left_child.insert_left('2').insert_right('6')
node_6 = node_7.right_child.insert_left('5').insert_right('11')
node_5 = node_root.right_child.insert_right('9')
node_9 = node_5.right_child.insert_left('4')

node_root.pre_order()
