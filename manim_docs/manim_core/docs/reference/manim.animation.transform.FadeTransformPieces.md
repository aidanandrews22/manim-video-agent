# FadeTransformPieces

Qualified name: `manim.animation.transform.FadeTransformPieces`

### *class* FadeTransformPieces(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`FadeTransform`](manim.animation.transform.FadeTransform.md#manim.animation.transform.FadeTransform)

Fades submobjects of one mobject into submobjects of another one.

#### SEE ALSO
[`FadeTransform`](manim.animation.transform.FadeTransform.md#manim.animation.transform.FadeTransform)

### Examples

<div id="fadetransformsubmobjects" class="admonition admonition-manim-example">
<p class="admonition-title">Example: FadeTransformSubmobjects <a class="headerlink" href="#fadetransformsubmobjects">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./FadeTransformSubmobjects-1.mp4">
</video>
```python
from manim import *

class FadeTransformSubmobjects(Scene):
    def construct(self):
        src = VGroup(Square(), Circle().shift(LEFT + UP))
        src.shift(3*LEFT + 2*UP)
        src_copy = src.copy().shift(4*DOWN)

        target = VGroup(Circle(), Triangle().shift(RIGHT + DOWN))
        target.shift(3*RIGHT + 2*UP)
        target_copy = target.copy().shift(4*DOWN)

        self.play(FadeIn(src), FadeIn(src_copy))
        self.play(
            FadeTransform(src, target),
            FadeTransformPieces(src_copy, target_copy)
        )
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
```

<pre data-manim-binder data-manim-classname="FadeTransformSubmobjects">
class FadeTransformSubmobjects(Scene):
    def construct(self):
        src = VGroup(Square(), Circle().shift(LEFT + UP))
        src.shift(3\*LEFT + 2\*UP)
        src_copy = src.copy().shift(4\*DOWN)

        target = VGroup(Circle(), Triangle().shift(RIGHT + DOWN))
        target.shift(3\*RIGHT + 2\*UP)
        target_copy = target.copy().shift(4\*DOWN)

        self.play(FadeIn(src), FadeIn(src_copy))
        self.play(
            FadeTransform(src, target),
            FadeTransformPieces(src_copy, target_copy)
        )
        self.play(\*[FadeOut(mobj) for mobj in self.mobjects])

</pre></div>

### Methods

| [`begin`](#manim.animation.transform.FadeTransformPieces.begin)       | Initial setup for the animation.                                                     |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [`ghost_to`](#manim.animation.transform.FadeTransformPieces.ghost_to) | Replaces the source submobjects by the target submobjects and sets the opacity to 0. |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, target_mobject, stretch=True, dim_to_match=1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

#### begin()

Initial setup for the animation.

The mobject to which this animation is bound is a group consisting of
both the starting and the ending mobject. At the start, the ending
mobject replaces the starting mobject (and is completely faded). In the
end, it is set to be the other way around.

#### ghost_to(source, target)

Replaces the source submobjects by the target submobjects and sets
the opacity to 0.
