# ElectricField

Qualified name: `manim\_physics.electromagnetism.electrostatics.ElectricField`

### *class* ElectricField(\*charges, \*\*kwargs)

Bases: `ArrowVectorField`

An electric field.

* **Parameters:**
  * **charges** ([*Charge*](manim_physics.electromagnetism.electrostatics.Charge.md#manim_physics.electromagnetism.electrostatics.Charge)) – The charges affecting the electric field.
  * **kwargs** – Additional parameters to be passed to `ArrowVectorField`.

### Examples

<div id="electricfieldexamplescene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ElectricFieldExampleScene <a class="headerlink" href="#electricfieldexamplescene">¶</a></p>![image](media/images/ElectricFieldExampleScene-1.png)
```python
from manim import *

from manim_physics import *

class ElectricFieldExampleScene(Scene):
    def construct(self):
        charge1 = Charge(-1, LEFT + DOWN)
        charge2 = Charge(2, RIGHT + DOWN)
        charge3 = Charge(-1, UP)
        field = ElectricField(charge1, charge2, charge3)
        self.add(charge1, charge2, charge3)
        self.add(field)
```

<pre data-manim-binder data-manim-classname="ElectricFieldExampleScene">
from manim_physics import \*

class ElectricFieldExampleScene(Scene):
    def construct(self):
        charge1 = Charge(-1, LEFT + DOWN)
        charge2 = Charge(2, RIGHT + DOWN)
        charge3 = Charge(-1, UP)
        field = ElectricField(charge1, charge2, charge3)
        self.add(charge1, charge2, charge3)
        self.add(field)

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
