# Line

Qualified name: `manim.mobject.geometry.line.Line`

### *class* Line(start=array([-1., 0., 0.]), end=array([1., 0., 0.]), buff=0, path_arc=None, \*\*kwargs)

Bases: [`TipableVMobject`](manim.mobject.geometry.arc.TipableVMobject.md#manim.mobject.geometry.arc.TipableVMobject)

### Methods

| [`generate_points`](#manim.mobject.geometry.line.Line.generate_points)           | Initializes `points` and therefore the shape.                  |
|----------------------------------------------------------------------------------|----------------------------------------------------------------|
| `get_angle`                                                                      |                                                                |
| [`get_projection`](#manim.mobject.geometry.line.Line.get_projection)             | Returns the projection of a point onto a line.                 |
| `get_slope`                                                                      |                                                                |
| `get_unit_vector`                                                                |                                                                |
| `get_vector`                                                                     |                                                                |
| [`init_points`](#manim.mobject.geometry.line.Line.init_points)                   | Initializes `points` and therefore the shape.                  |
| [`put_start_and_end_on`](#manim.mobject.geometry.line.Line.put_start_and_end_on) | Sets starts and end coordinates of a line.                     |
| `set_angle`                                                                      |                                                                |
| `set_length`                                                                     |                                                                |
| `set_path_arc`                                                                   |                                                                |
| [`set_points_by_ends`](#manim.mobject.geometry.line.Line.set_points_by_ends)     | Sets the points of the line based on its start and end points. |

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
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **buff** (*float*)
  * **path_arc** (*float* *|* *None*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(start=array([-1., 0., 0.]), end=array([1., 0., 0.]), buff=0, path_arc=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **buff** (*float*)
  * **path_arc** (*float* *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### \_pointify(mob_or_point, direction=None)

Transforms a mobject into its corresponding point. Does nothing if a point is passed.

`direction` determines the location of the point along its bounding box in that direction.

* **Parameters:**
  * **mob_or_point** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The mobject or point.
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D) *|* *None*) – The direction.
* **Return type:**
  [Point3D](manim.typing.md#manim.typing.Point3D)

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None

#### get_projection(point)

Returns the projection of a point onto a line.

* **Parameters:**
  **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The point to which the line is projected.
* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### init_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None

#### put_start_and_end_on(start, end)

Sets starts and end coordinates of a line.

### Examples

<div id="lineexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LineExample <a class="headerlink" href="#lineexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./LineExample-1.mp4">
</video>
```python
from manim import *

class LineExample(Scene):
    def construct(self):
        d = VGroup()
        for i in range(0,10):
            d.add(Dot())
        d.arrange_in_grid(buff=1)
        self.add(d)
        l= Line(d[0], d[1])
        self.add(l)
        self.wait()
        l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
        self.wait()
        l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
        self.wait()
```

<pre data-manim-binder data-manim-classname="LineExample">
class LineExample(Scene):
    def construct(self):
        d = VGroup()
        for i in range(0,10):
            d.add(Dot())
        d.arrange_in_grid(buff=1)
        self.add(d)
        l= Line(d[0], d[1])
        self.add(l)
        self.wait()
        l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
        self.wait()
        l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
        self.wait()

</pre></div>
* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
* **Return type:**
  Self

#### set_points_by_ends(start, end, buff=0, path_arc=0)

Sets the points of the line based on its start and end points.
Unlike [`put_start_and_end_on()`](#manim.mobject.geometry.line.Line.put_start_and_end_on), this method respects self.buff and
Mobject bounding boxes.

* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The start point or Mobject of the line.
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The end point or Mobject of the line.
  * **buff** (*float*) – The empty space between the start and end of the line, by default 0.
  * **path_arc** (*float*) – The angle of a circle spanned by this arc, by default 0 which is a straight line.
* **Return type:**
  None
