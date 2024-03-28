# декоратор класса

def add_new_method(class_to_decorate):
    class DecoratedClass(class_to_decorate):
        def new_method(self):
            return "This is a new method"

    return DecoratedClass


@add_new_method
class MyClass:
    def my_method(self):
        return "This is my method"


my_object = MyClass()
print(my_object.my_method())  # вывод: This is my method
print(my_object.new_method())  # вывод: This is a new method


#################################################


# декоратор-класс

class MyDecorator:
    def __init__(self, function):
        self.function = function
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self.counter += 1
        print(f"Called {self.counter} times")


@MyDecorator
def some_function():
    return 42


some_function()
some_function()
some_function()