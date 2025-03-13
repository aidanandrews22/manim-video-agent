# MoveToTarget

Qualified name: `manim.animation.transform.MoveToTarget`

### *class* MoveToTarget(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Transforms a mobject to the mobject stored in its `target` attribute.

After calling the `generate_target()` method, the `target`
attribute of the mobject is populated with a copy of it. After modifying the attribute,
playing the [`MoveToTarget`](#manim.animation.transform.MoveToTarget) animation transforms the original mobject
into the modified one stored in the `target` attribute.

### Examples

<div id="movetotargetexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MoveToTargetExample <a class="headerlink" href="#movetotargetexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./MoveToTargetExample-1.mp4">
</video>
```python
from manim import *

class MoveToTargetExample(Scene):
    def construct(self):
        c = Circle()

        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT + UP).scale(0.5)

        self.add(c)
        self.play(MoveToTarget(c))
```

<pre data-manim-binder data-manim-classname="MoveToTargetExample">
class MoveToTargetExample(Scene):
    def construct(self):
        c = Circle()

        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2\*RIGHT + UP).scale(0.5)

        self.add(c)
        self.play(MoveToTarget(c))

</pre></div>

### Methods

| `check_validity_of_input`   |    |
|-----------------------------|----|

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
