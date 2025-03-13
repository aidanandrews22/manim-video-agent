# Ray

Qualified name: `manim\_physics.optics.rays.Ray`

### *class* Ray(start, direction, init_length=5, propagate=None, \*\*kwargs)

Bases: `Line`

A light ray.

* **Parameters:**
  * **start** (*Iterable* *[**float* *]*) – The start point of the ray
  * **direction** (*Iterable* *[**float* *]*) – The direction of the ray
  * **init_length** (*float*) – The initial length of the ray. Once propagated,
    the length are lengthened to showcase lensing.
  * **propagate** (*Iterable* *[*[*Lens*](manim_physics.optics.lenses.Lens.md#manim_physics.optics.lenses.Lens) *]*  *|* *None*) – A list of lenses to propagate through.

### Example

<div id="rayexamplescene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RayExampleScene <a class="headerlink" href="#rayexamplescene">¶</a></p>![image](media/images/RayExampleScene-1.png)
```python
from manim import *

from manim_physics import *

class RayExampleScene(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        a = Lens(-5, 1, **lens_style).shift(LEFT)
        a2 = Lens(5, 1, **lens_style).shift(RIGHT)
        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [a, a2], color=RED)
            for i in np.linspace(-2, 2, 10)
        ]
        self.add(a, a2, *b)
```

<pre data-manim-binder data-manim-classname="RayExampleScene">
from manim_physics import \*

class RayExampleScene(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        a = Lens(-5, 1, \*\*lens_style).shift(LEFT)
        a2 = Lens(5, 1, \*\*lens_style).shift(RIGHT)
        b = [
            Ray(LEFT \* 5 + UP \* i, RIGHT, 8, [a, a2], color=RED)
            for i in np.linspace(-2, 2, 10)
        ]
        self.add(a, a2, \*b)

</pre></div>

### Methods

| [`propagate`](#manim_physics.optics.rays.Ray.propagate)   | Let the ray propagate through the list of lenses passed.   |
|-----------------------------------------------------------|------------------------------------------------------------|

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

#### propagate(\*lenses)

Let the ray propagate through the list
of lenses passed.

* **Parameters:**
  **lenses** ([*Lens*](manim_physics.optics.lenses.Lens.md#manim_physics.optics.lenses.Lens)) – All the lenses for the ray to propagate through
* **Return type:**
  None
