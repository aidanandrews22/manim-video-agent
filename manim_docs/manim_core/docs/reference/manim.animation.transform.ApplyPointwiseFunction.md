# ApplyPointwiseFunction

Qualified name: `manim.animation.transform.ApplyPointwiseFunction`

### *class* ApplyPointwiseFunction(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.md#manim.animation.transform.ApplyMethod)

Animation that applies a pointwise function to a mobject.

### Examples

<div id="warpsquare" class="admonition admonition-manim-example">
<p class="admonition-title">Example: WarpSquare <a class="headerlink" href="#warpsquare">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./WarpSquare-1.mp4">
</video>
```python
from manim import *

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="WarpSquare">
class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()

</pre></div>

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |
* **Parameters:**
  * **function** (*types.MethodType*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **run_time** (*float*)

#### \_original_\_init_\_(function, mobject, run_time=3.0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **function** (*MethodType*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **run_time** (*float*)
* **Return type:**
  None
