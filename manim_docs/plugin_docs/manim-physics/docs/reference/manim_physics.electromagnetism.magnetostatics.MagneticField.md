# MagneticField

Qualified name: `manim\_physics.electromagnetism.magnetostatics.MagneticField`

### *class* MagneticField(\*wires, \*\*kwargs)

Bases: `ArrowVectorField`

A magnetic field.

* **Parameters:**
  * **wires** ([*Wire*](manim_physics.electromagnetism.magnetostatics.Wire.md#manim_physics.electromagnetism.magnetostatics.Wire)) – All wires contributing to the total field.
  * **kwargs** – Additional parameters to be passed to `ArrowVectorField`.

### Example

<div id="magneticfieldexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MagneticFieldExample <a class="headerlink" href="#magneticfieldexample">¶</a></p>![image](media/images/MagneticFieldExample-1.png)
```python
from manim import *

from manim_physics import *

class MagneticFieldExample(ThreeDScene):
    def construct(self):
        wire = Wire(Circle(2).rotate(PI / 2, UP))
        mag_field = MagneticField(
            wire,
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.set_camera_orientation(PI / 3, PI / 4)
        self.add(wire, mag_field)
```

<pre data-manim-binder data-manim-classname="MagneticFieldExample">
from manim_physics import \*

class MagneticFieldExample(ThreeDScene):
    def construct(self):
        wire = Wire(Circle(2).rotate(PI / 2, UP))
        mag_field = MagneticField(
            wire,
            x_range=[-4, 4],
            y_range=[-4, 4],
        )
        self.set_camera_orientation(PI / 3, PI / 4)
        self.add(wire, mag_field)

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
