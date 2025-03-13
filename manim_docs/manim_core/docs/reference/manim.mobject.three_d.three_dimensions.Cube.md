# Cube

Qualified name: `manim.mobject.three\_d.three\_dimensions.Cube`

### *class* Cube(side_length=2, fill_opacity=0.75, fill_color=ManimColor('#58C4DD'), stroke_width=0, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

A three-dimensional cube.

* **Parameters:**
  * **side_length** (*float*) – Length of each side of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).
  * **fill_opacity** (*float*) – The opacity of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube), from 0 being fully transparent to 1 being
    fully opaque. Defaults to 0.75.
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).
  * **stroke_width** (*float*) – The width of the stroke surrounding each face of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).

### Examples

<div id="cubeexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CubeExample <a class="headerlink" href="#cubeexample">¶</a></p>![image](media/images/CubeExample-1.png)
```python
from manim import *

class CubeExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
        self.add(cube)
```

<pre data-manim-binder data-manim-classname="CubeExample">
class CubeExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75\*DEGREES, theta=-45\*DEGREES)

        axes = ThreeDAxes()
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
        self.add(cube)

</pre></div>

### Methods

| [`generate_points`](#manim.mobject.three_d.three_dimensions.Cube.generate_points)   | Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).   |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [`init_points`](#manim.mobject.three_d.three_dimensions.Cube.init_points)           | Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).   |

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

#### \_original_\_init_\_(side_length=2, fill_opacity=0.75, fill_color=ManimColor('#58C4DD'), stroke_width=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **side_length** (*float*)
  * **fill_opacity** (*float*)
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **stroke_width** (*float*)
* **Return type:**
  None

#### generate_points()

Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).

* **Return type:**
  None

#### init_points()

Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).

* **Return type:**
  None
