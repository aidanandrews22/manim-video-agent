# ArcBrace

Qualified name: `manim.mobject.svg.brace.ArcBrace`

### *class* ArcBrace(arc=None, direction=array([1., 0., 0.]), \*\*kwargs)

Bases: [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace)

Creates a [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace) that wraps around an [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc).

The direction parameter allows the brace to be applied
from outside or inside the arc.

#### WARNING
The [`ArcBrace`](#manim.mobject.svg.brace.ArcBrace) is smaller for arcs with smaller radii.

#### NOTE
The [`ArcBrace`](#manim.mobject.svg.brace.ArcBrace) is initially a vertical [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace) defined by the
length of the [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc), but is scaled down to match the start and end
angles. An exponential function is then applied after it is shifted based on
the radius of the arc.

The scaling effect is not applied for arcs with radii smaller than 1 to prevent
over-scaling.

* **Parameters:**
  * **arc** ([*Arc*](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) *|* *None*) – The [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) that wraps around the [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace) mobject.
  * **direction** (*Sequence* *[**float* *]*) – The direction from which the brace faces the arc.
    `LEFT` for inside the arc, and `RIGHT` for the outside.

### Example

<div id="arcbraceexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ArcBraceExample <a class="headerlink" href="#arcbraceexample">¶</a></p>![image](media/images/ArcBraceExample-1.png)
```python
from manim import *

class ArcBraceExample(Scene):
    def construct(self):
        arc_1 = Arc(radius=1.5,start_angle=0,angle=2*PI/3).set_color(RED)
        brace_1 = ArcBrace(arc_1,LEFT)
        group_1 = VGroup(arc_1,brace_1)

        arc_2 = Arc(radius=3,start_angle=0,angle=5*PI/6).set_color(YELLOW)
        brace_2 = ArcBrace(arc_2)
        group_2 = VGroup(arc_2,brace_2)

        arc_3 = Arc(radius=0.5,start_angle=-0,angle=PI).set_color(BLUE)
        brace_3 = ArcBrace(arc_3)
        group_3 = VGroup(arc_3,brace_3)

        arc_4 = Arc(radius=0.2,start_angle=0,angle=3*PI/2).set_color(GREEN)
        brace_4 = ArcBrace(arc_4)
        group_4 = VGroup(arc_4,brace_4)

        arc_group = VGroup(group_1, group_2, group_3, group_4).arrange_in_grid(buff=1.5)
        self.add(arc_group.center())
```

<pre data-manim-binder data-manim-classname="ArcBraceExample">
class ArcBraceExample(Scene):
    def construct(self):
        arc_1 = Arc(radius=1.5,start_angle=0,angle=2\*PI/3).set_color(RED)
        brace_1 = ArcBrace(arc_1,LEFT)
        group_1 = VGroup(arc_1,brace_1)

        arc_2 = Arc(radius=3,start_angle=0,angle=5\*PI/6).set_color(YELLOW)
        brace_2 = ArcBrace(arc_2)
        group_2 = VGroup(arc_2,brace_2)

        arc_3 = Arc(radius=0.5,start_angle=-0,angle=PI).set_color(BLUE)
        brace_3 = ArcBrace(arc_3)
        group_3 = VGroup(arc_3,brace_3)

        arc_4 = Arc(radius=0.2,start_angle=0,angle=3\*PI/2).set_color(GREEN)
        brace_4 = ArcBrace(arc_4)
        group_4 = VGroup(arc_4,brace_4)

        arc_group = VGroup(group_1, group_2, group_3, group_4).arrange_in_grid(buff=1.5)
        self.add(arc_group.center())

</pre>

References: [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)

</div>

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

#### \_original_\_init_\_(arc=None, direction=array([1., 0., 0.]), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **arc** ([*Arc*](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) *|* *None*)
  * **direction** (*Sequence* *[**float* *]*)
