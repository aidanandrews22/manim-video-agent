# CapStyleType

Qualified name: `manim.constants.CapStyleType`

### *class* CapStyleType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: `Enum`

Collection of available cap styles.

See the example below for a visual illustration of the different
cap styles.

### Examples

<div id="capstylevariants" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CapStyleVariants <a class="headerlink" href="#capstylevariants">¶</a></p>![image](media/images/CapStyleVariants-1.png)
```python
from manim import *

class CapStyleVariants(Scene):
    def construct(self):
        arcs = VGroup(*[
            Arc(
                radius=1,
                start_angle=0,
                angle=TAU / 4,
                stroke_width=20,
                color=GREEN,
                cap_style=cap_style,
            )
            for cap_style in CapStyleType
        ])
        arcs.arrange(RIGHT, buff=1)
        self.add(arcs)
        for arc in arcs:
            label = Text(arc.cap_style.name, font_size=24).next_to(arc, DOWN)
            self.add(label)
```

<pre data-manim-binder data-manim-classname="CapStyleVariants">
class CapStyleVariants(Scene):
    def construct(self):
        arcs = VGroup(\*[
            Arc(
                radius=1,
                start_angle=0,
                angle=TAU / 4,
                stroke_width=20,
                color=GREEN,
                cap_style=cap_style,
            )
            for cap_style in CapStyleType
        ])
        arcs.arrange(RIGHT, buff=1)
        self.add(arcs)
        for arc in arcs:
            label = Text(arc.cap_style.name, font_size=24).next_to(arc, DOWN)
            self.add(label)

</pre></div>

### Attributes

| `AUTO`   |    |
|----------|----|
| `ROUND`  |    |
| `BUTT`   |    |
| `SQUARE` |    |
