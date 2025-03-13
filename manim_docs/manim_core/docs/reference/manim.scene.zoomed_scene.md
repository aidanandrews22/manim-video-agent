# zoomed_scene

A scene supporting zooming in on a specified section.

### Examples

<div id="usezoomedscene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UseZoomedScene <a class="headerlink" href="#usezoomedscene">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./UseZoomedScene-1.mp4">
</video>
```python
from manim import *

class UseZoomedScene(ZoomedScene):
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.animate.shift(LEFT))
```

<pre data-manim-binder data-manim-classname="UseZoomedScene">
class UseZoomedScene(ZoomedScene):
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.animate.shift(LEFT))

</pre></div><div id="changingzoomscale" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ChangingZoomScale <a class="headerlink" href="#changingzoomscale">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ChangingZoomScale-1.mp4">
</video>
```python
from manim import *

class ChangingZoomScale(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=3,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )

    def construct(self):
        dot = Dot().set_color(GREEN)
        sq = Circle(fill_opacity=1, radius=0.2).next_to(dot, RIGHT)
        self.add(dot, sq)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.animate.shift(LEFT * 0.3))

        self.play(self.zoomed_camera.frame.animate.scale(4))
        self.play(self.zoomed_camera.frame.animate.shift(0.5 * DOWN))
```

<pre data-manim-binder data-manim-classname="ChangingZoomScale">
class ChangingZoomScale(ZoomedScene):
    def \_\_init_\_(self, \*\*kwargs):
        ZoomedScene._\_init_\_(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=3,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            \*\*kwargs
        )

    def construct(self):
        dot = Dot().set_color(GREEN)
        sq = Circle(fill_opacity=1, radius=0.2).next_to(dot, RIGHT)
        self.add(dot, sq)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.animate.shift(LEFT \* 0.3))

        self.play(self.zoomed_camera.frame.animate.scale(4))
        self.play(self.zoomed_camera.frame.animate.shift(0.5 \* DOWN))

</pre></div>

### Classes

| [`ZoomedScene`](manim.scene.zoomed_scene.ZoomedScene.md#manim.scene.zoomed_scene.ZoomedScene)   | This is a Scene with special configurations made for when a particular part of the scene must be zoomed in on and displayed separately.   |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
