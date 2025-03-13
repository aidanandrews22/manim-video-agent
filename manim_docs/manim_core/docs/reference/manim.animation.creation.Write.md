# Write

Qualified name: `manim.animation.creation.Write`

### *class* Write(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`DrawBorderThenFill`](manim.animation.creation.DrawBorderThenFill.md#manim.animation.creation.DrawBorderThenFill)

Simulate hand-writing a [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or hand-drawing a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

### Examples

<div id="showwrite" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShowWrite <a class="headerlink" href="#showwrite">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ShowWrite-1.mp4">
</video>
```python
from manim import *

class ShowWrite(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144)))
```

<pre data-manim-binder data-manim-classname="ShowWrite">
class ShowWrite(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144)))

</pre></div><div id="showwritereversed" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShowWriteReversed <a class="headerlink" href="#showwritereversed">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ShowWriteReversed-1.mp4">
</video>
```python
from manim import *

class ShowWriteReversed(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))
```

<pre data-manim-binder data-manim-classname="ShowWriteReversed">
class ShowWriteReversed(Scene):
    def construct(self):
        self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))

</pre></div>

### Tests

Check that creating empty [`Write`](#manim.animation.creation.Write) animations works:

```default
>>> from manim import Write, Text
>>> Write(Text(''))
Write(Text(''))
```

### Methods

| [`begin`](#manim.animation.creation.Write.begin)   | Begin the animation.   |
|----------------------------------------------------|------------------------|
| [`finish`](#manim.animation.creation.Write.finish) | Finish the animation.  |
| `reverse_submobjects`                              |                        |

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **reverse** (*bool*)

#### \_original_\_init_\_(vmobject, rate_func=<function linear>, reverse=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **reverse** (*bool*)
* **Return type:**
  None

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None

#### finish()

Finish the animation.

This method gets called when the animation is over.

* **Return type:**
  None
