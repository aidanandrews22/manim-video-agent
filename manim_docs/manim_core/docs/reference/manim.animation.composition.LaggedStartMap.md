# LaggedStartMap

Qualified name: `manim.animation.composition.LaggedStartMap`

### *class* LaggedStartMap(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`LaggedStart`](manim.animation.composition.LaggedStart.md#manim.animation.composition.LaggedStart)

Plays a series of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) while mapping a function to submobjects.

* **Parameters:**
  * **AnimationClass** (*Callable* *[* *...* *,* [*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) to apply to mobject.
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) whose submobjects the animation, and optionally the function,
    are to be applied.
  * **arg_creator** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *str* *]*) – Function which will be applied to [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **run_time** (*float*) – The duration of the animation in seconds.

### Examples

<div id="laggedstartmapexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LaggedStartMapExample <a class="headerlink" href="#laggedstartmapexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./LaggedStartMapExample-1.mp4">
</video>
```python
from manim import *

class LaggedStartMapExample(Scene):
    def construct(self):
        title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
        dots = VGroup(
            *[Dot(radius=0.16) for _ in range(35)]
            ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
        self.add(dots, title)

        # Animate yellow ripple effect
        for mob in dots, title:
            self.play(LaggedStartMap(
                ApplyMethod, mob,
                lambda m : (m.set_color, YELLOW),
                lag_ratio = 0.1,
                rate_func = there_and_back,
                run_time = 2
            ))
```

<pre data-manim-binder data-manim-classname="LaggedStartMapExample">
class LaggedStartMapExample(Scene):
    def construct(self):
        title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
        dots = VGroup(
            \*[Dot(radius=0.16) for \_ in range(35)]
            ).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
        self.add(dots, title)

        # Animate yellow ripple effect
        for mob in dots, title:
            self.play(LaggedStartMap(
                ApplyMethod, mob,
                lambda m : (m.set_color, YELLOW),
                lag_ratio = 0.1,
                rate_func = there_and_back,
                run_time = 2
            ))

</pre></div>

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(AnimationClass, mobject, arg_creator=None, run_time=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **AnimationClass** (*Callable* *[* *[* *...* *]* *,* [*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **arg_creator** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *str* *]*)
  * **run_time** (*float*)
* **Return type:**
  None
