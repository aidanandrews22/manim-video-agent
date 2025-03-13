# MobjectMatrix

Qualified name: `manim.mobject.matrix.MobjectMatrix`

### *class* MobjectMatrix(matrix, element_to_mobject=<function MobjectMatrix.<lambda>>, \*\*kwargs)

Bases: [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)

A mobject that displays a matrix of mobject entries on the screen.

### Examples

<div id="mobjectmatrixexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MobjectMatrixExample <a class="headerlink" href="#mobjectmatrixexample">¶</a></p>![image](media/images/MobjectMatrixExample-1.png)
```python
from manim import *

class MobjectMatrixExample(Scene):
    def construct(self):
        a = Circle().scale(0.3)
        b = Square().scale(0.3)
        c = MathTex("\\pi").scale(2)
        d = Star().scale(0.3)
        m0 = MobjectMatrix([[a, b], [c, d]])
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="MobjectMatrixExample">
class MobjectMatrixExample(Scene):
    def construct(self):
        a = Circle().scale(0.3)
        b = Square().scale(0.3)
        c = MathTex("\\\\pi").scale(2)
        d = Star().scale(0.3)
        m0 = MobjectMatrix([[a, b], [c, d]])
        self.add(m0)

</pre></div>

### Methods

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

#### \_original_\_init_\_(matrix, element_to_mobject=<function MobjectMatrix.<lambda>>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.
