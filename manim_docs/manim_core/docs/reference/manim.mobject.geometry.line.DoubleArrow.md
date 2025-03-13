# DoubleArrow

Qualified name: `manim.mobject.geometry.line.DoubleArrow`

### *class* DoubleArrow(\*args, \*\*kwargs)

Bases: [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)

An arrow with tips on both ends.

* **Parameters:**
  * **args** (*Any*) – Arguments to be passed to [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)

#### SEE ALSO
`ArrowTip`
`CurvedDoubleArrow`

### Examples

<div id="doublearrowexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DoubleArrowExample <a class="headerlink" href="#doublearrowexample">¶</a></p>![image](media/images/DoubleArrowExample-1.png)
```python
from manim import *

from manim.mobject.geometry.tips import ArrowCircleFilledTip
class DoubleArrowExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip, tip_shape_start=ArrowCircleFilledTip)
        group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="DoubleArrowExample">
from manim.mobject.geometry.tips import ArrowCircleFilledTip
class DoubleArrowExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip, tip_shape_start=ArrowCircleFilledTip)
        group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        self.add(group)

</pre></div><div id="doublearrowexample2" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DoubleArrowExample2 <a class="headerlink" href="#doublearrowexample2">¶</a></p>![image](media/images/DoubleArrowExample2-1.png)
```python
from manim import *

class DoubleArrowExample2(Scene):
    def construct(self):
        box = Square()
        p1 = box.get_left()
        p2 = box.get_right()
        d1 = DoubleArrow(p1, p2, buff=0)
        d2 = DoubleArrow(p1, p2, buff=0, tip_length=0.2, color=YELLOW)
        d3 = DoubleArrow(p1, p2, buff=0, tip_length=0.4, color=BLUE)
        Group(d1, d2, d3).arrange(DOWN)
        self.add(box, d1, d2, d3)
```

<pre data-manim-binder data-manim-classname="DoubleArrowExample2">
class DoubleArrowExample2(Scene):
    def construct(self):
        box = Square()
        p1 = box.get_left()
        p2 = box.get_right()
        d1 = DoubleArrow(p1, p2, buff=0)
        d2 = DoubleArrow(p1, p2, buff=0, tip_length=0.2, color=YELLOW)
        d3 = DoubleArrow(p1, p2, buff=0, tip_length=0.4, color=BLUE)
        Group(d1, d2, d3).arrange(DOWN)
        self.add(box, d1, d2, d3)

</pre></div>

### Methods

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(\*args, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **args** (*Any*)
  * **kwargs** (*Any*)
* **Return type:**
  None
