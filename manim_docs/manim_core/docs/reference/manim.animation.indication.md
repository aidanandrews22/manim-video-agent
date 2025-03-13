# indication

Animations drawing attention to particular mobjects.

### Examples

<div id="indications" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Indications <a class="headerlink" href="#indications">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./Indications-1.mp4">
</video>
```python
from manim import *

class Indications(Scene):
    def construct(self):
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        names = [Tex(i.__name__).scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is Flash:
                self.play(Flash(UP))
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
            ))
```

<pre data-manim-binder data-manim-classname="Indications">
class Indications(Scene):
    def construct(self):
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        names = [Tex(i._\_name_\_).scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is Flash:
                self.play(Flash(UP))
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP\*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP\*1.5),
            ))

</pre></div>

### Classes

| [`ApplyWave`](manim.animation.indication.ApplyWave.md#manim.animation.indication.ApplyWave)                                                                                           | Send a wave through the Mobject distorting it temporarily.    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [`Blink`](manim.animation.indication.Blink.md#manim.animation.indication.Blink)                                                                                                       | Blink the mobject.                                            |
| [`Circumscribe`](manim.animation.indication.Circumscribe.md#manim.animation.indication.Circumscribe)                                                                                  | Draw a temporary line surrounding the mobject.                |
| [`Flash`](manim.animation.indication.Flash.md#manim.animation.indication.Flash)                                                                                                       | Send out lines in all directions.                             |
| [`FocusOn`](manim.animation.indication.FocusOn.md#manim.animation.indication.FocusOn)                                                                                                 | Shrink a spotlight to a position.                             |
| [`Indicate`](manim.animation.indication.Indicate.md#manim.animation.indication.Indicate)                                                                                              | Indicate a Mobject by temporarily resizing and recoloring it. |
| [`ShowPassingFlash`](manim.animation.indication.ShowPassingFlash.md#manim.animation.indication.ShowPassingFlash)                                                                      | Show only a sliver of the VMobject each frame.                |
| [`ShowPassingFlashWithThinningStrokeWidth`](manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.md#manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth) |                                                               |
| [`Wiggle`](manim.animation.indication.Wiggle.md#manim.animation.indication.Wiggle)                                                                                                    | Wiggle a Mobject.                                             |
