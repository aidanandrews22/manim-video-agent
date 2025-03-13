# SurroundingRectangle

Qualified name: `manim.mobject.geometry.shape\_matchers.SurroundingRectangle`

### *class* SurroundingRectangle(\*mobjects, color=ManimColor('#FFFF00'), buff=0.1, corner_radius=0.0, \*\*kwargs)

Bases: [`RoundedRectangle`](manim.mobject.geometry.polygram.RoundedRectangle.md#manim.mobject.geometry.polygram.RoundedRectangle)

A rectangle surrounding a [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

<div id="surroundingrectexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SurroundingRectExample <a class="headerlink" href="#surroundingrectexample">¶</a></p>![image](media/images/SurroundingRectExample-1.png)
```python
from manim import *

class SurroundingRectExample(Scene):
    def construct(self):
        title = Title("A Quote from Newton")
        quote = Text(
            "If I have seen further than others, \n"
            "it is by standing upon the shoulders of giants.",
            color=BLUE,
        ).scale(0.75)
        box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

        t2 = Tex(r"Hello World").scale(1.5)
        box2 = SurroundingRectangle(t2, corner_radius=0.2)
        mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
        self.add(title, mobjects)
```

<pre data-manim-binder data-manim-classname="SurroundingRectExample">
class SurroundingRectExample(Scene):
    def construct(self):
        title = Title("A Quote from Newton")
        quote = Text(
            "If I have seen further than others, \\n"
            "it is by standing upon the shoulders of giants.",
            color=BLUE,
        ).scale(0.75)
        box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

        t2 = Tex(r"Hello World").scale(1.5)
        box2 = SurroundingRectangle(t2, corner_radius=0.2)
        mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
        self.add(title, mobjects)

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
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **buff** (*float*)
  * **corner_radius** (*float*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(\*mobjects, color=ManimColor('#FFFF00'), buff=0.1, corner_radius=0.0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **buff** (*float*)
  * **corner_radius** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
