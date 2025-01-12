# 1
#class Book():
#    title = 'Книга'
#    author = 'Пушкин'
#    year = 1999

#    @classmethod
#    def get_info(cls):
#        return f"Название: {cls.title}\nАвтор: {cls.author}\nГод: {cls.year}"


#Book.title = 'Name'
#Book.author = 'auvtor'
#Book.year = 34324

#print(Book.get_info())


# 2
class Circle:
    def __init__(self, radius):
        self.radios = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


Obj = Circle(23)
Obj.set_radius(345)
print(Obj.get_radius())