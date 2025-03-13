# PGroup

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PGroup`

### *class* PGroup(\*pmobs, \*\*kwargs)

Bases: [`PMobject`](manim.mobject.types.point_cloud_mobject.PMobject.md#manim.mobject.types.point_cloud_mobject.PMobject)

A group for several point mobjects.

### Examples

<div id="pgroupexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PgroupExample <a class="headerlink" href="#pgroupexample">¶</a></p>![image](media/images/PgroupExample-1.png)
```python
from manim import *

class PgroupExample(Scene):
    def construct(self):

        p1 = PointCloudDot(radius=1, density=20, color=BLUE)
        p1.move_to(4.5 * LEFT)
        p2 = PointCloudDot()
        p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
        p3.move_to(4.5 * RIGHT)
        pList = PGroup(p1, p2, p3)

        self.add(pList)
```

<pre data-manim-binder data-manim-classname="PgroupExample">
class PgroupExample(Scene):
    def construct(self):

        p1 = PointCloudDot(radius=1, density=20, color=BLUE)
        p1.move_to(4.5 \* LEFT)
        p2 = PointCloudDot()
        p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
        p3.move_to(4.5 \* RIGHT)
        pList = PGroup(p1, p2, p3)

        self.add(pList)

</pre></div>

### Methods

| `fade_to`   |    |
|-------------|----|

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |
* **Parameters:**
  * **pmobs** (*Any*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(\*pmobs, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **pmobs** (*Any*)
  * **kwargs** (*Any*)
* **Return type:**
  None
