# Tetrahedron

Qualified name: `manim.mobject.three\_d.polyhedra.Tetrahedron`

### *class* Tetrahedron(edge_length=1, \*\*kwargs)

Bases: [`Polyhedron`](manim.mobject.three_d.polyhedra.Polyhedron.md#manim.mobject.three_d.polyhedra.Polyhedron)

A tetrahedron, one of the five platonic solids. It has 4 faces, 6 edges, and 4 vertices.

* **Parameters:**
  **edge_length** (*float*) – The length of an edge between any two vertices.

### Examples

<div id="tetrahedronscene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TetrahedronScene <a class="headerlink" href="#tetrahedronscene">¶</a></p>![image](media/images/TetrahedronScene-1.png)
```python
from manim import *

class TetrahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Tetrahedron()
        self.add(obj)
```

<pre data-manim-binder data-manim-classname="TetrahedronScene">
class TetrahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 \* DEGREES, theta=30 \* DEGREES)
        obj = Tetrahedron()
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
