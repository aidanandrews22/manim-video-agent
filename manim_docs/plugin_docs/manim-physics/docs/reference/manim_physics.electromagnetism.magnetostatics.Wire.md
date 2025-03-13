# Wire

Qualified name: `manim\_physics.electromagnetism.magnetostatics.Wire`

### *class* Wire(stroke, current=1, samples=16, \*\*kwargs)

Bases: `VMobject`

An abstract class denoting a current carrying wire to produce a
[`MagneticField`](manim_physics.electromagnetism.magnetostatics.MagneticField.md#manim_physics.electromagnetism.magnetostatics.MagneticField).

* **Parameters:**
  * **stroke** (*VMobject*) – The original wire `VMobject`. The resulting wire takes its form.
  * **current** (*float*) – The magnitude of current flowing in the wire.
  * **samples** (*int*) – The number of segments of the wire used to create the
    [`MagneticField`](manim_physics.electromagnetism.magnetostatics.MagneticField.md#manim_physics.electromagnetism.magnetostatics.MagneticField).
  * **kwargs** – Additional parameters passed to `VMobject`.

#### NOTE
See [`MagneticField`](manim_physics.electromagnetism.magnetostatics.MagneticField.md#manim_physics.electromagnetism.magnetostatics.MagneticField) for examples.

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
