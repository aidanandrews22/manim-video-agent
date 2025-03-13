# SpinInFromNothing

Qualified name: `manim.animation.growing.SpinInFromNothing`

### *class* SpinInFromNothing(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`GrowFromCenter`](manim.animation.growing.GrowFromCenter.md#manim.animation.growing.GrowFromCenter)

Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) spinning and growing it from its center.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to be introduced.
  * **angle** (*float*) – The amount of spinning before mobject reaches its full size. E.g. 2\*PI means
    that the object will do one full spin before being fully introduced.
  * **point_color** (*str*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.

### Examples

<div id="spininfromnothingexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SpinInFromNothingExample <a class="headerlink" href="#spininfromnothingexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./SpinInFromNothingExample-1.mp4">
</video>
```python
from manim import *

class SpinInFromNothingExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(3)]
        VGroup(*squares).set_x(0).arrange(buff=2)
        self.play(SpinInFromNothing(squares[0]))
        self.play(SpinInFromNothing(squares[1], angle=2 * PI))
        self.play(SpinInFromNothing(squares[2], point_color=RED))
```

<pre data-manim-binder data-manim-classname="SpinInFromNothingExample">
class SpinInFromNothingExample(Scene):
    def construct(self):
        squares = [Square() for \_ in range(3)]
        VGroup(\*squares).set_x(0).arrange(buff=2)
        self.play(SpinInFromNothing(squares[0]))
        self.play(SpinInFromNothing(squares[1], angle=2 \* PI))
        self.play(SpinInFromNothing(squares[2], point_color=RED))

</pre></div>

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, angle=1.5707963267948966, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **angle** (*float*)
  * **point_color** (*str*)
* **Return type:**
  None
