# ManimBanner

Qualified name: `manim.mobject.logo.ManimBanner`

### *class* ManimBanner(dark_theme=True)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

Convenience class representing Manim’s banner.

Can be animated using custom methods.

* **Parameters:**
  **dark_theme** (*bool*) – If `True` (the default), the dark theme version of the logo
  (with light text font) will be rendered. Otherwise, if `False`,
  the light theme version (with dark text font) is used.

### Examples

<div id="darkthemebanner" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DarkThemeBanner <a class="headerlink" href="#darkthemebanner">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./DarkThemeBanner-1.mp4">
</video>
```python
from manim import *

class DarkThemeBanner(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
```

<pre data-manim-binder data-manim-classname="DarkThemeBanner">
class DarkThemeBanner(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))

</pre></div><div id="lightthemebanner" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LightThemeBanner <a class="headerlink" href="#lightthemebanner">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./LightThemeBanner-1.mp4">
</video>
```python
from manim import *

class LightThemeBanner(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
```

<pre data-manim-binder data-manim-classname="LightThemeBanner">
class LightThemeBanner(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))

</pre></div>

### Methods

| [`create`](#manim.mobject.logo.ManimBanner.create)   | The creation animation for Manim's logo.                |
|------------------------------------------------------|---------------------------------------------------------|
| [`expand`](#manim.mobject.logo.ManimBanner.expand)   | An animation that expands Manim's logo into its banner. |
| [`scale`](#manim.mobject.logo.ManimBanner.scale)     | Scale the banner by the specified scale factor.         |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(dark_theme=True)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **dark_theme** (*bool*)

#### create(run_time=2)

The creation animation for Manim’s logo.

* **Parameters:**
  **run_time** (*float*) – The run time of the animation.
* **Returns:**
  An animation to be used in a [`Scene.play()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.play) call.
* **Return type:**
  [`AnimationGroup`](manim.animation.composition.AnimationGroup.md#manim.animation.composition.AnimationGroup)

#### expand(run_time=1.5, direction='center')

An animation that expands Manim’s logo into its banner.

The returned animation transforms the banner from its initial
state (representing Manim’s logo with just the icons) to its
expanded state (showing the full name together with the icons).

See the class documentation for how to use this.

#### NOTE
Before calling this method, the text “anim” is not a
submobject of the banner object. After the expansion,
it is added as a submobject so subsequent animations
to the banner object apply to the text “anim” as well.

* **Parameters:**
  * **run_time** (*float*) – The run time of the animation.
  * **direction** – The direction in which the logo is expanded.
* **Returns:**
  An animation to be used in a [`Scene.play()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.play) call.
* **Return type:**
  [`Succession`](manim.animation.composition.Succession.md#manim.animation.composition.Succession)

### Examples

<div id="expanddirections" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ExpandDirections <a class="headerlink" href="#expanddirections">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ExpandDirections-1.mp4">
</video>
```python
from manim import *

class ExpandDirections(Scene):
    def construct(self):
        banners = [ManimBanner().scale(0.5).shift(UP*x) for x in [-2, 0, 2]]
        self.play(
            banners[0].expand(direction="right"),
            banners[1].expand(direction="center"),
            banners[2].expand(direction="left"),
        )
```

<pre data-manim-binder data-manim-classname="ExpandDirections">
class ExpandDirections(Scene):
    def construct(self):
        banners = [ManimBanner().scale(0.5).shift(UP\*x) for x in [-2, 0, 2]]
        self.play(
            banners[0].expand(direction="right"),
            banners[1].expand(direction="center"),
            banners[2].expand(direction="left"),
        )

</pre></div>

#### scale(scale_factor, \*\*kwargs)

Scale the banner by the specified scale factor.

* **Parameters:**
  **scale_factor** (*float*) – The factor used for scaling the banner.
* **Returns:**
  The scaled banner.
* **Return type:**
  [`ManimBanner`](#manim.mobject.logo.ManimBanner)
