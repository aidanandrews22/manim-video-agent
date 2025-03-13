# Triangle

Qualified name: `manim.mobject.geometry.polygram.Triangle`

### *class* Triangle(\*\*kwargs)

Bases: [`RegularPolygon`](manim.mobject.geometry.polygram.RegularPolygon.md#manim.mobject.geometry.polygram.RegularPolygon)

An equilateral triangle.

* **Parameters:**
  **kwargs** (*Any*) – Additional arguments to be passed to [`RegularPolygon`](manim.mobject.geometry.polygram.RegularPolygon.md#manim.mobject.geometry.polygram.RegularPolygon)

### Examples

<div id="triangleexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TriangleExample <a class="headerlink" href="#triangleexample">¶</a></p>![image](media/images/TriangleExample-1.png)
```python
from manim import *

class TriangleExample(Scene):
    def construct(self):
        triangle_1 = Triangle()
        triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
        tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        self.add(tri_group)
```

<pre data-manim-binder data-manim-classname="TriangleExample">
class TriangleExample(Scene):
    def construct(self):
        triangle_1 = Triangle()
        triangle_2 = Triangle().scale(2).rotate(60\*DEGREES)
        tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        self.add(tri_group)

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

#### \_original_\_init_\_(\*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **kwargs** (*Any*)
* **Return type:**
  None
