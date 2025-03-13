# Dot

Qualified name: `manim.mobject.geometry.arc.Dot`

### *class* Dot(point=array([0., 0., 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=ManimColor('#FFFFFF'), \*\*kwargs)

Bases: [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle)

A circle with a very small radius.

* **Parameters:**
  * **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The location of the dot.
  * **radius** (*float*) – The radius of the dot.
  * **stroke_width** (*float*) – The thickness of the outline of the dot.
  * **fill_opacity** (*float*) – The opacity of the dot’s fill_colour
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the dot.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle)

### Examples

<div id="dotexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DotExample <a class="headerlink" href="#dotexample">¶</a></p>![image](media/images/DotExample-1.png)
```python
from manim import *

class DotExample(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT, radius=0.08)
        dot2 = Dot(point=ORIGIN)
        dot3 = Dot(point=RIGHT)
        self.add(dot1,dot2,dot3)
```

<pre data-manim-binder data-manim-classname="DotExample">
class DotExample(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT, radius=0.08)
        dot2 = Dot(point=ORIGIN)
        dot3 = Dot(point=RIGHT)
        self.add(dot1,dot2,dot3)

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

#### \_original_\_init_\_(point=array([0., 0., 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=ManimColor('#FFFFFF'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **radius** (*float*)
  * **stroke_width** (*float*)
  * **fill_opacity** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)
* **Return type:**
  None
