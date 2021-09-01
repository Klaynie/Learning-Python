# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    keep_going = True
    node = self.get_head_node()
    while keep_going:
      string_list += str(node.get_value()) + "\n"
      node = node.get_next_node()
      if node == None:
        keep_going = False
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      keep_going = True
      while keep_going:
        current_node = current_node.get_next_node() # a -> b
        if current_node.get_value() == None:
          keep_going = False
        elif current_node.get_value() == value_to_remove:
          keep_going = False
          current_next_node = current_node.get_next_node() # b -> c
          current_node.set_next_node(current_next_node)

my_linked_list = LinkedList(5)
my_linked_list.insert_beginning(10)
# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    keep_going = True
    node = self.get_head_node()
    while keep_going:
      string_list += str(node.get_value()) + "\n"
      node = node.get_next_node()
      if node == None:
        keep_going = False
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      keep_going = True
      while keep_going:
        current_node = current_node.get_next_node() # a -> b
        if current_node.get_value() == None:
          keep_going = False
        elif current_node.get_value() == value_to_remove:
          keep_going = False
          current_next_node = current_node.get_next_node() # b -> c
          current_node.set_next_node(current_next_node)

my_linked_list = LinkedList()
# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    keep_going = True
    node = self.get_head_node()
    while keep_going:
      string_list += str(node.get_value()) + "\n"
      node = node.get_next_node()
      if node == None:
        keep_going = False
    return string_list

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      keep_going = True
      while keep_going:
        previous_node = current_node
        current_node = current_node.get_next_node()
        if current_node.get_value() == None:
          keep_going = False
        elif current_node.get_value() == value_to_remove:
          keep_going = False
          current_next_node = current_node.get_next_node()
          previous_node.set_next_node(current_next_node)

my_linked_list = LinkedList(5)
my_linked_list.insert_beginning(10)
my_linked_list.insert_beginning(15)
my_linked_list.insert_beginning(20)
my_linked_list.remove_node(15)
print(my_linked_list.stringify_list())