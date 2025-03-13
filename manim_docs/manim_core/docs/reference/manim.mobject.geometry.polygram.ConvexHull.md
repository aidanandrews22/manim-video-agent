# ConvexHull

Qualified name: `manim.mobject.geometry.polygram.ConvexHull`

### *class* ConvexHull(\*points, tolerance=1e-05, \*\*kwargs)

Bases: [`Polygram`](manim.mobject.geometry.polygram.Polygram.md#manim.mobject.geometry.polygram.Polygram)

Constructs a convex hull for a set of points in no particular order.

* **Parameters:**
  * **points** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The points to consider.
  * **tolerance** (*float*) – The tolerance used by quickhull.
  * **kwargs** (*Any*) – Forwarded to the parent constructor.

### Examples

<div id="convexhullexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ConvexHullExample <a class="headerlink" href="#convexhullexample">¶</a></p>![image](media/images/ConvexHullExample-1.png)
```python
from manim import *

class ConvexHullExample(Scene):
    def construct(self):
        points = [
            [-2.35, -2.25, 0],
            [1.65, -2.25, 0],
            [2.65, -0.25, 0],
            [1.65, 1.75, 0],
            [-0.35, 2.75, 0],
            [-2.35, 0.75, 0],
            [-0.35, -1.25, 0],
            [0.65, -0.25, 0],
            [-1.35, 0.25, 0],
            [0.15, 0.75, 0]
        ]
        hull = ConvexHull(*points, color=BLUE)
        dots = VGroup(*[Dot(point) for point in points])
        self.add(hull)
        self.add(dots)
```

<pre data-manim-binder data-manim-classname="ConvexHullExample">
class ConvexHullExample(Scene):
    def construct(self):
        points = [
            [-2.35, -2.25, 0],
            [1.65, -2.25, 0],
            [2.65, -0.25, 0],
            [1.65, 1.75, 0],
            [-0.35, 2.75, 0],
            [-2.35, 0.75, 0],
            [-0.35, -1.25, 0],
            [0.65, -0.25, 0],
            [-1.35, 0.25, 0],
            [0.15, 0.75, 0]
        ]
        hull = ConvexHull(\*points, color=BLUE)
        dots = VGroup(\*[Dot(point) for point in points])
        self.add(hull)
        self.add(dots)

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

#### \_original_\_init_\_(\*points, tolerance=1e-05, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **points** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **tolerance** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
