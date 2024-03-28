class Singleton(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()
print(a)
print(b)

print(a is b)

a.field = 123
print(b.field)
