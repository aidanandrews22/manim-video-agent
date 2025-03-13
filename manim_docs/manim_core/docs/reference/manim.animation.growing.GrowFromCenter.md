# GrowFromCenter

Qualified name: `manim.animation.growing.GrowFromCenter`

### *class* GrowFromCenter(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.md#manim.animation.growing.GrowFromPoint)

Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) by growing it from its center.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to be introduced.
  * **point_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

### Examples

<div id="growfromcenterexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GrowFromCenterExample <a class="headerlink" href="#growfromcenterexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./GrowFromCenterExample-1.mp4">
</video>
```python
from manim import *

class GrowFromCenterExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(2)]
        VGroup(*squares).set_x(0).arrange(buff=2)
        self.play(GrowFromCenter(squares[0]))
        self.play(GrowFromCenter(squares[1], point_color=RED))
```

<pre data-manim-binder data-manim-classname="GrowFromCenterExample">
class GrowFromCenterExample(Scene):
    def construct(self):
        squares = [Square() for \_ in range(2)]
        VGroup(\*squares).set_x(0).arrange(buff=2)
        self.play(GrowFromCenter(squares[0]))
        self.play(GrowFromCenter(squares[1], point_color=RED))

</pre></div>

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **point_color** (*str*)
* **Return type:**
  None
