# Ellipse

Qualified name: `manim.mobject.geometry.arc.Ellipse`

### *class* Ellipse(width=2, height=1, \*\*kwargs)

Bases: [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle)

A circular shape; oval, circle.

* **Parameters:**
  * **width** (*float*) – The horizontal width of the ellipse.
  * **height** (*float*) – The vertical height of the ellipse.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle).

### Examples

<div id="ellipseexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: EllipseExample <a class="headerlink" href="#ellipseexample">¶</a></p>![image](media/images/EllipseExample-1.png)
```python
from manim import *

class EllipseExample(Scene):
    def construct(self):
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
        ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
        ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
        self.add(ellipse_group)
```

<pre data-manim-binder data-manim-classname="EllipseExample">
class EllipseExample(Scene):
    def construct(self):
        ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
        ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
        ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
        self.add(ellipse_group)

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

#### \_original_\_init_\_(width=2, height=1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **width** (*float*)
  * **height** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
