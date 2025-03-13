# Integer

Qualified name: `manim.mobject.text.numbers.Integer`

### *class* Integer(number=0, num_decimal_places=0, \*\*kwargs)

Bases: [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber)

A class for displaying Integers.

### Examples

<div id="integerexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: IntegerExample <a class="headerlink" href="#integerexample">¶</a></p>![image](media/images/IntegerExample-1.png)
```python
from manim import *

class IntegerExample(Scene):
    def construct(self):
        self.add(Integer(number=2.5).set_color(ORANGE).scale(2.5).set_x(-0.5).set_y(0.8))
        self.add(Integer(number=3.14159, show_ellipsis=True).set_x(3).set_y(3.3).scale(3.14159))
        self.add(Integer(number=42).set_x(2.5).set_y(-2.3).set_color_by_gradient(BLUE, TEAL).scale(1.7))
        self.add(Integer(number=6.28).set_x(-1.5).set_y(-2).set_color(YELLOW).scale(1.4))
```

<pre data-manim-binder data-manim-classname="IntegerExample">
class IntegerExample(Scene):
    def construct(self):
        self.add(Integer(number=2.5).set_color(ORANGE).scale(2.5).set_x(-0.5).set_y(0.8))
        self.add(Integer(number=3.14159, show_ellipsis=True).set_x(3).set_y(3.3).scale(3.14159))
        self.add(Integer(number=42).set_x(2.5).set_y(-2.3).set_color_by_gradient(BLUE, TEAL).scale(1.7))
        self.add(Integer(number=6.28).set_x(-1.5).set_y(-2).set_color(YELLOW).scale(1.4))

</pre></div>

### Methods

| `get_value`   |    |
|---------------|----|

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `font_size`           | The font size of the tex mobject.                                      |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |
* **Parameters:**
  * **number** (*float*)
  * **num_decimal_places** (*int*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(number=0, num_decimal_places=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **number** (*float*)
  * **num_decimal_places** (*int*)
  * **kwargs** (*Any*)
* **Return type:**
  None
