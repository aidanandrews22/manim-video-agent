# ClockwiseTransform

Qualified name: `manim.animation.transform.ClockwiseTransform`

### *class* ClockwiseTransform(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Transforms the points of a mobject along a clockwise oriented arc.

#### SEE ALSO
[`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform), [`CounterclockwiseTransform`](manim.animation.transform.CounterclockwiseTransform.md#manim.animation.transform.CounterclockwiseTransform)

### Examples

<div id="clockwiseexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ClockwiseExample <a class="headerlink" href="#clockwiseexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ClockwiseExample-1.mp4">
</video>
```python
from manim import *

class ClockwiseExample(Scene):
    def construct(self):
        dl, dr = Dot(), Dot()
        sl, sr = Square(), Square()

        VGroup(dl, sl).arrange(DOWN).shift(2*LEFT)
        VGroup(dr, sr).arrange(DOWN).shift(2*RIGHT)

        self.add(dl, dr)
        self.wait()
        self.play(
            ClockwiseTransform(dl, sl),
            Transform(dr, sr)
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="ClockwiseExample">
class ClockwiseExample(Scene):
    def construct(self):
        dl, dr = Dot(), Dot()
        sl, sr = Square(), Square()

        VGroup(dl, sl).arrange(DOWN).shift(2\*LEFT)
        VGroup(dr, sr).arrange(DOWN).shift(2\*RIGHT)

        self.add(dl, dr)
        self.wait()
        self.play(
            ClockwiseTransform(dl, sl),
            Transform(dr, sr)
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
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **path_arc** (*float*)

#### \_original_\_init_\_(mobject, target_mobject, path_arc=-3.141592653589793, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **path_arc** (*float*)
* **Return type:**
  None
