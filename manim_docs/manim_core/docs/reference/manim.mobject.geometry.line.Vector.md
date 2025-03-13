# Vector

Qualified name: `manim.mobject.geometry.line.Vector`

### *class* Vector(direction=array([1., 0., 0.]), buff=0, \*\*kwargs)

Bases: [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)

A vector specialized for use in graphs.

* **Parameters:**
  * **direction** ([*Point2DLike*](manim.typing.md#manim.typing.Point2DLike) *|* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The direction of the arrow.
  * **buff** (*float*) – The distance of the vector from its endpoints.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)

### Examples

<div id="vectorexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: VectorExample <a class="headerlink" href="#vectorexample">¶</a></p>![image](media/images/VectorExample-1.png)
```python
from manim import *

class VectorExample(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([1,2])
        vector_2 = Vector([-5,-2])
        self.add(plane, vector_1, vector_2)
```

<pre data-manim-binder data-manim-classname="VectorExample">
class VectorExample(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([1,2])
        vector_2 = Vector([-5,-2])
        self.add(plane, vector_1, vector_2)

</pre></div>

### Methods

| [`coordinate_label`](#manim.mobject.geometry.line.Vector.coordinate_label)   | Creates a label based on the coordinates of the vector.   |
|------------------------------------------------------------------------------|-----------------------------------------------------------|

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

#### \_original_\_init_\_(direction=array([1., 0., 0.]), buff=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **direction** ([*Point2DLike*](manim.typing.md#manim.typing.Point2DLike) *|* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **buff** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### coordinate_label(integer_labels=True, n_dim=2, color=None, \*\*kwargs)

Creates a label based on the coordinates of the vector.

* **Parameters:**
  * **integer_labels** (*bool*) – Whether or not to round the coordinates to integers.
  * **n_dim** (*int*) – The number of dimensions of the vector.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – Sets the color of label, optional.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix).
* **Returns:**
  The label.
* **Return type:**
  [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)

### Examples

<div id="vectorcoordinatelabel" class="admonition admonition-manim-example">
<p class="admonition-title">Example: VectorCoordinateLabel <a class="headerlink" href="#vectorcoordinatelabel">¶</a></p>![image](media/images/VectorCoordinateLabel-1.png)
```python
from manim import *

class VectorCoordinateLabel(Scene):
    def construct(self):
        plane = NumberPlane()

        vec_1 = Vector([1, 2])
        vec_2 = Vector([-3, -2])
        label_1 = vec_1.coordinate_label()
        label_2 = vec_2.coordinate_label(color=YELLOW)

        self.add(plane, vec_1, vec_2, label_1, label_2)
```

<pre data-manim-binder data-manim-classname="VectorCoordinateLabel">
class VectorCoordinateLabel(Scene):
    def construct(self):
        plane = NumberPlane()

        vec_1 = Vector([1, 2])
        vec_2 = Vector([-3, -2])
        label_1 = vec_1.coordinate_label()
        label_2 = vec_2.coordinate_label(color=YELLOW)

        self.add(plane, vec_1, vec_2, label_1, label_2)

</pre></div>
