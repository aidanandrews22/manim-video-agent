# Flash

Qualified name: `manim.animation.indication.Flash`

### *class* Flash(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.md#manim.animation.composition.AnimationGroup)

Send out lines in all directions.

* **Parameters:**
  * **point** (*np.ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The center of the flash lines. If it is a `Mobject` its center will be used.
  * **line_length** (*float*) – The length of the flash lines.
  * **num_lines** (*int*) – The number of flash lines.
  * **flash_radius** (*float*) – The distance from point at which the flash lines start.
  * **line_stroke_width** (*int*) – The stroke width of the flash lines.
  * **color** (*str*) – The color of the flash lines.
  * **time_width** (*float*) – The time width used for the flash lines. See `ShowPassingFlash` for more details.
  * **run_time** (*float*) – The duration of the animation.
  * **kwargs** – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.md#manim.animation.composition.Succession) constructor

### Examples

<div id="usingflash" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UsingFlash <a class="headerlink" href="#usingflash">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UsingFlash-1.mp4">
</video>
```python
from manim import *

class UsingFlash(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(DOWN)
        self.add(Tex("Flash the dot below:"), dot)
        self.play(Flash(dot))
        self.wait()
```

<pre data-manim-binder data-manim-classname="UsingFlash">
class UsingFlash(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(DOWN)
        self.add(Tex("Flash the dot below:"), dot)
        self.play(Flash(dot))
        self.wait()

</pre></div><div id="flashoncircle" class="admonition admonition-manim-example">
<p class="admonition-title">Example: FlashOnCircle <a class="headerlink" href="#flashoncircle">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./FlashOnCircle-1.mp4">
</video>
```python
from manim import *

class FlashOnCircle(Scene):
    def construct(self):
        radius = 2
        circle = Circle(radius)
        self.add(circle)
        self.play(Flash(
            circle, line_length=1,
            num_lines=30, color=RED,
            flash_radius=radius+SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))
```

<pre data-manim-binder data-manim-classname="FlashOnCircle">
class FlashOnCircle(Scene):
    def construct(self):
        radius = 2
        circle = Circle(radius)
        self.add(circle)
        self.play(Flash(
            circle, line_length=1,
            num_lines=30, color=RED,
            flash_radius=radius+SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))

</pre></div>

### Methods

| `create_line_anims`   |    |
|-----------------------|----|
| `create_lines`        |    |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(point, line_length=0.2, num_lines=12, flash_radius=0.1, line_stroke_width=3, color=ManimColor('#FFFF00'), time_width=1, run_time=1.0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **point** (*ndarray* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **line_length** (*float*)
  * **num_lines** (*int*)
  * **flash_radius** (*float*)
  * **line_stroke_width** (*int*)
  * **color** (*str*)
  * **time_width** (*float*)
  * **run_time** (*float*)
* **Return type:**
  None
