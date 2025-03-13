# LabeledPolygram

Qualified name: `manim.mobject.geometry.labeled.LabeledPolygram`

### *class* LabeledPolygram(\*vertex_groups, label, precision=0.01, label_config=None, box_config=None, frame_config=None, \*\*kwargs)

Bases: [`Polygram`](manim.mobject.geometry.polygram.Polygram.md#manim.mobject.geometry.polygram.Polygram)

Constructs a polygram containing a label box at its pole of inaccessibility.

* **Parameters:**
  * **vertex_groups** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array)) – Vertices passed to the [`Polygram`](manim.mobject.geometry.polygram.Polygram.md#manim.mobject.geometry.polygram.Polygram) constructor.
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)) – Label that will be displayed on the Polygram.
  * **precision** (*float*) – The precision used by the PolyLabel algorithm.
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the label.
    This is only applied if `label` is of type `str`.
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the background box.
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – 

    A dictionary containing the configuration for the frame.

    #### NOTE
    The PolyLabel Algorithm expects each vertex group to form a closed ring.
    If the input is open, [`LabeledPolygram`](#manim.mobject.geometry.labeled.LabeledPolygram) will attempt to close it.
    This may cause the polygon to intersect itself leading to unexpected results.
  * **kwargs** (*Any*)

### Examples

<div id="labeledpolygramexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LabeledPolygramExample <a class="headerlink" href="#labeledpolygramexample">¶</a></p>![image](media/images/LabeledPolygramExample-1.png)
```python
from manim import *

class LabeledPolygramExample(Scene):
    def construct(self):
        # Define Rings
        ring1 = [
            [-3.8, -2.4, 0], [-2.4, -2.5, 0], [-1.3, -1.6, 0], [-0.2, -1.7, 0],
            [1.7, -2.5, 0], [2.9, -2.6, 0], [3.5, -1.5, 0], [4.9, -1.4, 0],
            [4.5, 0.2, 0], [4.7, 1.6, 0], [3.5, 2.4, 0], [1.1, 2.5, 0],
            [-0.1, 0.9, 0], [-1.2, 0.5, 0], [-1.6, 0.7, 0], [-1.4, 1.9, 0],
            [-2.6, 2.6, 0], [-4.4, 1.2, 0], [-4.9, -0.8, 0], [-3.8, -2.4, 0]
        ]
        ring2 = [
            [0.2, -1.2, 0], [0.9, -1.2, 0], [1.4, -2.0, 0], [2.1, -1.6, 0],
            [2.2, -0.5, 0], [1.4, 0.0, 0], [0.4, -0.2, 0], [0.2, -1.2, 0]
        ]
        ring3 = [[-2.7, 1.4, 0], [-2.3, 1.7, 0], [-2.8, 1.9, 0], [-2.7, 1.4, 0]]

        # Create Polygons (for reference)
        p1 = Polygon(*ring1, fill_opacity=0.75)
        p2 = Polygon(*ring2, fill_color=BLACK, fill_opacity=1)
        p3 = Polygon(*ring3, fill_color=BLACK, fill_opacity=1)

        # Create Labeled Polygram
        polygram = LabeledPolygram(
            *[ring1, ring2, ring3],
            label=Text('Pole', font='sans-serif'),
            precision=0.01,
        )

        # Display Circle (for reference)
        circle = Circle(radius=polygram.radius, color=WHITE).move_to(polygram.pole)

        self.add(p1, p2, p3)
        self.add(polygram)
        self.add(circle)
```

<pre data-manim-binder data-manim-classname="LabeledPolygramExample">
class LabeledPolygramExample(Scene):
    def construct(self):
        # Define Rings
        ring1 = [
            [-3.8, -2.4, 0], [-2.4, -2.5, 0], [-1.3, -1.6, 0], [-0.2, -1.7, 0],
            [1.7, -2.5, 0], [2.9, -2.6, 0], [3.5, -1.5, 0], [4.9, -1.4, 0],
            [4.5, 0.2, 0], [4.7, 1.6, 0], [3.5, 2.4, 0], [1.1, 2.5, 0],
            [-0.1, 0.9, 0], [-1.2, 0.5, 0], [-1.6, 0.7, 0], [-1.4, 1.9, 0],
            [-2.6, 2.6, 0], [-4.4, 1.2, 0], [-4.9, -0.8, 0], [-3.8, -2.4, 0]
        ]
        ring2 = [
            [0.2, -1.2, 0], [0.9, -1.2, 0], [1.4, -2.0, 0], [2.1, -1.6, 0],
            [2.2, -0.5, 0], [1.4, 0.0, 0], [0.4, -0.2, 0], [0.2, -1.2, 0]
        ]
        ring3 = [[-2.7, 1.4, 0], [-2.3, 1.7, 0], [-2.8, 1.9, 0], [-2.7, 1.4, 0]]

        # Create Polygons (for reference)
        p1 = Polygon(\*ring1, fill_opacity=0.75)
        p2 = Polygon(\*ring2, fill_color=BLACK, fill_opacity=1)
        p3 = Polygon(\*ring3, fill_color=BLACK, fill_opacity=1)

        # Create Labeled Polygram
        polygram = LabeledPolygram(
            \*[ring1, ring2, ring3],
            label=Text('Pole', font='sans-serif'),
            precision=0.01,
        )

        # Display Circle (for reference)
        circle = Circle(radius=polygram.radius, color=WHITE).move_to(polygram.pole)

        self.add(p1, p2, p3)
        self.add(polygram)
        self.add(circle)

</pre></div><div id="labeledcountryexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LabeledCountryExample <a class="headerlink" href="#labeledcountryexample">¶</a></p>![image](media/images/LabeledCountryExample-1.png)
```python
from manim import *

import requests
import json

class LabeledCountryExample(Scene):
    def construct(self):
        # Fetch JSON data and process arcs
        data = requests.get('https://cdn.jsdelivr.net/npm/us-atlas@3/nation-10m.json').json()
        arcs, transform = data['arcs'], data['transform']
        sarcs = [np.cumsum(arc, axis=0) * transform['scale'] + transform['translate'] for arc in arcs]
        ssarcs = sorted(sarcs, key=len, reverse=True)[:1]

        # Compute Bounding Box
        points = np.concatenate(ssarcs)
        mins, maxs = np.min(points, axis=0), np.max(points, axis=0)

        # Build Axes
        ax = Axes(
            x_range=[mins[0], maxs[0], maxs[0] - mins[0]], x_length=10,
            y_range=[mins[1], maxs[1], maxs[1] - mins[1]], y_length=7,
            tips=False
        )

        # Adjust Coordinates
        array = [[ax.c2p(*point) for point in sarc] for sarc in ssarcs]

        # Add Polygram
        polygram = LabeledPolygram(
            *array,
            label=Text('USA', font='sans-serif'),
            precision=0.01,
            fill_color=BLUE,
            stroke_width=0,
            fill_opacity=0.75
        )

        # Display Circle (for reference)
        circle = Circle(radius=polygram.radius, color=WHITE).move_to(polygram.pole)

        self.add(ax)
        self.add(polygram)
        self.add(circle)
```

<pre data-manim-binder data-manim-classname="LabeledCountryExample">
import requests
import json

class LabeledCountryExample(Scene):
    def construct(self):
        # Fetch JSON data and process arcs
        data = requests.get('https://cdn.jsdelivr.net/npm/us-atlas@3/nation-10m.json').json()
        arcs, transform = data['arcs'], data['transform']
        sarcs = [np.cumsum(arc, axis=0) \* transform['scale'] + transform['translate'] for arc in arcs]
        ssarcs = sorted(sarcs, key=len, reverse=True)[:1]

        # Compute Bounding Box
        points = np.concatenate(ssarcs)
        mins, maxs = np.min(points, axis=0), np.max(points, axis=0)

        # Build Axes
        ax = Axes(
            x_range=[mins[0], maxs[0], maxs[0] - mins[0]], x_length=10,
            y_range=[mins[1], maxs[1], maxs[1] - mins[1]], y_length=7,
            tips=False
        )

        # Adjust Coordinates
        array = [[ax.c2p(\*point) for point in sarc] for sarc in ssarcs]

        # Add Polygram
        polygram = LabeledPolygram(
            \*array,
            label=Text('USA', font='sans-serif'),
            precision=0.01,
            fill_color=BLUE,
            stroke_width=0,
            fill_opacity=0.75
        )

        # Display Circle (for reference)
        circle = Circle(radius=polygram.radius, color=WHITE).move_to(polygram.pole)

        self.add(ax)
        self.add(polygram)
        self.add(circle)

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

#### \_original_\_init_\_(\*vertex_groups, label, precision=0.01, label_config=None, box_config=None, frame_config=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vertex_groups** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **precision** (*float*)
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
