# Restore

Qualified name: `manim.animation.transform.Restore`

### *class* Restore(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.md#manim.animation.transform.ApplyMethod)

Transforms a mobject to its last saved state.

To save the state of a mobject, use the [`save_state()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.save_state) method.

### Examples

<div id="restoreexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RestoreExample <a class="headerlink" href="#restoreexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./RestoreExample-1.mp4">
</video>
```python
from manim import *

class RestoreExample(Scene):
    def construct(self):
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)
```

<pre data-manim-binder data-manim-classname="RestoreExample">
class RestoreExample(Scene):
    def construct(self):
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2\*LEFT).scale(3))
        self.play(s.animate.shift(5\*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)

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
