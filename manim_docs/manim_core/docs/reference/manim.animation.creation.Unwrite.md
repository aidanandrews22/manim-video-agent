# Unwrite

Qualified name: `manim.animation.creation.Unwrite`

### *class* Unwrite(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Write`](manim.animation.creation.Write.md#manim.animation.creation.Write)

Simulate erasing by hand a [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

* **Parameters:**
  * **reverse** (*bool*) – Set True to have the animation start erasing from the last submobject first.
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)

### Examples

<div id="unwritereversetrue" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UnwriteReverseTrue <a class="headerlink" href="#unwritereversetrue">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UnwriteReverseTrue-1.mp4">
</video>
```python
from manim import *

class UnwriteReverseTrue(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text))
```

<pre data-manim-binder data-manim-classname="UnwriteReverseTrue">
class UnwriteReverseTrue(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text))

</pre></div><div id="unwritereversefalse" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UnwriteReverseFalse <a class="headerlink" href="#unwritereversefalse">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UnwriteReverseFalse-1.mp4">
</video>
```python
from manim import *

class UnwriteReverseFalse(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text, reverse=False))
```

<pre data-manim-binder data-manim-classname="UnwriteReverseFalse">
class UnwriteReverseFalse(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text, reverse=False))

</pre></div>

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(vmobject, rate_func=<function linear>, reverse=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **reverse** (*bool*)
* **Return type:**
  None
