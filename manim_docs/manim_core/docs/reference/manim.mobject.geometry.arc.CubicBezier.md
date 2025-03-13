# CubicBezier

Qualified name: `manim.mobject.geometry.arc.CubicBezier`

### *class* CubicBezier(start_anchor, start_handle, end_handle, end_anchor, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A cubic Bézier curve.

### Example

<div id="beziersplineexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: BezierSplineExample <a class="headerlink" href="#beziersplineexample">¶</a></p>![image](media/images/BezierSplineExample-1.png)
```python
from manim import *

class BezierSplineExample(Scene):
    def construct(self):
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.add(l1, d1, l2, d2, bezier)
```

<pre data-manim-binder data-manim-classname="BezierSplineExample">
class BezierSplineExample(Scene):
    def construct(self):
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b)
        bezier = CubicBezier(p1b, p1b + 3 \* RIGHT, p2b - 3 \* RIGHT, p2b)
        self.add(l1, d1, l2, d2, bezier)

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
* **Parameters:**
  * **start_anchor** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **start_handle** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end_handle** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end_anchor** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(start_anchor, start_handle, end_handle, end_anchor, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **start_anchor** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **start_handle** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end_handle** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end_anchor** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **kwargs** (*Any*)
* **Return type:**
  None
