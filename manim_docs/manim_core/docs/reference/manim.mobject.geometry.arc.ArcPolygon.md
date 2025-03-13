# ArcPolygon

Qualified name: `manim.mobject.geometry.arc.ArcPolygon`

### *class* ArcPolygon(\*vertices, angle=0.7853981633974483, radius=None, arc_config=None, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A generalized polygon allowing for points to be connected with arcs.

This version tries to stick close to the way `Polygon` is used. Points
can be passed to it directly which are used to generate the according arcs
(using [`ArcBetweenPoints`](manim.mobject.geometry.arc.ArcBetweenPoints.md#manim.mobject.geometry.arc.ArcBetweenPoints)). An angle or radius can be passed to it to
use across all arcs, but to configure arcs individually an `arc_config` list
has to be passed with the syntax explained below.

* **Parameters:**
  * **vertices** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – A list of vertices, start and end points for the arc segments.
  * **angle** (*float*) – The angle used for constructing the arcs. If no other parameters
    are set, this angle is used to construct all arcs.
  * **radius** (*float* *|* *None*) – The circle radius used to construct the arcs. If specified,
    overrides the specified `angle`.
  * **arc_config** (*list* *[**dict* *]*  *|* *None*) – When passing a `dict`, its content will be passed as keyword
    arguments to [`ArcBetweenPoints`](manim.mobject.geometry.arc.ArcBetweenPoints.md#manim.mobject.geometry.arc.ArcBetweenPoints). Otherwise, a list
    of dictionaries containing values that are passed as keyword
    arguments for every individual arc can be passed.
  * **kwargs** (*Any*) – Further keyword arguments that are passed to the constructor of
    [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

#### arcs

The arcs created from the input parameters:

```default
>>> from manim import ArcPolygon
>>> ap = ArcPolygon([0, 0, 0], [2, 0, 0], [0, 2, 0])
>>> ap.arcs
[ArcBetweenPoints, ArcBetweenPoints, ArcBetweenPoints]
```

* **Type:**
  `list`

#### NOTE
There is an alternative version ([`ArcPolygonFromArcs`](manim.mobject.geometry.arc.ArcPolygonFromArcs.md#manim.mobject.geometry.arc.ArcPolygonFromArcs)) that is instantiated
with pre-defined arcs.

#### SEE ALSO
[`ArcPolygonFromArcs`](manim.mobject.geometry.arc.ArcPolygonFromArcs.md#manim.mobject.geometry.arc.ArcPolygonFromArcs)

### Examples

<div id="severalarcpolygons" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SeveralArcPolygons <a class="headerlink" href="#severalarcpolygons">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./SeveralArcPolygons-1.mp4">
</video>
```python
from manim import *

class SeveralArcPolygons(Scene):
    def construct(self):
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
        ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                                    arc_config=[{'radius': 1.7, 'color': RED},
                                    {'angle': 20*DEGREES, 'color': BLUE},
                                    {'radius': 1}])
        ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        self.play(*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
        self.wait()
```

<pre data-manim-binder data-manim-classname="SeveralArcPolygons">
class SeveralArcPolygons(Scene):
    def construct(self):
        a = [0, 0, 0]
        b = [2, 0, 0]
        c = [0, 2, 0]
        ap1 = ArcPolygon(a, b, c, radius=2)
        ap2 = ArcPolygon(a, b, c, angle=45\*DEGREES)
        ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                                    arc_config=[{'radius': 1.7, 'color': RED},
                                    {'angle': 20\*DEGREES, 'color': BLUE},
                                    {'radius': 1}])
        ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        self.play(\*[Create(ap) for ap in [ap1, ap2, ap3, ap4]])
        self.wait()

</pre></div>

For further examples see [`ArcPolygonFromArcs`](manim.mobject.geometry.arc.ArcPolygonFromArcs.md#manim.mobject.geometry.arc.ArcPolygonFromArcs).

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

#### \_original_\_init_\_(\*vertices, angle=0.7853981633974483, radius=None, arc_config=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vertices** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **angle** (*float*)
  * **radius** (*float* *|* *None*)
  * **arc_config** (*list* *[**dict* *]*  *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
