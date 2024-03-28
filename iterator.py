print('Iterating with the “for” loop')

some_primes = [2, 3, 5]
for prime in some_primes:
    print(prime)

elements = [('H', 1.008), ('He', 4.003), ('Li', 6.94)]
for tup in elements:
    symbol, weight = tup
    print(symbol, weight)

for symbol, weight in elements:
    print(symbol, weight)

d = {'H': 1.008, 'He': 4.003, 'Li': 6.94}
for symbol, weight in d.items():
    print(symbol, weight)

print([symbol for symbol, weight in d.items() if weight > 5])
print({symbol for symbol, weight in d.items() if weight > 5})
print({symbol: weight for symbol, weight in d.items() if weight > 5})
print(list(symbol for symbol, weight in d.items() if weight > 5))


print('The pattern: the iterable and its iterator')
it = iter(some_primes)
while True:
    try:
        prime = next(it)
    except StopIteration:
        break
    else:
        print(prime)


print('Implementing an Iterable and Iterator')


class OddNumbers(object):
    """An iterable object."""

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        return OddIterator(self)


class OddIterator(object):
    """An iterator."""

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


numbers = OddNumbers(7)

for n in numbers:
    print(n)

it = iter(OddNumbers(5))
print(next(it))
print(next(it))

print(list(numbers))
print(set(n for n in numbers if n > 4))
