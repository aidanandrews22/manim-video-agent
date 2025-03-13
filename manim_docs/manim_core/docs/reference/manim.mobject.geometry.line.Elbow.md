# Elbow

Qualified name: `manim.mobject.geometry.line.Elbow`

### *class* Elbow(width=0.2, angle=0, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

Two lines that create a right angle about each other: L-shape.

* **Parameters:**
  * **width** (*float*) – The length of the elbow’s sides.
  * **angle** (*float*) – The rotation of the elbow.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)
  * **seealso::** ( *..*) – [`RightAngle`](manim.mobject.geometry.line.RightAngle.md#manim.mobject.geometry.line.RightAngle)

### Examples

<div id="elbowexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ElbowExample <a class="headerlink" href="#elbowexample">¶</a></p>![image](media/images/ElbowExample-1.png)
```python
from manim import *

class ElbowExample(Scene):
    def construct(self):
        elbow_1 = Elbow()
        elbow_2 = Elbow(width=2.0)
        elbow_3 = Elbow(width=2.0, angle=5*PI/4)

        elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
        self.add(elbow_group)
```

<pre data-manim-binder data-manim-classname="ElbowExample">
class ElbowExample(Scene):
    def construct(self):
        elbow_1 = Elbow()
        elbow_2 = Elbow(width=2.0)
        elbow_3 = Elbow(width=2.0, angle=5\*PI/4)

        elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
        self.add(elbow_group)

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

#### \_original_\_init_\_(width=0.2, angle=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **width** (*float*)
  * **angle** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
