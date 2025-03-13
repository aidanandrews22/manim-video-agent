# MultiPendulum

Qualified name: `manim\_physics.rigid\_mechanics.pendulum.MultiPendulum`

### *class* MultiPendulum(\*bobs, pivot_point=array([0., 2., 0.]), rod_style={}, bob_style={'color': ManimColor('#FF862F'), 'fill_opacity': 1, 'radius': 0.1}, \*\*kwargs)

Bases: `VGroup`

A multipendulum.

* **Parameters:**
  * **bobs** (*Iterable* *[**np.ndarray* *]*) – Positions of pendulum bobs.
  * **pivot_point** (*np.ndarray*) – Position of the pivot.
  * **rod_style** (*dict*) – Parameters for `Line`.
  * **bob_style** (*dict*) – Parameters for `Circle`.
  * **kwargs** – Additional parameters for `VGroup`.

### Examples

<div id="multipendulumexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MultiPendulumExample <a class="headerlink" href="#multipendulumexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./MultiPendulumExample-1.mp4">
</video>
```python
from manim import *

from manim_physics import *

class MultiPendulumExample(SpaceScene):
    def construct(self):
        p = MultiPendulum(RIGHT, LEFT)
        self.add(p)
        self.make_rigid_body(*p.bobs)
        p.start_swinging()
        self.add(TracedPath(p.bobs[-1].get_center, stroke_color=BLUE))
        self.wait(10)
```

<pre data-manim-binder data-manim-classname="MultiPendulumExample">
from manim_physics import \*

class MultiPendulumExample(SpaceScene):
    def construct(self):
        p = MultiPendulum(RIGHT, LEFT)
        self.add(p)
        self.make_rigid_body(\*p.bobs)
        p.start_swinging()
        self.add(TracedPath(p.bobs[-1].get_center, stroke_color=BLUE))
        self.wait(10)

</pre></div>

### Methods

| [`end_swinging`](#manim_physics.rigid_mechanics.pendulum.MultiPendulum.end_swinging)     | Stop swinging.   |
|------------------------------------------------------------------------------------------|------------------|
| [`start_swinging`](#manim_physics.rigid_mechanics.pendulum.MultiPendulum.start_swinging) | Start swinging.  |

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

#### end_swinging()

Stop swinging.

* **Return type:**
  None

#### start_swinging()

Start swinging.

* **Return type:**
  None
