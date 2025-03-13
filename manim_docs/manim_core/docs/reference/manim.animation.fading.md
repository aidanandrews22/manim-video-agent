# fading

Fading in and out of view.

<div id="fading" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Fading <a class="headerlink" href="#fading">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./Fading-1.mp4">
</video>
```python
from manim import *

class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))
```

<pre data-manim-binder data-manim-classname="Fading">
class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN \* 2, scale=1.5))

</pre></div>

### Classes

| [`FadeIn`](manim.animation.fading.FadeIn.md#manim.animation.fading.FadeIn)    | Fade in [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) s.   |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [`FadeOut`](manim.animation.fading.FadeOut.md#manim.animation.fading.FadeOut) | Fade out [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) s.  |
