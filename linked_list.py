class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    def get_head_node(self):
        return self.head
    
    def get_lenght(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def middle_node(self):
        current_node = self.head
        middle_node = self.get_lenght() // 2
        while middle_node > 0:
            current_node = current_node.get_next()
            middle_node -= 1
        return current_node.get_data()
    


node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")
node_i = Node("I")
node_j = Node("J")
node_k = Node("K")
node_l = Node("L")
node_m = Node("M")
node_n = Node("N")
node_o = Node("O")

linked_list = LinkedList(node_a)

node_a.set_next(new_next=node_b)
node_b.set_next(new_next=node_c)
node_c.set_next(new_next=node_d)
node_d.set_next(new_next=node_e)
node_e.set_next(new_next=node_f)
node_f.set_next(new_next=node_g)
node_g.set_next(new_next=node_h)
node_h.set_next(new_next=node_i)
node_i.set_next(new_next=node_j)
node_j.set_next(new_next=node_k)
node_k.set_next(new_next=node_l)
node_l.set_next(new_next=node_m)
node_m.set_next(new_next=node_n)
node_n.set_next(new_next=node_o)
node_o.set_next(new_next=None)

print(linked_list.middle_node())