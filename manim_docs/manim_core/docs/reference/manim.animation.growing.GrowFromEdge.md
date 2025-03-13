# GrowFromEdge

Qualified name: `manim.animation.growing.GrowFromEdge`

### *class* GrowFromEdge(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.md#manim.animation.growing.GrowFromPoint)

Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) by growing it from one of its bounding box edges.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to be introduced.
  * **edge** (*np.ndarray*) – The direction to seek bounding box edge of mobject.
  * **point_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

### Examples

<div id="growfromedgeexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GrowFromEdgeExample <a class="headerlink" href="#growfromedgeexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./GrowFromEdgeExample-1.mp4">
</video>
```python
from manim import *

class GrowFromEdgeExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(4)]
        VGroup(*squares).set_x(0).arrange(buff=1)
        self.play(GrowFromEdge(squares[0], DOWN))
        self.play(GrowFromEdge(squares[1], RIGHT))
        self.play(GrowFromEdge(squares[2], UR))
        self.play(GrowFromEdge(squares[3], UP, point_color=RED))
```

<pre data-manim-binder data-manim-classname="GrowFromEdgeExample">
class GrowFromEdgeExample(Scene):
    def construct(self):
        squares = [Square() for \_ in range(4)]
        VGroup(\*squares).set_x(0).arrange(buff=1)
        self.play(GrowFromEdge(squares[0], DOWN))
        self.play(GrowFromEdge(squares[1], RIGHT))
        self.play(GrowFromEdge(squares[2], UR))
        self.play(GrowFromEdge(squares[3], UP, point_color=RED))

</pre></div>

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, edge, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **edge** (*np.ndarray*)
  * **point_color** (*str*)
* **Return type:**
  None
