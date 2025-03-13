# Polygon

Qualified name: `manim.mobject.geometry.polygram.Polygon`

### *class* Polygon(\*vertices, \*\*kwargs)

Bases: [`Polygram`](manim.mobject.geometry.polygram.Polygram.md#manim.mobject.geometry.polygram.Polygram)

A shape consisting of one closed loop of vertices.

* **Parameters:**
  * **vertices** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The vertices of the [`Polygon`](#manim.mobject.geometry.polygram.Polygon).
  * **kwargs** (*Any*) – Forwarded to the parent constructor.

### Examples

<div id="polygonexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PolygonExample <a class="headerlink" href="#polygonexample">¶</a></p>![image](media/images/PolygonExample-1.png)
```python
from manim import *

class PolygonExample(Scene):
    def construct(self):
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        square_and_triangles = Polygon(*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)
```

<pre data-manim-binder data-manim-classname="PolygonExample">
class PolygonExample(Scene):
    def construct(self):
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        square_and_triangles = Polygon(\*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)

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

#### \_original_\_init_\_(\*vertices, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vertices** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **kwargs** (*Any*)
* **Return type:**
  None
