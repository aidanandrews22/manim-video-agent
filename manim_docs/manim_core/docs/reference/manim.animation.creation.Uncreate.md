# Uncreate

Qualified name: `manim.animation.creation.Uncreate`

### *class* Uncreate(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Create`](manim.animation.creation.Create.md#manim.animation.creation.Create)

Like [`Create`](manim.animation.creation.Create.md#manim.animation.creation.Create) but in reverse.

### Examples

<div id="showuncreate" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShowUncreate <a class="headerlink" href="#showuncreate">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ShowUncreate-1.mp4">
</video>
```python
from manim import *

class ShowUncreate(Scene):
    def construct(self):
        self.play(Uncreate(Square()))
```

<pre data-manim-binder data-manim-classname="ShowUncreate">
class ShowUncreate(Scene):
    def construct(self):
        self.play(Uncreate(Square()))

</pre></div>

#### SEE ALSO
[`Create`](manim.animation.creation.Create.md#manim.animation.creation.Create)

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **reverse_rate_function** (*bool*)
  * **remover** (*bool*)

#### \_original_\_init_\_(mobject, reverse_rate_function=True, remover=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **reverse_rate_function** (*bool*)
  * **remover** (*bool*)
* **Return type:**
  None
