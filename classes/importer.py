class Importer:
    def __init__(self, id):
        self.id = id
        self.name = self.__name()
        self.imported_products = self.__imported_products()
        self.similar_importers = self.__similar_importers()

    def __name(self):
        return "" #query db using self.id

    def __imported_products(self):
        return [] #query db using self.id

    def __similar_importers(self):
        return [] #query db using self.id
    
    def __repr__(self):
        return self.name

    
