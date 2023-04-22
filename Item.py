# Item.py
class Item:
    def __init__(self, id, name, width, height):
        self.id = id
        self.name = name
        self.width = width
        self.height = height

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def rotate_item(self):
        temp_width = self.width
        temp_height = self.height
        self.width = temp_height
        self.height = temp_width

    def get_rotated_item(self):
        return Item(self.get_id(), self.get_name(), self.get_height(), self.get_width())