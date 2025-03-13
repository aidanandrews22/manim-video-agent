# Circle

Qualified name: `manim.mobject.geometry.arc.Circle`

### *class* Circle(radius=None, color=ManimColor('#FC6255'), \*\*kwargs)

Bases: [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)

A circle.

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the shape.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)
  * **radius** (*float* *|* *None*)

### Examples

<div id="circleexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CircleExample <a class="headerlink" href="#circleexample">¶</a></p>![image](media/images/CircleExample-1.png)
```python
from manim import *

class CircleExample(Scene):
    def construct(self):
        circle_1 = Circle(radius=1.0)
        circle_2 = Circle(radius=1.5, color=GREEN)
        circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)

        circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
        self.add(circle_group)
```

<pre data-manim-binder data-manim-classname="CircleExample">
class CircleExample(Scene):
    def construct(self):
        circle_1 = Circle(radius=1.0)
        circle_2 = Circle(radius=1.5, color=GREEN)
        circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)

        circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
        self.add(circle_group)

</pre></div>

### Methods

| [`from_three_points`](#manim.mobject.geometry.arc.Circle.from_three_points)   | Returns a circle passing through the specified three points.   |
|-------------------------------------------------------------------------------|----------------------------------------------------------------|
| [`point_at_angle`](#manim.mobject.geometry.arc.Circle.point_at_angle)         | Returns the position of a point on the circle.                 |
| [`surround`](#manim.mobject.geometry.arc.Circle.surround)                     | Modifies a circle so that it surrounds a given mobject.        |

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

#### \_original_\_init_\_(radius=None, color=ManimColor('#FC6255'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **radius** (*float* *|* *None*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)
* **Return type:**
  None

#### *static* from_three_points(p1, p2, p3, \*\*kwargs)

Returns a circle passing through the specified
three points.

### Example

<div id="circlefrompointsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CircleFromPointsExample <a class="headerlink" href="#circlefrompointsexample">¶</a></p>![image](media/images/CircleFromPointsExample-1.png)
```python
from manim import *

class CircleFromPointsExample(Scene):
    def construct(self):
        circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
        dots = VGroup(
            Dot(LEFT),
            Dot(LEFT + UP),
            Dot(UP * 2),
        )
        self.add(NumberPlane(), circle, dots)
```

<pre data-manim-binder data-manim-classname="CircleFromPointsExample">
class CircleFromPointsExample(Scene):
    def construct(self):
        circle = Circle.from_three_points(LEFT, LEFT + UP, UP \* 2, color=RED)
        dots = VGroup(
            Dot(LEFT),
            Dot(LEFT + UP),
            Dot(UP \* 2),
        )
        self.add(NumberPlane(), circle, dots)

</pre></div>
* **Parameters:**
  * **p1** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **p2** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **p3** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **kwargs** (*Any*)
* **Return type:**
  [Circle](#manim.mobject.geometry.arc.Circle)

#### point_at_angle(angle)

Returns the position of a point on the circle.

* **Parameters:**
  **angle** (*float*) – The angle of the point along the circle in radians.
* **Returns:**
  The location of the point along the circle’s circumference.
* **Return type:**
  `numpy.ndarray`

### Examples

<div id="pointatangleexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PointAtAngleExample <a class="headerlink" href="#pointatangleexample">¶</a></p>![image](media/images/PointAtAngleExample-1.png)
```python
from manim import *

class PointAtAngleExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        p1 = circle.point_at_angle(PI/2)
        p2 = circle.point_at_angle(270*DEGREES)

        s1 = Square(side_length=0.25).move_to(p1)
        s2 = Square(side_length=0.25).move_to(p2)
        self.add(circle, s1, s2)
```

<pre data-manim-binder data-manim-classname="PointAtAngleExample">
class PointAtAngleExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        p1 = circle.point_at_angle(PI/2)
        p2 = circle.point_at_angle(270\*DEGREES)

        s1 = Square(side_length=0.25).move_to(p1)
        s2 = Square(side_length=0.25).move_to(p2)
        self.add(circle, s1, s2)

</pre></div>

#### surround(mobject, dim_to_match=0, stretch=False, buffer_factor=1.2)

Modifies a circle so that it surrounds a given mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject that the circle will be surrounding.
  * **dim_to_match** (*int*)
  * **buffer_factor** (*float*) – Scales the circle with respect to the mobject. A buffer_factor < 1 makes the circle smaller than the mobject.
  * **stretch** (*bool*) – Stretches the circle to fit more tightly around the mobject. Note: Does not work with `Line`
* **Return type:**
  Self

### Examples

<div id="circlesurround" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CircleSurround <a class="headerlink" href="#circlesurround">¶</a></p>![image](media/images/CircleSurround-1.png)
```python
from manim import *

class CircleSurround(Scene):
    def construct(self):
        triangle1 = Triangle()
        circle1 = Circle().surround(triangle1)
        group1 = Group(triangle1,circle1) # treat the two mobjects as one

        line2 = Line()
        circle2 = Circle().surround(line2, buffer_factor=2.0)
        group2 = Group(line2,circle2)

        # buffer_factor < 1, so the circle is smaller than the square
        square3 = Square()
        circle3 = Circle().surround(square3, buffer_factor=0.5)
        group3 = Group(square3, circle3)

        group = Group(group1, group2, group3).arrange(buff=1)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="CircleSurround">
class CircleSurround(Scene):
    def construct(self):
        triangle1 = Triangle()
        circle1 = Circle().surround(triangle1)
        group1 = Group(triangle1,circle1) # treat the two mobjects as one

        line2 = Line()
        circle2 = Circle().surround(line2, buffer_factor=2.0)
        group2 = Group(line2,circle2)

        # buffer_factor < 1, so the circle is smaller than the square
        square3 = Square()
        circle3 = Circle().surround(square3, buffer_factor=0.5)
        group3 = Group(square3, circle3)

        group = Group(group1, group2, group3).arrange(buff=1)
        self.add(group)

</pre></div>
