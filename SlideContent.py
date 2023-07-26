from manim import mobject
from mobject_extra.SlideList import SlideList

class SlideContent :
    def __init__ (self, **kwargs) :
        self.__dict__ = kwargs

    @property
    def all (self) :
        return SlideList(list(self.__dict__.keys()), self.__dict__.values())


