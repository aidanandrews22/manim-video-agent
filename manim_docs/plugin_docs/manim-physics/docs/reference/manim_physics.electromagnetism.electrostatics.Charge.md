# Charge

Qualified name: `manim\_physics.electromagnetism.electrostatics.Charge`

### *class* Charge(magnitude=1, point=array([0., 0., 0.]), add_glow=True, \*\*kwargs)

Bases: `VGroup`

An electrostatic charge object to produce an [`ElectricField`](manim_physics.electromagnetism.electrostatics.ElectricField.md#manim_physics.electromagnetism.electrostatics.ElectricField).

* **Parameters:**
  * **magnitude** (*float*) – The strength of the electrostatic charge.
  * **point** (*np.ndarray*) – The position of the charge.
  * **add_glow** (*bool*) – Whether to add a glowing effect. Adds rings of
    varying opacities to simulate glowing effect.
  * **kwargs** – Additional parameters to be passed to `VGroup`.

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
