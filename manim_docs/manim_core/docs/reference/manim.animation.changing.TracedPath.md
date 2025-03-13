# TracedPath

Qualified name: `manim.animation.changing.TracedPath`

### *class* TracedPath(traced_point_func, stroke_width=2, stroke_color=ManimColor('#FFFFFF'), dissipating_time=None, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

Traces the path of a point returned by a function call.

* **Parameters:**
  * **traced_point_func** (*Callable*) – The function to be traced.
  * **stroke_width** (*float*) – The width of the trace.
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the trace.
  * **dissipating_time** (*float* *|* *None*) – The time taken for the path to dissipate. Default set to `None`
    which disables dissipation.

### Examples

<div id="tracedpathexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TracedPathExample <a class="headerlink" href="#tracedpathexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./TracedPathExample-1.mp4">
</video>
```python
from manim import *

class TracedPathExample(Scene):
    def construct(self):
        circ = Circle(color=RED).shift(4*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)
```

<pre data-manim-binder data-manim-classname="TracedPathExample">
class TracedPathExample(Scene):
    def construct(self):
        circ = Circle(color=RED).shift(4\*LEFT)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace, rolling_circle)
        self.play(rolling_circle.animate.shift(8\*RIGHT), run_time=4, rate_func=linear)

</pre></div><div id="dissipatingpathexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DissipatingPathExample <a class="headerlink" href="#dissipatingpathexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./DissipatingPathExample-1.mp4">
</video>
```python
from manim import *

class DissipatingPathExample(Scene):
    def construct(self):
        a = Dot(RIGHT * 2)
        b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        self.wait()
```

<pre data-manim-binder data-manim-classname="DissipatingPathExample">
class DissipatingPathExample(Scene):
    def construct(self):
        a = Dot(RIGHT \* 2)
        b = TracedPath(a.get_center, dissipating_time=0.5, stroke_opacity=[0, 1])
        self.add(a, b)
        self.play(a.animate(path_arc=PI / 4).shift(LEFT \* 2))
        self.play(a.animate(path_arc=-PI / 4).shift(LEFT \* 2))
        self.wait()

</pre></div>

### Methods

| `update_path`   |    |
|-----------------|----|

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

#### \_original_\_init_\_(traced_point_func, stroke_width=2, stroke_color=ManimColor('#FFFFFF'), dissipating_time=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **traced_point_func** (*Callable*)
  * **stroke_width** (*float*)
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **dissipating_time** (*float* *|* *None*)
