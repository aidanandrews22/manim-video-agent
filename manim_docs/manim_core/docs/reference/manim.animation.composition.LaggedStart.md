# LaggedStart

Qualified name: `manim.animation.composition.LaggedStart`

### *class* LaggedStart(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.md#manim.animation.composition.AnimationGroup)

Adjusts the timing of a series of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) according to `lag_ratio`.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation)) – Sequence of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) objects to be played.
  * **lag_ratio** (*float*) – 

    Defines the delay after which the animation is applied to submobjects. A lag_ratio of
    `n.nn` means the next animation will play when `nnn%` of the current animation has played.
    Defaults to 0.05, meaning that the next animation will begin when 5% of the current
    animation has played.

    This does not influence the total runtime of the animation. Instead the runtime
    of individual animations is adjusted so that the complete animation has the defined
    run time.

### Examples

<div id="laggedstartexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LaggedStartExample <a class="headerlink" href="#laggedstartexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./LaggedStartExample-1.mp4">
</video>
```python
from manim import *

class LaggedStartExample(Scene):
    def construct(self):
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
        dot2 = Dot(point=LEFT * 2, radius=0.16)
        dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
        line_25 = DashedLine(
            start=LEFT + UP * 2,
            end=LEFT + DOWN * 2,
            color=RED
        )
        label = Text("25%", font_size=24).next_to(line_25, UP)
        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(LaggedStart(
            dot1.animate.shift(RIGHT * 4),
            dot2.animate.shift(RIGHT * 4),
            dot3.animate.shift(RIGHT * 4),
            lag_ratio=0.25,
            run_time=4
        ))
```

<pre data-manim-binder data-manim-classname="LaggedStartExample">
class LaggedStartExample(Scene):
    def construct(self):
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = Dot(point=LEFT \* 2 + UP, radius=0.16)
        dot2 = Dot(point=LEFT \* 2, radius=0.16)
        dot3 = Dot(point=LEFT \* 2 + DOWN, radius=0.16)
        line_25 = DashedLine(
            start=LEFT + UP \* 2,
            end=LEFT + DOWN \* 2,
            color=RED
        )
        label = Text("25%", font_size=24).next_to(line_25, UP)
        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(LaggedStart(
            dot1.animate.shift(RIGHT \* 4),
            dot2.animate.shift(RIGHT \* 4),
            dot3.animate.shift(RIGHT \* 4),
            lag_ratio=0.25,
            run_time=4
        ))

</pre></div>

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(\*animations, lag_ratio=0.05, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **lag_ratio** (*float*)
