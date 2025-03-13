# Brace

Qualified name: `manim.mobject.svg.brace.Brace`

### *class* Brace(mobject, direction=array([0., -1., 0.]), buff=0.2, sharpness=2, stroke_width=0, fill_opacity=1.0, background_stroke_width=0, background_stroke_color=ManimColor('#000000'), \*\*kwargs)

Bases: [`VMobjectFromSVGPath`](manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.md#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath)

Takes a mobject and draws a brace adjacent to it.

Passing a direction vector determines the direction from which the
brace is drawn. By default it is drawn from below.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject adjacent to which the brace is placed.
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D) *|* *None*) – The direction from which the brace faces the mobject.
  * **buff** (*float*)
  * **sharpness** (*float*)
  * **stroke_width** (*float*)
  * **fill_opacity** (*float*)
  * **background_stroke_width** (*float*)
  * **background_stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))

#### SEE ALSO
[`BraceBetweenPoints`](manim.mobject.svg.brace.BraceBetweenPoints.md#manim.mobject.svg.brace.BraceBetweenPoints)

### Examples

<div id="braceexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: BraceExample <a class="headerlink" href="#braceexample">¶</a></p>![image](media/images/BraceExample-1.png)
```python
from manim import *

class BraceExample(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        for i in np.linspace(0.1,1.0,4):
            br = Brace(s, sharpness=i)
            t = Text(f"sharpness= {i}").next_to(br, RIGHT)
            self.add(t)
            self.add(br)
        VGroup(*self.mobjects).arrange(DOWN, buff=0.2)
```

<pre data-manim-binder data-manim-classname="BraceExample">
class BraceExample(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        for i in np.linspace(0.1,1.0,4):
            br = Brace(s, sharpness=i)
            t = Text(f"sharpness= {i}").next_to(br, RIGHT)
            self.add(t)
            self.add(br)
        VGroup(\*self.mobjects).arrange(DOWN, buff=0.2)

</pre></div>

### Methods

| [`get_direction`](#manim.mobject.svg.brace.Brace.get_direction)   | Returns the direction from the center to the brace tip.   |
|-------------------------------------------------------------------|-----------------------------------------------------------|
| [`get_tex`](#manim.mobject.svg.brace.Brace.get_tex)               | Places the tex at the brace tip.                          |
| [`get_text`](#manim.mobject.svg.brace.Brace.get_text)             | Places the text at the brace tip.                         |
| [`get_tip`](#manim.mobject.svg.brace.Brace.get_tip)               | Returns the point at the brace tip.                       |
| [`put_at_tip`](#manim.mobject.svg.brace.Brace.put_at_tip)         | Puts the given mobject at the brace tip.                  |

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

#### \_original_\_init_\_(mobject, direction=array([0., -1., 0.]), buff=0.2, sharpness=2, stroke_width=0, fill_opacity=1.0, background_stroke_width=0, background_stroke_color=ManimColor('#000000'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D) *|* *None*)
  * **buff** (*float*)
  * **sharpness** (*float*)
  * **stroke_width** (*float*)
  * **fill_opacity** (*float*)
  * **background_stroke_width** (*float*)
  * **background_stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))

#### get_direction()

Returns the direction from the center to the brace tip.

#### get_tex(\*tex, \*\*kwargs)

Places the tex at the brace tip.

* **Parameters:**
  * **tex** – The tex to be placed at the brace tip.
  * **kwargs** – Any further keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip) which
    is used to position the tex at the brace tip.
* **Return type:**
  [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

#### get_text(\*text, \*\*kwargs)

Places the text at the brace tip.

* **Parameters:**
  * **text** – The text to be placed at the brace tip.
  * **kwargs** – Any additional keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip) which
    is used to position the text at the brace tip.
* **Return type:**
  [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)

#### get_tip()

Returns the point at the brace tip.

#### put_at_tip(mob, use_next_to=True, \*\*kwargs)

Puts the given mobject at the brace tip.

* **Parameters:**
  * **mob** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be placed at the tip.
  * **use_next_to** (*bool*) – If true, then `next_to()` is used to place the mobject at the
    tip.
  * **kwargs** – Any additional keyword arguments are passed to `next_to()` which
    is used to put the mobject next to the brace tip.
