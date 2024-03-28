from abc import abstractmethod


class State:
    """Base state. This is to share functionality"""

    def __init__(self, radio: 'Radio', stations: list, name: str):
        self.pos = 0
        self.radio = radio
        self.stations = stations
        self.name = name

    @abstractmethod
    def toggle_amfm(self):
        ...

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Scanning... Station is {} {}".format(self.stations[self.pos], self.name))


class AmState(State):
    def __init__(self, radio: 'Radio'):
        super().__init__(radio, ["1250", "1380", "1510"], "AM")

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio: 'Radio'):
        super().__init__(radio, ["81.3", "89.1", "103.9"], "FM")

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio:
    """A radio. It has a scan button, and an AM/FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


def main():
    """
    >>> radio = Radio()
    >>> actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    >>> actions *= 2
    >>> for action in actions:
    ...    action()
    Scanning... Station is 1380 AM
    Scanning... Station is 1510 AM
    Switching to FM
    Scanning... Station is 89.1 FM
    Scanning... Station is 103.9 FM
    Scanning... Station is 81.3 FM
    Scanning... Station is 89.1 FM
    Switching to AM
    Scanning... Station is 1250 AM
    Scanning... Station is 1380 AM
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
