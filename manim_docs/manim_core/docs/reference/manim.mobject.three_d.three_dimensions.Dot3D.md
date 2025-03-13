# Dot3D

Qualified name: `manim.mobject.three\_d.three\_dimensions.Dot3D`

### *class* Dot3D(point=array([0., 0., 0.]), radius=0.08, color=ManimColor('#FFFFFF'), resolution=(8, 8), \*\*kwargs)

Bases: [`Sphere`](manim.mobject.three_d.three_dimensions.Sphere.md#manim.mobject.three_d.three_dimensions.Sphere)

A spherical dot.

* **Parameters:**
  * **point** (*list* *|* *np.ndarray*) – The location of the dot.
  * **radius** (*float*) – The radius of the dot.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the [`Dot3D`](#manim.mobject.three_d.three_dimensions.Dot3D).
  * **resolution** (*tuple* *[**int* *,* *int* *]*) – The number of samples taken of the [`Dot3D`](#manim.mobject.three_d.three_dimensions.Dot3D). A tuple can be
    used to define different resolutions for `u` and `v` respectively.

### Examples

<div id="dot3dexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Dot3DExample <a class="headerlink" href="#dot3dexample">¶</a></p>![image](media/images/Dot3DExample-1.png)
```python
from manim import *

class Dot3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        dot_1 = Dot3D(point=axes.coords_to_point(0, 0, 1), color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.add(axes, dot_1, dot_2,dot_3)
```

<pre data-manim-binder data-manim-classname="Dot3DExample">
class Dot3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75\*DEGREES, theta=-45\*DEGREES)

        axes = ThreeDAxes()
        dot_1 = Dot3D(point=axes.coords_to_point(0, 0, 1), color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.add(axes, dot_1, dot_2,dot_3)

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

#### \_original_\_init_\_(point=array([0., 0., 0.]), radius=0.08, color=ManimColor('#FFFFFF'), resolution=(8, 8), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **point** (*list* *|* *ndarray*)
  * **radius** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **resolution** (*tuple* *[**int* *,* *int* *]*)
* **Return type:**
  None
