from abc import ABC, abstractmethod


class PngInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class PngImage(PngInterface):
    def __init__(self, png):
        self.png = png
        self.format = "raster"

    def draw(self):
        # сложная реализация вывода картинки формата png на экран
        print("drawing " + self.get_image())

    def get_image(self):
        return "png"

#########################################################


class SvgImage:
    """
    Библиотека для работы с векторной графикой, но она не соответствует интерфейсу с методом draw
    """
    def __init__(self, svg):
        self.svg = svg
        self.format = "vector"

    def get_image(self):
        return "svg"

###########################################################


class SvgAdapter(PngInterface):
    """
    Адаптер объекта
    обертывает внешний (служебный) класс, предлагая интерфейс, соответствующий нашему собственному (клиентскому) классу.
    """
    def __init__(self, svg):
        self.svg = svg

    def rasterize(self):
        return "rasterized " + self.svg.get_image()

    def draw(self):
        img = self.rasterize()
        print("drawing " + img)


regular_png = PngImage("some data")
regular_png.draw()

example_svg = SvgImage("some data")
example_adapter = SvgAdapter(example_svg)
example_adapter.draw()


############################################################


class ConvertingNonVector(Exception):
    pass


class ClassAdapter(PngImage, SvgImage):
    """
    Адаптер класса наследует как наш класс, так и внешний класс, тем самым наследуя все их функции.
    """
    def __init__(self, image):
        self.image = image

    def rasterize(self):
        if self.image.format == "vector":
            return "rasterized " + self.image.get_image()
        else:
            raise ConvertingNonVector

    def draw(self):
        try:
            img = self.rasterize()
            print("drawing " + img)
        except ConvertingNonVector as e:
            print("drawing " + self.image.get_image())


example_png = PngImage("some data")
regular_png = ClassAdapter(example_png)
regular_png.draw()

example_svg = SvgImage("some data")
example_adapter = ClassAdapter(example_svg)
example_adapter.draw()
