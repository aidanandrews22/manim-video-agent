# Torus

Qualified name: `manim.mobject.three\_d.three\_dimensions.Torus`

### *class* Torus(major_radius=3, minor_radius=1, u_range=(0, 6.283185307179586), v_range=(0, 6.283185307179586), resolution=None, \*\*kwargs)

Bases: [`Surface`](manim.mobject.three_d.three_dimensions.Surface.md#manim.mobject.three_d.three_dimensions.Surface)

A torus.

* **Parameters:**
  * **major_radius** (*float*) – Distance from the center of the tube to the center of the torus.
  * **minor_radius** (*float*) – Radius of the tube.
  * **u_range** (*Sequence* *[**float* *]*) – The range of the `u` variable: `(u_min, u_max)`.
  * **v_range** (*Sequence* *[**float* *]*) – The range of the `v` variable: `(v_min, v_max)`.
  * **resolution** (*tuple* *[**int* *,* *int* *]*  *|* *None*) – The number of samples taken of the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus). A tuple can be
    used to define different resolutions for `u` and `v` respectively.

### Examples

<div id="exampletorus" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ExampleTorus <a class="headerlink" href="#exampletorus">¶</a></p>![image](media/images/ExampleTorus-1.png)
```python
from manim import *

class ExampleTorus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        torus = Torus()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, torus)
```

<pre data-manim-binder data-manim-classname="ExampleTorus">
class ExampleTorus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        torus = Torus()
        self.set_camera_orientation(phi=75 \* DEGREES, theta=30 \* DEGREES)
        self.add(axes, torus)

</pre></div>

### Methods

| [`func`](#manim.mobject.three_d.three_dimensions.Torus.func)   | The z values defining the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus) being plotted.   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|

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

#### \_original_\_init_\_(major_radius=3, minor_radius=1, u_range=(0, 6.283185307179586), v_range=(0, 6.283185307179586), resolution=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **major_radius** (*float*)
  * **minor_radius** (*float*)
  * **u_range** (*Sequence* *[**float* *]*)
  * **v_range** (*Sequence* *[**float* *]*)
  * **resolution** (*tuple* *[**int* *,* *int* *]*  *|* *None*)
* **Return type:**
  None

#### func(u, v)

The z values defining the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus) being plotted.

* **Returns:**
  The z values defining the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus).
* **Return type:**
  `numpy.ndarray`
* **Parameters:**
  * **u** (*float*)
  * **v** (*float*)
