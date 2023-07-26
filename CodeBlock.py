from pygments import highlight, lexers, formatters
from manim import *

class CodeBlock:
    def __init__ (self, code, language="cpp", fill="#252733", highlight_fill="#34363f", highlight_border=None, width=10, height=6, style="material", padding=1, radius=0.25):
        self.lexer = getattr(lexers, f"{language.capitalize()}Lexer")()
        self.language = language
        self.formatter = getattr(formatters, "PangoMarkupFormatter")(style=style)
        self.code = code
        self.fill = fill
        self.highlight_fill = highlight_fill
        self.highlight_border = highlight_border
        self.width = width
        self.height = height
        self.style = style
        self.padding = padding
        self.radius = radius
        self.line_chars = [len(i.replace(' ', '')) for i in self.code.splitlines()]

        markup = MarkupText(highlight(self.code, self.lexer, self.formatter), line_spacing=-1.25, z_index=5)
        backdrop = BackgroundRectangle(markup, buff=self.padding, fill_opacity=1, fill_color=self.fill, corner_radius=self.radius, z_index=0)

        self.mobject = VGroup(backdrop, markup)

        oldwidth = self.mobject.get_width()
        oldheight = self.mobject.get_height()

        self.mobject.scale_to_fit_width(self.width)
        self.scale_factor = self.mobject.get_width() / oldwidth
        if self.mobject.height > self.height:
            self.mobject.scale_to_fit_height(self.height)
            self.scale_factor = self.mobject.get_height() / oldheight

    def _line_to_char (self, line_number) :
        return sum(self.line_chars[:line_number])

    def highlight (self, startln : int, endln : int) :
        startchr = self._line_to_char(startln)
        endchr = self._line_to_char(endln)

        chars = self.mobject[-1]

        base_rect = BackgroundRectangle(
            chars[startchr:endchr]
        )

        highlight_rect = RoundedRectangle(
            fill_opacity=0.5,
            fill_color=self.highlight_fill,
            corner_radius=self.radius / 2,
            height=base_rect.height + 0.25 * self.scale_factor,
            width=base_rect.width + self.padding * self.scale_factor,
            stroke_opacity=0,
            stroke_width=0,
            z_index=1
        ).move_to([base_rect.get_x(), base_rect.get_y(), 0])

        if self.highlight_border is not None:
            highlight_rect.stroke = self.highlight_border
            highlight_rect.stroke_opacity = 1
            highlight_rect.stroke_width = 1

        self.mobject.insert(1, highlight_rect)
        
        return highlight_rect

    def highlight_lines (self, *lines) :
        out = []
        for line in lines:
            out.append(self.highlight(line, line + 1))

        return out

    def shift (self, dir_vector) : 
        self.mobject.shift(dir_vector)
        return self

    def scale (self, factor) :
        self.scale_factor *= factor
        self.mobject.scale(factor)
        return self




