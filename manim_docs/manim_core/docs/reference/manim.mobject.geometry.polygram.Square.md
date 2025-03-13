# Square

Qualified name: `manim.mobject.geometry.polygram.Square`

### *class* Square(side_length=2.0, \*\*kwargs)

Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle)

A rectangle with equal side lengths.

* **Parameters:**
  * **side_length** (*float*) – The length of the sides of the square.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle).

### Examples

<div id="squareexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SquareExample <a class="headerlink" href="#squareexample">¶</a></p>![image](media/images/SquareExample-1.png)
```python
from manim import *

class SquareExample(Scene):
    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)
```

<pre data-manim-binder data-manim-classname="SquareExample">
class SquareExample(Scene):
    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)

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
| `side_length`         |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(side_length=2.0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **side_length** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
