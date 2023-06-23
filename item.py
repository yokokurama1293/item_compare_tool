# item.py

class Item:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    @classmethod
    def from_file(cls, filename, item_name):
        from data_loader import load_item_from_file  # Import here to avoid circular imports
        item_info = load_item_from_file(filename, item_name)
        if item_info is None:
            return None  # Item not found

        name, attributes = item_info
        return cls(name, attributes)

    def compare(self, other):
        from compare_items import compare_items  # Import here to avoid circular imports
        return compare_items(self, other)
