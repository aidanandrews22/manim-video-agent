# Dodecahedron

Qualified name: `manim.mobject.three\_d.polyhedra.Dodecahedron`

### *class* Dodecahedron(edge_length=1, \*\*kwargs)

Bases: [`Polyhedron`](manim.mobject.three_d.polyhedra.Polyhedron.md#manim.mobject.three_d.polyhedra.Polyhedron)

A dodecahedron, one of the five platonic solids. It has 12 faces, 30 edges and 20 vertices.

* **Parameters:**
  **edge_length** (*float*) – The length of an edge between any two vertices.

### Examples

<div id="dodecahedronscene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DodecahedronScene <a class="headerlink" href="#dodecahedronscene">¶</a></p>![image](media/images/DodecahedronScene-1.png)
```python
from manim import *

class DodecahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Dodecahedron()
        self.add(obj)
```

<pre data-manim-binder data-manim-classname="DodecahedronScene">
class DodecahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 \* DEGREES, theta=30 \* DEGREES)
        obj = Dodecahedron()
        self.add(obj)

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

#### \_original_\_init_\_(edge_length=1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **edge_length** (*float*)
