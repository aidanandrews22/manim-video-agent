# RoundedRectangle

Qualified name: `manim.mobject.geometry.polygram.RoundedRectangle`

### *class* RoundedRectangle(corner_radius=0.5, \*\*kwargs)

Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle)

A rectangle with rounded corners.

* **Parameters:**
  * **corner_radius** (*float* *|* *list* *[**float* *]*) – The curvature of the corners of the rectangle.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle)

### Examples

<div id="roundedrectangleexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RoundedRectangleExample <a class="headerlink" href="#roundedrectangleexample">¶</a></p>![image](media/images/RoundedRectangleExample-1.png)
```python
from manim import *

class RoundedRectangleExample(Scene):
    def construct(self):
        rect_1 = RoundedRectangle(corner_radius=0.5)
        rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)

        rect_group = Group(rect_1, rect_2).arrange(buff=1)
        self.add(rect_group)
```

<pre data-manim-binder data-manim-classname="RoundedRectangleExample">
class RoundedRectangleExample(Scene):
    def construct(self):
        rect_1 = RoundedRectangle(corner_radius=0.5)
        rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)

        rect_group = Group(rect_1, rect_2).arrange(buff=1)
        self.add(rect_group)

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

#### \_original_\_init_\_(corner_radius=0.5, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **corner_radius** (*float* *|* *list* *[**float* *]*)
  * **kwargs** (*Any*)
