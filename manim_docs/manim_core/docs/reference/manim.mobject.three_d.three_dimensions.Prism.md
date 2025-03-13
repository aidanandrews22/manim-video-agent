# Prism

Qualified name: `manim.mobject.three\_d.three\_dimensions.Prism`

### *class* Prism(dimensions=[3, 2, 1], \*\*kwargs)

Bases: [`Cube`](manim.mobject.three_d.three_dimensions.Cube.md#manim.mobject.three_d.three_dimensions.Cube)

A right rectangular prism (or rectangular cuboid).
Defined by the length of each side in `[x, y, z]` format.

* **Parameters:**
  **dimensions** (*tuple* *[**float* *,* *float* *,* *float* *]*  *|* *np.ndarray*) – Dimensions of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism) in `[x, y, z]` format.

### Examples

<div id="exampleprism" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ExamplePrism <a class="headerlink" href="#exampleprism">¶</a></p>![image](media/images/ExamplePrism-1.png)
```python
from manim import *

class ExamplePrism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        self.add(prismSmall, prismLarge)
```

<pre data-manim-binder data-manim-classname="ExamplePrism">
class ExamplePrism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 \* DEGREES, theta=150 \* DEGREES)
        prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        self.add(prismSmall, prismLarge)

</pre></div>

### Methods

| [`generate_points`](#manim.mobject.three_d.three_dimensions.Prism.generate_points)   | Creates the sides of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism).   |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|

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

#### \_original_\_init_\_(dimensions=[3, 2, 1], \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **dimensions** (*tuple* *[**float* *,* *float* *,* *float* *]*  *|* *ndarray*)
* **Return type:**
  None

#### generate_points()

Creates the sides of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism).

* **Return type:**
  None
