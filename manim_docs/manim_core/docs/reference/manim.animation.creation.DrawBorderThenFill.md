# DrawBorderThenFill

Qualified name: `manim.animation.creation.DrawBorderThenFill`

### *class* DrawBorderThenFill(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Draw the border first and then show the fill.

### Examples

<div id="showdrawborderthenfill" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShowDrawBorderThenFill <a class="headerlink" href="#showdrawborderthenfill">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ShowDrawBorderThenFill-1.mp4">
</video>
```python
from manim import *

class ShowDrawBorderThenFill(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))
```

<pre data-manim-binder data-manim-classname="ShowDrawBorderThenFill">
class ShowDrawBorderThenFill(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))

</pre></div>

### Methods

| [`begin`](#manim.animation.creation.DrawBorderThenFill.begin)                       | Begin the animation.                        |
|-------------------------------------------------------------------------------------|---------------------------------------------|
| [`get_all_mobjects`](#manim.animation.creation.DrawBorderThenFill.get_all_mobjects) | Get all mobjects involved in the animation. |
| `get_outline`                                                                       |                                             |
| `get_stroke_color`                                                                  |                                             |
| `interpolate_submobject`                                                            |                                             |

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **run_time** (*float*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **stroke_width** (*float*)
  * **stroke_color** (*str*)
  * **draw_border_animation_config** (*dict*)
  * **fill_animation_config** (*dict*)
  * **introducer** (*bool*)

#### \_original_\_init_\_(vmobject, run_time=2, rate_func=<function double_smooth>, stroke_width=2, stroke_color=None, draw_border_animation_config={}, fill_animation_config={}, introducer=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **run_time** (*float*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **stroke_width** (*float*)
  * **stroke_color** (*str*)
  * **draw_border_animation_config** (*dict*)
  * **fill_animation_config** (*dict*)
  * **introducer** (*bool*)
* **Return type:**
  None

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None

#### get_all_mobjects()

Get all mobjects involved in the animation.

Ordering must match the ordering of arguments to interpolate_submobject

* **Returns:**
  The sequence of mobjects.
* **Return type:**
  Sequence[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]
