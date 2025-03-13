# DecimalMatrix

Qualified name: `manim.mobject.matrix.DecimalMatrix`

### *class* DecimalMatrix(matrix, element_to_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>, element_to_mobject_config={'num_decimal_places': 1}, \*\*kwargs)

Bases: [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)

A mobject that displays a matrix with decimal entries on the screen.

### Examples

<div id="decimalmatrixexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DecimalMatrixExample <a class="headerlink" href="#decimalmatrixexample">¶</a></p>![image](media/images/DecimalMatrixExample-1.png)
```python
from manim import *

class DecimalMatrixExample(Scene):
    def construct(self):
        m0 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\\{",
            right_bracket="\\}")
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="DecimalMatrixExample">
class DecimalMatrixExample(Scene):
    def construct(self):
        m0 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\\\\{",
            right_bracket="\\\\}")
        self.add(m0)

</pre></div>

Will round/truncate the decimal places as per the provided config.

* **Parameters:**
  * **matrix** (*Iterable*) – A numpy 2d array or list of lists
  * **element_to_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – Mobject to use, by default DecimalNumber
  * **element_to_mobject_config** (*dict* *[**str* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – Config for the desired mobject, by default {“num_decimal_places”: 1}

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

#### \_original_\_init_\_(matrix, element_to_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>, element_to_mobject_config={'num_decimal_places': 1}, \*\*kwargs)

Will round/truncate the decimal places as per the provided config.

* **Parameters:**
  * **matrix** (*Iterable*) – A numpy 2d array or list of lists
  * **element_to_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – Mobject to use, by default DecimalNumber
  * **element_to_mobject_config** (*dict* *[**str* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – Config for the desired mobject, by default {“num_decimal_places”: 1}
