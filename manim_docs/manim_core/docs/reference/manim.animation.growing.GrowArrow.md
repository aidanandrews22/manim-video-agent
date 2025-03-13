# GrowArrow

Qualified name: `manim.animation.growing.GrowArrow`

### *class* GrowArrow(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.md#manim.animation.growing.GrowFromPoint)

Introduce an [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow) by growing it from its start toward its tip.

* **Parameters:**
  * **arrow** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)) – The arrow to be introduced.
  * **point_color** (*str*) – Initial color of the arrow before growing to its full size. Leave empty to match arrow’s color.

### Examples

<div id="growarrowexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GrowArrowExample <a class="headerlink" href="#growarrowexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./GrowArrowExample-1.mp4">
</video>
```python
from manim import *

class GrowArrowExample(Scene):
    def construct(self):
        arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
        VGroup(*arrows).set_x(0).arrange(buff=2)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1], point_color=RED))
```

<pre data-manim-binder data-manim-classname="GrowArrowExample">
class GrowArrowExample(Scene):
    def construct(self):
        arrows = [Arrow(2 \* LEFT, 2 \* RIGHT), Arrow(2 \* DR, 2 \* UL)]
        VGroup(\*arrows).set_x(0).arrange(buff=2)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1], point_color=RED))

</pre></div>

### Methods

| `create_starting_mobject`   |    |
|-----------------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(arrow, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **arrow** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow))
  * **point_color** (*str*)
* **Return type:**
  None
