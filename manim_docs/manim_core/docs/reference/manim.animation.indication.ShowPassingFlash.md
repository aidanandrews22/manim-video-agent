# ShowPassingFlash

Qualified name: `manim.animation.indication.ShowPassingFlash`

### *class* ShowPassingFlash(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ShowPartial`](manim.animation.creation.ShowPartial.md#manim.animation.creation.ShowPartial)

Show only a sliver of the VMobject each frame.

* **Parameters:**
  * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The mobject whose stroke is animated.
  * **time_width** (*float*) – The length of the sliver relative to the length of the stroke.

### Examples

<div id="timewidthvalues" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TimeWidthValues <a class="headerlink" href="#timewidthvalues">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./TimeWidthValues-1.mp4">
</video>
```python
from manim import *

class TimeWidthValues(Scene):
    def construct(self):
        p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
        lbl = VMobject()
        self.add(p, lbl)
        p = p.copy().set_color(BLUE)
        for time_width in [0.2, 0.5, 1, 2]:
            lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
            self.play(ShowPassingFlash(
                p.copy().set_color(BLUE),
                run_time=2,
                time_width=time_width
            ))
```

<pre data-manim-binder data-manim-classname="TimeWidthValues">
class TimeWidthValues(Scene):
    def construct(self):
        p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
        lbl = VMobject()
        self.add(p, lbl)
        p = p.copy().set_color(BLUE)
        for time_width in [0.2, 0.5, 1, 2]:
            lbl.become(Tex(r"\\texttt{time\\_width={{%.1f}}}"%time_width))
            self.play(ShowPassingFlash(
                p.copy().set_color(BLUE),
                run_time=2,
                time_width=time_width
            ))

</pre></div>

#### SEE ALSO
[`Create`](manim.animation.creation.Create.md#manim.animation.creation.Create)

### Methods

| [`clean_up_from_scene`](#manim.animation.indication.ShowPassingFlash.clean_up_from_scene)   | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.   |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, time_width=0.1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **time_width** (*float*)
* **Return type:**
  None

#### clean_up_from_scene(scene)

Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.

This includes to [`remove()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is a remover.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene the animation should be cleaned up from.
* **Return type:**
  None
