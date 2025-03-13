# RegularPolygon

Qualified name: `manim.mobject.geometry.polygram.RegularPolygon`

### *class* RegularPolygon(n=6, \*\*kwargs)

Bases: [`RegularPolygram`](manim.mobject.geometry.polygram.RegularPolygram.md#manim.mobject.geometry.polygram.RegularPolygram)

An n-sided regular [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon).

* **Parameters:**
  * **n** (*int*) – The number of sides of the [`RegularPolygon`](#manim.mobject.geometry.polygram.RegularPolygon).
  * **kwargs** (*Any*) – Forwarded to the parent constructor.

### Examples

<div id="regularpolygonexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RegularPolygonExample <a class="headerlink" href="#regularpolygonexample">¶</a></p>![image](media/images/RegularPolygonExample-1.png)
```python
from manim import *

class RegularPolygonExample(Scene):
    def construct(self):
        poly_1 = RegularPolygon(n=6)
        poly_2 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN)
        poly_3 = RegularPolygon(n=10, color=RED)

        poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
        self.add(poly_group)
```

<pre data-manim-binder data-manim-classname="RegularPolygonExample">
class RegularPolygonExample(Scene):
    def construct(self):
        poly_1 = RegularPolygon(n=6)
        poly_2 = RegularPolygon(n=6, start_angle=30\*DEGREES, color=GREEN)
        poly_3 = RegularPolygon(n=10, color=RED)

        poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
        self.add(poly_group)

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

#### \_original_\_init_\_(n=6, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **n** (*int*)
  * **kwargs** (*Any*)
* **Return type:**
  None
