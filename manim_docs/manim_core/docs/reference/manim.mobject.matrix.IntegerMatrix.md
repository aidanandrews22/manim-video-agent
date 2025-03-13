# IntegerMatrix

Qualified name: `manim.mobject.matrix.IntegerMatrix`

### *class* IntegerMatrix(matrix, element_to_mobject=<class 'manim.mobject.text.numbers.Integer'>, \*\*kwargs)

Bases: [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)

A mobject that displays a matrix with integer entries on the screen.

### Examples

<div id="integermatrixexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: IntegerMatrixExample <a class="headerlink" href="#integermatrixexample">¶</a></p>![image](media/images/IntegerMatrixExample-1.png)
```python
from manim import *

class IntegerMatrixExample(Scene):
    def construct(self):
        m0 = IntegerMatrix(
            [[3.7, 2], [42.2, 12]],
            left_bracket="(",
            right_bracket=")")
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="IntegerMatrixExample">
class IntegerMatrixExample(Scene):
    def construct(self):
        m0 = IntegerMatrix(
            [[3.7, 2], [42.2, 12]],
            left_bracket="(",
            right_bracket=")")
        self.add(m0)

</pre></div>

Will round if there are decimal entries in the matrix.

* **Parameters:**
  * **matrix** (*Iterable*) – A numpy 2d array or list of lists
  * **element_to_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – Mobject to use, by default Integer

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

#### \_original_\_init_\_(matrix, element_to_mobject=<class 'manim.mobject.text.numbers.Integer'>, \*\*kwargs)

Will round if there are decimal entries in the matrix.

* **Parameters:**
  * **matrix** (*Iterable*) – A numpy 2d array or list of lists
  * **element_to_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – Mobject to use, by default Integer
