# ScaleInPlace

Qualified name: `manim.animation.transform.ScaleInPlace`

### *class* ScaleInPlace(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.md#manim.animation.transform.ApplyMethod)

Animation that scales a mobject by a certain factor.

### Examples

<div id="scaleinplaceexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ScaleInPlaceExample <a class="headerlink" href="#scaleinplaceexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ScaleInPlaceExample-1.mp4">
</video>
```python
from manim import *

class ScaleInPlaceExample(Scene):
    def construct(self):
        self.play(ScaleInPlace(Text("Hello World!"), 2))
```

<pre data-manim-binder data-manim-classname="ScaleInPlaceExample">
class ScaleInPlaceExample(Scene):
    def construct(self):
        self.play(ScaleInPlace(Text("Hello World!"), 2))

</pre></div>

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |
* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **scale_factor** (*float*)

#### \_original_\_init_\_(mobject, scale_factor, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **scale_factor** (*float*)
* **Return type:**
  None
