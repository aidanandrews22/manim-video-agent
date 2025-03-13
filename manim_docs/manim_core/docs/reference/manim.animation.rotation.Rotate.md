# Rotate

Qualified name: `manim.animation.rotation.Rotate`

### *class* Rotate(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Animation that rotates a Mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be rotated.
  * **angle** (*float*) – The rotation angle.
  * **axis** (*np.ndarray*) – The rotation axis as a numpy vector.
  * **about_point** (*Sequence* *[**float* *]*  *|* *None*) – The rotation center.
  * **about_edge** (*Sequence* *[**float* *]*  *|* *None*) – If `about_point` is `None`, this argument specifies
    the direction of the bounding box point to be taken as
    the rotation center.

### Examples

<div id="usingrotate" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UsingRotate <a class="headerlink" href="#usingrotate">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UsingRotate-1.mp4">
</video>
```python
from manim import *

class UsingRotate(Scene):
    def construct(self):
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            )
```

<pre data-manim-binder data-manim-classname="UsingRotate">
class UsingRotate(Scene):
    def construct(self):
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP \* 2),
                angle=2\*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2\*PI, rate_func=linear),
            )

</pre></div>

### Methods

| `create_target`   |    |
|-------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, angle=3.141592653589793, axis=array([0., 0., 1.]), about_point=None, about_edge=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **angle** (*float*)
  * **axis** (*np.ndarray*)
  * **about_point** (*Sequence* *[**float* *]*  *|* *None*)
  * **about_edge** (*Sequence* *[**float* *]*  *|* *None*)
* **Return type:**
  None
