# growing

Animations that introduce mobjects to scene by growing them from points.

<div id="growing" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Growing <a class="headerlink" href="#growing">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./Growing-1.mp4">
</video>
```python
from manim import *

class Growing(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        arrow = Arrow(LEFT, RIGHT)
        star = Star()

        VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
        VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)

        self.play(GrowFromPoint(square, ORIGIN))
        self.play(GrowFromCenter(circle))
        self.play(GrowFromEdge(triangle, DOWN))
        self.play(GrowArrow(arrow))
        self.play(SpinInFromNothing(star))
```

<pre data-manim-binder data-manim-classname="Growing">
class Growing(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        arrow = Arrow(LEFT, RIGHT)
        star = Star()

        VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
        VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)

        self.play(GrowFromPoint(square, ORIGIN))
        self.play(GrowFromCenter(circle))
        self.play(GrowFromEdge(triangle, DOWN))
        self.play(GrowArrow(arrow))
        self.play(SpinInFromNothing(star))

</pre></div>

### Classes

| [`GrowArrow`](manim.animation.growing.GrowArrow.md#manim.animation.growing.GrowArrow)                         | Introduce an [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow) by growing it from its start toward its tip.   |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [`GrowFromCenter`](manim.animation.growing.GrowFromCenter.md#manim.animation.growing.GrowFromCenter)          | Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) by growing it from its center.                       |
| [`GrowFromEdge`](manim.animation.growing.GrowFromEdge.md#manim.animation.growing.GrowFromEdge)                | Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) by growing it from one of its bounding box edges.    |
| [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.md#manim.animation.growing.GrowFromPoint)             | Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) by growing it from a point.                          |
| [`SpinInFromNothing`](manim.animation.growing.SpinInFromNothing.md#manim.animation.growing.SpinInFromNothing) | Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) spinning and growing it from its center.             |
