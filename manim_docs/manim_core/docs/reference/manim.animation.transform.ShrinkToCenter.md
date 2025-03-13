# ShrinkToCenter

Qualified name: `manim.animation.transform.ShrinkToCenter`

### *class* ShrinkToCenter(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ScaleInPlace`](manim.animation.transform.ScaleInPlace.md#manim.animation.transform.ScaleInPlace)

Animation that makes a mobject shrink to center.

### Examples

<div id="shrinktocenterexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShrinkToCenterExample <a class="headerlink" href="#shrinktocenterexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ShrinkToCenterExample-1.mp4">
</video>
```python
from manim import *

class ShrinkToCenterExample(Scene):
    def construct(self):
        self.play(ShrinkToCenter(Text("Hello World!")))
```

<pre data-manim-binder data-manim-classname="ShrinkToCenterExample">
class ShrinkToCenterExample(Scene):
    def construct(self):
        self.play(ShrinkToCenter(Text("Hello World!")))

</pre></div>

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |
* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))

#### \_original_\_init_\_(mobject, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
* **Return type:**
  None
