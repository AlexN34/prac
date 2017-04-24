from abc import ABCMeta, abstractmethod
# need above for set up of abstract methods
class Book(metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display():
        pass

#Write MyBook class
# fill in below
#fill in overrides method to formalise things overriding
# check if method name exists in superclass
def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

class MyBook (Book):
    def __init__(self, title, author, price):
        #Book.__init__(self, title, author) #calling Book's init still needs self - magic method
        # super(MyBook, self).__init__(title, author) #alternative way of calling. first arg says whose init method to call - choose Book or MyBook in this case
        super().__init__(title, author) #alternative way of calling. first arg says whose init method to call - choose Book or MyBook in this case - omit arguments = call superclass's (Book) method - same as super(Book, self)
        self.price = price

    @overrides (Book) # not compulsory, normally just define MyBook's display
    def display(self):
        print ("Title: %s\nAuthor: %s\nPrice: %d" \
                % (self.title, self.author, self.price)) #price is int in input



title=input()
author=input()
price=int(input())
# print ("inputs: %s %s %d" % (title, author, price))
new_novel=MyBook(title,author,price)
new_novel.display()
#new_novel2 = Book(title, author) # gives error even though it has an init method -- can't instantiate abstract
