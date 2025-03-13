# PointCloudDot

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PointCloudDot`

### *class* PointCloudDot(center=array([0., 0., 0.]), radius=2.0, stroke_width=2, density=10, color=ManimColor('#FFFF00'), \*\*kwargs)

Bases: [`Mobject1D`](manim.mobject.types.point_cloud_mobject.Mobject1D.md#manim.mobject.types.point_cloud_mobject.Mobject1D)

A disc made of a cloud of dots.

### Examples

<div id="pointclouddotexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PointCloudDotExample <a class="headerlink" href="#pointclouddotexample">¶</a></p>![image](media/images/PointCloudDotExample-1.png)
```python
from manim import *

class PointCloudDotExample(Scene):
    def construct(self):
        cloud_1 = PointCloudDot(color=RED)
        cloud_2 = PointCloudDot(stroke_width=4, radius=1)
        cloud_3 = PointCloudDot(density=15)

        group = Group(cloud_1, cloud_2, cloud_3).arrange()
        self.add(group)
```

<pre data-manim-binder data-manim-classname="PointCloudDotExample">
class PointCloudDotExample(Scene):
    def construct(self):
        cloud_1 = PointCloudDot(color=RED)
        cloud_2 = PointCloudDot(stroke_width=4, radius=1)
        cloud_3 = PointCloudDot(density=15)

        group = Group(cloud_1, cloud_2, cloud_3).arrange()
        self.add(group)

</pre></div><div id="pointclouddotexample2" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PointCloudDotExample2 <a class="headerlink" href="#pointclouddotexample2">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./PointCloudDotExample2-1.mp4">
</video>
```python
from manim import *

class PointCloudDotExample2(Scene):
    def construct(self):
        plane = ComplexPlane()
        cloud = PointCloudDot(color=RED)
        self.add(
            plane, cloud
        )
        self.wait()
        self.play(
            cloud.animate.apply_complex_function(lambda z: np.exp(z))
        )
```

<pre data-manim-binder data-manim-classname="PointCloudDotExample2">
class PointCloudDotExample2(Scene):
    def construct(self):
        plane = ComplexPlane()
        cloud = PointCloudDot(color=RED)
        self.add(
            plane, cloud
        )
        self.wait()
        self.play(
            cloud.animate.apply_complex_function(lambda z: np.exp(z))
        )

</pre></div>

### Methods

| [`generate_points`](#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points)   | Initializes `points` and therefore the shape.   |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| `init_points`                                                                                 |                                                 |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |
* **Parameters:**
  * **center** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D))
  * **radius** (*float*)
  * **stroke_width** (*int*)
  * **density** (*int*)
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(center=array([0., 0., 0.]), radius=2.0, stroke_width=2, density=10, color=ManimColor('#FFFF00'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **center** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D))
  * **radius** (*float*)
  * **stroke_width** (*int*)
  * **density** (*int*)
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **kwargs** (*Any*)
* **Return type:**
  None

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None
