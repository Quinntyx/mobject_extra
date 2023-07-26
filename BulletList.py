from manim import *

class BulletList :
    def __init__ (self, *lines) :
        self.group = VGroup()
        for n, i in enumerate(lines):
            self.group.add(Text(i, font_size=24))

        self.group.arrange(DOWN, center=False, aligned_edge=LEFT).shift(2 * LEFT)

    def shift (self, amt) :
        self.group.shift(amt)
        return self

    def __len__ (self) :
        return len(self.group)

def AnimateBulletList (l : BulletList, shift=RIGHT, lag_ratio=0.5) :
    return LaggedStart(*[FadeIn(i, shift=shift) for i in l.group], lag_ratio=lag_ratio)

def DeAnimateBulletList (l : BulletList, shift=LEFT, lag_ratio=0.2, start=0, end=None) :
    if end is None: end = len(l)
    return LaggedStart(*[FadeOut(i, shift=shift) for i in l.group[start:end]], lag_ratio=lag_ratio)



