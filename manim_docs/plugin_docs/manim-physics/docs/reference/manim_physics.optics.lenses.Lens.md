# Lens

Qualified name: `manim\_physics.optics.lenses.Lens`

### *class* Lens(f, d, n=1.52, \*\*kwargs)

Bases: `VMobject`

A lens. Commonly used with `Ray` .

* **Parameters:**
  * **f** (*float*) – Focal length. This does not correspond correctly
    to the point of focus (Known issue). Positive f
    returns a convex lens, negative for concave.
  * **d** (*float*) – Lens thickness
  * **n** (*float*) – Refractive index. By default, glass.
  * **kwargs** – Additional parameters to be passed to `VMobject` .

### Methods

### Attributes

| [`C`](#manim_physics.optics.lenses.Lens.C)   | Returns a tuple of two points corresponding to the centers of curvature.   |
|----------------------------------------------|----------------------------------------------------------------------------|
| `animate`                                    | Used to animate the application of any method of `self`.                   |
| `animation_overrides`                        |                                                                            |
| `color`                                      |                                                                            |
| `depth`                                      | The depth of the mobject.                                                  |
| `fill_color`                                 | If there are multiple colors (for gradient) this returns the first one     |
| `height`                                     | The height of the mobject.                                                 |
| `n_points_per_curve`                         |                                                                            |
| `sheen_factor`                               |                                                                            |
| `stroke_color`                               |                                                                            |
| `width`                                      | The width of the mobject.                                                  |

#### *property* C *: Tuple[Iterable[float]]*

Returns a tuple of two points corresponding to the centers of curvature.
