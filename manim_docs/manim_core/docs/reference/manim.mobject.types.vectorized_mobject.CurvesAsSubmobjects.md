# CurvesAsSubmobjects

Qualified name: `manim.mobject.types.vectorized\_mobject.CurvesAsSubmobjects`

### *class* CurvesAsSubmobjects(vmobject, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

Convert a curve’s elements to submobjects.

### Examples

<div id="linegradientexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LineGradientExample <a class="headerlink" href="#linegradientexample">¶</a></p>![image](media/images/LineGradientExample-1.png)
```python
from manim import *

class LineGradientExample(Scene):
    def construct(self):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)
        new_curve.set_color_by_gradient(BLUE, RED)
        self.add(new_curve.shift(UP), curve)
```

<pre data-manim-binder data-manim-classname="LineGradientExample">
class LineGradientExample(Scene):
    def construct(self):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)
        new_curve.set_color_by_gradient(BLUE, RED)
        self.add(new_curve.shift(UP), curve)

</pre></div>

### Methods

| [`point_from_proportion`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion)   | Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).   |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

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
* **Parameters:**
  **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))

#### \_original_\_init_\_(vmobject, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
* **Return type:**
  None

#### point_from_proportion(alpha)

Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).

* **Parameters:**
  **alpha** (*float*) – The proportion along the the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).
* **Returns:**
  The point on the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).
* **Return type:**
  `numpy.ndarray`
* **Raises:**
  * **ValueError** – If `alpha` is not between 0 and 1.
  * **Exception** – If the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects) has no submobjects, or no submobject has points.
