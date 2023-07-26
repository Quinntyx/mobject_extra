from manim import *

class RadialGraph:
    def __init__ (
            self, 
            values : list, 
            labels=None, 
            fill_color=RED,
            color='#555555',
            fill_opacity=.5,
            divisions=10, 
            line_gap=0.25,
            dynamic_divisions=False
        ) :

        if dynamic_divisions:
            distance = divisions * line_gap
            divisions = max(values)
            line_gap = distance / divisions

        assert labels is None or len(values) == len(labels)
        self.values = values
        self.fill_color = fill_color
        self.fill_opacity=fill_opacity
        self.count = len(values)


        self.directions = RegularPolygon(n=self.count).get_vertices()
        display_coords = [i * self.values[n] * line_gap for n, i in enumerate(self.directions)]

        self.lines = VGroup()
        for i in range(divisions):
            self.lines.add(
                RegularPolygon(n=self.count, radius=line_gap * (i + 1), color=color, stroke_width=2)
            )

        self.poly = Polygon(*display_coords, fill_opacity=fill_opacity, fill_color=fill_color, stroke_opacity=0, z_index=5)

        self.labels = VGroup()
        if labels is not None:
            for i, j in zip(labels, self.directions):
                self.labels.add(Text(i, font_size=12).shift(j * (divisions) * line_gap + j * max(line_gap, 0.5)))

        # if labels is not None:
        #     self.labels = 1

        self.point = self.manufacture_point()

        self.master_group = VGroup(
            self.point,
            self.lines,
            self.poly,
            self.labels
        )

    def get_center (self) :
        return self.lines.get_center()

    def manufacture_point (self) :
        return RegularPolygon(self.count, radius=0, fill_color=self.fill_color, fill_opacity=self.fill_opacity, stroke_opacity=0).shift(self.get_center())

    def shift (self, *args, **kwargs) :
        self.master_group.shift(*args, **kwargs)
        return self

    def scale (self, *args, **kwargs) :
        self.master_group.scale(*args, **kwargs)
        return self


def AnimateRadialGraph (display : RadialGraph) :
    return AnimationGroup(
        *[Create(i) for i in display.lines],
        ReplacementTransform(display.point, display.poly),
        *[FadeIn(i, target_position=display.get_center()) for i in display.labels],
        lag_ratio=0.15
    )


def DeAnimateRadialGraph (display : RadialGraph) :
    return AnimationGroup(
        AnimationGroup(
            *[FadeOut(i) for i in display.lines],
            ReplacementTransform(display.poly, display.manufacture_point())
        ),
        *[FadeOut(i, target_position=display.get_center()) for i in display.labels],
        lag_ratio=0.1
    )


