# FadeToColor

Qualified name: `manim.animation.transform.FadeToColor`

### *class* FadeToColor(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.md#manim.animation.transform.ApplyMethod)

Animation that changes color of a mobject.

### Examples

<div id="fadetocolorexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: FadeToColorExample <a class="headerlink" href="#fadetocolorexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./FadeToColorExample-1.mp4">
</video>
```python
from manim import *

class FadeToColorExample(Scene):
    def construct(self):
        self.play(FadeToColor(Text("Hello World!"), color=RED))
```

<pre data-manim-binder data-manim-classname="FadeToColorExample">
class FadeToColorExample(Scene):
    def construct(self):
        self.play(FadeToColor(Text("Hello World!"), color=RED))

</pre></div>

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |
* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **color** (*str*)

#### \_original_\_init_\_(mobject, color, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **color** (*str*)
* **Return type:**
  None
