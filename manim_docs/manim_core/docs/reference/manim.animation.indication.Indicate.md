# Indicate

Qualified name: `manim.animation.indication.Indicate`

### *class* Indicate(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Indicate a Mobject by temporarily resizing and recoloring it.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to indicate.
  * **scale_factor** (*float*) – The factor by which the mobject will be temporally scaled
  * **color** (*str*) – The color the mobject temporally takes.
  * **rate_func** (*Callable* *[* *[**float* *,* *float* *|* *None* *]* *,* *np.ndarray* *]*) – The function defining the animation progress at every point in time.
  * **kwargs** – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.md#manim.animation.composition.Succession) constructor

### Examples

<div id="usingindicate" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UsingIndicate <a class="headerlink" href="#usingindicate">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UsingIndicate-1.mp4">
</video>
```python
from manim import *

class UsingIndicate(Scene):
    def construct(self):
        tex = Tex("Indicate").scale(3)
        self.play(Indicate(tex))
        self.wait()
```

<pre data-manim-binder data-manim-classname="UsingIndicate">
class UsingIndicate(Scene):
    def construct(self):
        tex = Tex("Indicate").scale(3)
        self.play(Indicate(tex))
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

#### \_original_\_init_\_(mobject, scale_factor=1.2, color=ManimColor('#FFFF00'), rate_func=<function there_and_back>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **scale_factor** (*float*)
  * **color** (*str*)
  * **rate_func** (*Callable* *[* *[**float* *,* *float* *|* *None* *]* *,* *ndarray* *]*)
* **Return type:**
  None
