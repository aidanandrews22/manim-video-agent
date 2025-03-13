# Exclusion

Qualified name: `manim.mobject.geometry.boolean\_ops.Exclusion`

### *class* Exclusion(subject, clip, \*\*kwargs)

Bases: `_BooleanOps`

Find the XOR between two [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).
This creates a new [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) consisting of the region
covered by exactly one of them.

* **Parameters:**
  * **subject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The 1st [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).
  * **clip** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The 2nd [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)
  * **kwargs** (*Any*)

### Example

<div id="intersectionexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: IntersectionExample <a class="headerlink" href="#intersectionexample">¶</a></p>![image](media/images/IntersectionExample-1.png)
```python
from manim import *

class IntersectionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Exclusion(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0.4, 0])
        self.add(sq, cr, un)
```

<pre data-manim-binder data-manim-classname="IntersectionExample">
class IntersectionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Exclusion(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0.4, 0])
        self.add(sq, cr, un)

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

#### \_original_\_init_\_(subject, clip, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **subject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **clip** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **kwargs** (*Any*)
* **Return type:**
  None
