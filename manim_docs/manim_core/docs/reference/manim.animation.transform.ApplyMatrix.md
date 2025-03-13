# ApplyMatrix

Qualified name: `manim.animation.transform.ApplyMatrix`

### *class* ApplyMatrix(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.md#manim.animation.transform.ApplyPointwiseFunction)

Applies a matrix transform to an mobject.

* **Parameters:**
  * **matrix** (*np.ndarray*) – The transformation matrix.
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **about_point** (*np.ndarray*) – The origin point for the transform. Defaults to `ORIGIN`.
  * **kwargs** – Further keyword arguments that are passed to [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.md#manim.animation.transform.ApplyPointwiseFunction).

### Examples

<div id="applymatrixexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ApplyMatrixExample <a class="headerlink" href="#applymatrixexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ApplyMatrixExample-1.mp4">
</video>
```python
from manim import *

class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))
```

<pre data-manim-binder data-manim-classname="ApplyMatrixExample">
class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))

</pre></div>

### Methods

| `initialize_matrix`   |    |
|-----------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(matrix, mobject, about_point=array([0., 0., 0.]), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **matrix** (*ndarray*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **about_point** (*ndarray*)
* **Return type:**
  None
