# ArcBetweenPoints

Qualified name: `manim.mobject.geometry.arc.ArcBetweenPoints`

### *class* ArcBetweenPoints(start, end, angle=1.5707963267948966, radius=None, \*\*kwargs)

Bases: [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)

Inherits from Arc and additionally takes 2 points between which the arc is spanned.

### Example

<div id="arcbetweenpointsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ArcBetweenPointsExample <a class="headerlink" href="#arcbetweenpointsexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ArcBetweenPointsExample-1.mp4">
</video>
```python
from manim import *

class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))
```

<pre data-manim-binder data-manim-classname="ArcBetweenPointsExample">
class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 \* RIGHT, end=2 \* UP, stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))

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
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **angle** (*float*)
  * **radius** (*float* *|* *None*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(start, end, angle=1.5707963267948966, radius=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **angle** (*float*)
  * **radius** (*float* *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
