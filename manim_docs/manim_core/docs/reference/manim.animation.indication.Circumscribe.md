# Circumscribe

Qualified name: `manim.animation.indication.Circumscribe`

### *class* Circumscribe(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Succession`](manim.animation.composition.Succession.md#manim.animation.composition.Succession)

Draw a temporary line surrounding the mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be circumscribed.
  * **shape** (*type*) – The shape with which to surround the given mobject. Should be either
    [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle) or [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle)
  * **fade_in** – Whether to make the surrounding shape to fade in. It will be drawn otherwise.
  * **fade_out** – Whether to make the surrounding shape to fade out. It will be undrawn otherwise.
  * **time_width** – The time_width of the drawing and undrawing. Gets ignored if either fade_in or fade_out is True.
  * **buff** (*float*) – The distance between the surrounding shape and the given mobject.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the surrounding shape.
  * **run_time** – The duration of the entire animation.
  * **kwargs** – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.md#manim.animation.composition.Succession) constructor

### Examples

<div id="usingcircumscribe" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UsingCircumscribe <a class="headerlink" href="#usingcircumscribe">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UsingCircumscribe-1.mp4">
</video>
```python
from manim import *

class UsingCircumscribe(Scene):
    def construct(self):
        lbl = Tex(r"Circum-\\scribe").scale(2)
        self.add(lbl)
        self.play(Circumscribe(lbl))
        self.play(Circumscribe(lbl, Circle))
        self.play(Circumscribe(lbl, fade_out=True))
        self.play(Circumscribe(lbl, time_width=2))
        self.play(Circumscribe(lbl, Circle, True))
```

<pre data-manim-binder data-manim-classname="UsingCircumscribe">
class UsingCircumscribe(Scene):
    def construct(self):
        lbl = Tex(r"Circum-\\\\scribe").scale(2)
        self.add(lbl)
        self.play(Circumscribe(lbl))
        self.play(Circumscribe(lbl, Circle))
        self.play(Circumscribe(lbl, fade_out=True))
        self.play(Circumscribe(lbl, time_width=2))
        self.play(Circumscribe(lbl, Circle, True))

</pre></div>

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, shape=<class 'manim.mobject.geometry.polygram.Rectangle'>, fade_in=False, fade_out=False, time_width=0.3, buff=0.1, color=ManimColor('#FFFF00'), run_time=1, stroke_width=4, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **shape** (*type*)
  * **buff** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
