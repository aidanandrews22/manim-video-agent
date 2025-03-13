# Pendulum

Qualified name: `manim\_physics.rigid\_mechanics.pendulum.Pendulum`

### *class* Pendulum(length=3.5, initial_theta=0.3, pivot_point=array([0., 2., 0.]), rod_style={}, bob_style={'color': ManimColor('#FF862F'), 'fill_opacity': 1, 'radius': 0.25}, \*\*kwargs)

Bases: [`MultiPendulum`](manim_physics.rigid_mechanics.pendulum.MultiPendulum.md#manim_physics.rigid_mechanics.pendulum.MultiPendulum)

A pendulum.

* **Parameters:**
  * **length** – The length of the pendulum.
  * **initial_theta** – The initial angle of deviation.
  * **rod_style** – Parameters for `Line`.
  * **bob_style** – Parameters for `Circle`.
  * **kwargs** – Additional parameters for `VGroup`.

### Examples

<div id="pendulumexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PendulumExample <a class="headerlink" href="#pendulumexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./PendulumExample-1.mp4">
</video>
```python
from manim import *

from manim_physics import *
class PendulumExample(SpaceScene):
    def construct(self):
        pends = VGroup(*[Pendulum(i) for i in np.linspace(1, 5, 7)])
        self.add(pends)
        for p in pends:
            self.make_rigid_body(*p.bobs)
            p.start_swinging()
        self.wait(10)
```

<pre data-manim-binder data-manim-classname="PendulumExample">
from manim_physics import \*
class PendulumExample(SpaceScene):
    def construct(self):
        pends = VGroup(\*[Pendulum(i) for i in np.linspace(1, 5, 7)])
        self.add(pends)
        for p in pends:
            self.make_rigid_body(\*p.bobs)
            p.start_swinging()
        self.wait(10)

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
