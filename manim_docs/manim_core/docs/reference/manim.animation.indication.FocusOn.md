# FocusOn

Qualified name: `manim.animation.indication.FocusOn`

### *class* FocusOn(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Shrink a spotlight to a position.

* **Parameters:**
  * **focus_point** (*np.ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The point at which to shrink the spotlight. If it is a `Mobject` its center will be used.
  * **opacity** (*float*) – The opacity of the spotlight.
  * **color** (*str*) – The color of the spotlight.
  * **run_time** (*float*) – The duration of the animation.

### Examples

<div id="usingfocuson" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UsingFocusOn <a class="headerlink" href="#usingfocuson">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UsingFocusOn-1.mp4">
</video>
```python
from manim import *

class UsingFocusOn(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(DOWN)
        self.add(Tex("Focusing on the dot below:"), dot)
        self.play(FocusOn(dot))
        self.wait()
```

<pre data-manim-binder data-manim-classname="UsingFocusOn">
class UsingFocusOn(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(DOWN)
        self.add(Tex("Focusing on the dot below:"), dot)
        self.play(FocusOn(dot))
        self.wait()

</pre></div>

### Methods

| `create_target`   |    |
|-------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(focus_point, opacity=0.2, color=ManimColor('#888888'), run_time=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **focus_point** (*ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **opacity** (*float*)
  * **color** (*str*)
  * **run_time** (*float*)
* **Return type:**
  None
