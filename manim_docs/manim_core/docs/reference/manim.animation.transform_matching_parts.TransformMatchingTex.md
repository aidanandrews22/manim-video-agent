# TransformMatchingTex

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingTex`

### *class* TransformMatchingTex(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.md#manim.animation.transform_matching_parts.TransformMatchingAbstractBase)

A transformation trying to transform rendered LaTeX strings.

Two submobjects match if their `tex_string` matches.

#### SEE ALSO
[`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.md#manim.animation.transform_matching_parts.TransformMatchingAbstractBase)

### Examples

<div id="matchingequationparts" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MatchingEquationParts <a class="headerlink" href="#matchingequationparts">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./MatchingEquationParts-1.mp4">
</video>
```python
from manim import *

class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)
```

<pre data-manim-binder data-manim-classname="MatchingEquationParts">
class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)

</pre></div>

### Methods

| `get_mobject_key`   |    |
|---------------------|----|
| `get_mobject_parts` |    |

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **transform_mismatches** (*bool*)
  * **fade_transform_mismatches** (*bool*)
  * **key_map** (*dict* *|* *None*)

#### \_original_\_init_\_(mobject, target_mobject, transform_mismatches=False, fade_transform_mismatches=False, key_map=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **transform_mismatches** (*bool*)
  * **fade_transform_mismatches** (*bool*)
  * **key_map** (*dict* *|* *None*)
