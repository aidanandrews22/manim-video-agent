# Sector

Qualified name: `manim.mobject.geometry.arc.Sector`

### *class* Sector(radius=1, \*\*kwargs)

Bases: [`AnnularSector`](manim.mobject.geometry.arc.AnnularSector.md#manim.mobject.geometry.arc.AnnularSector)

A sector of a circle.

### Examples

<div id="examplesector" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ExampleSector <a class="headerlink" href="#examplesector">¶</a></p>![image](media/images/ExampleSector-1.png)
```python
from manim import *

class ExampleSector(Scene):
    def construct(self):
        sector = Sector(radius=2)
        sector2 = Sector(radius=2.5, angle=60*DEGREES).move_to([-3, 0, 0])
        sector.set_color(RED)
        sector2.set_color(PINK)
        self.add(sector, sector2)
```

<pre data-manim-binder data-manim-classname="ExampleSector">
class ExampleSector(Scene):
    def construct(self):
        sector = Sector(radius=2)
        sector2 = Sector(radius=2.5, angle=60\*DEGREES).move_to([-3, 0, 0])
        sector.set_color(RED)
        sector2.set_color(PINK)
        self.add(sector, sector2)

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
* **Parameters:**
  * **radius** (*float*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(radius=1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **radius** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
