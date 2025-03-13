# BraceBetweenPoints

Qualified name: `manim.mobject.svg.brace.BraceBetweenPoints`

### *class* BraceBetweenPoints(point_1, point_2, direction=array([0., 0., 0.]), \*\*kwargs)

Bases: [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace)

Similar to Brace, but instead of taking a mobject it uses 2
points to place the brace.

A fitting direction for the brace is
computed, but it still can be manually overridden.
If the points go from left to right, the brace is drawn from below.
Swapping the points places the brace on the opposite side.

* **Parameters:**
  * **point_1** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – The first point.
  * **point_2** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – The second point.
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D) *|* *None*) – The direction from which the brace faces towards the points.

### Examples

<div id="bracebpexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: BraceBPExample <a class="headerlink" href="#bracebpexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./BraceBPExample-1.mp4">
</video>
```python
from manim import *

class BraceBPExample(Scene):
    def construct(self):
        p1 = [0,0,0]
        p2 = [1,2,0]
        brace = BraceBetweenPoints(p1,p2)
        self.play(Create(NumberPlane()))
        self.play(Create(brace))
        self.wait(2)
```

<pre data-manim-binder data-manim-classname="BraceBPExample">
class BraceBPExample(Scene):
    def construct(self):
        p1 = [0,0,0]
        p2 = [1,2,0]
        brace = BraceBetweenPoints(p1,p2)
        self.play(Create(NumberPlane()))
        self.play(Create(brace))
        self.wait(2)

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

#### \_original_\_init_\_(point_1, point_2, direction=array([0., 0., 0.]), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **point_1** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **point_2** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D) *|* *None*)
