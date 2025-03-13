# GrowFromPoint

Qualified name: `manim.animation.growing.GrowFromPoint`

### *class* GrowFromPoint(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) by growing it from a point.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to be introduced.
  * **point** (*np.ndarray*) – The point from which the mobject grows.
  * **point_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

### Examples

<div id="growfrompointexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GrowFromPointExample <a class="headerlink" href="#growfrompointexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./GrowFromPointExample-1.mp4">
</video>
```python
from manim import *

class GrowFromPointExample(Scene):
    def construct(self):
        dot = Dot(3 * UR, color=GREEN)
        squares = [Square() for _ in range(4)]
        VGroup(*squares).set_x(0).arrange(buff=1)
        self.add(dot)
        self.play(GrowFromPoint(squares[0], ORIGIN))
        self.play(GrowFromPoint(squares[1], [-2, 2, 0]))
        self.play(GrowFromPoint(squares[2], [3, -2, 0], RED))
        self.play(GrowFromPoint(squares[3], dot, dot.get_color()))
```

<pre data-manim-binder data-manim-classname="GrowFromPointExample">
class GrowFromPointExample(Scene):
    def construct(self):
        dot = Dot(3 \* UR, color=GREEN)
        squares = [Square() for \_ in range(4)]
        VGroup(\*squares).set_x(0).arrange(buff=1)
        self.add(dot)
        self.play(GrowFromPoint(squares[0], ORIGIN))
        self.play(GrowFromPoint(squares[1], [-2, 2, 0]))
        self.play(GrowFromPoint(squares[2], [3, -2, 0], RED))
        self.play(GrowFromPoint(squares[3], dot, dot.get_color()))

</pre></div>

### Methods

| `create_starting_mobject`   |    |
|-----------------------------|----|
| `create_target`             |    |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, point, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **point** (*np.ndarray*)
  * **point_color** (*str*)
* **Return type:**
  None
