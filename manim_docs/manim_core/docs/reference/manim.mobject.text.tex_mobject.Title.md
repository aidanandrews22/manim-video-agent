# Title

Qualified name: `manim.mobject.text.tex\_mobject.Title`

### *class* Title(\*text_parts, include_underline=True, match_underline_width_to_text=False, underline_buff=0.25, \*\*kwargs)

Bases: [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)

A mobject representing an underlined title.

### Examples

<div id="titleexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TitleExample <a class="headerlink" href="#titleexample">¶</a></p>![image](media/images/TitleExample-1.png)
```python
from manim import *

import manim

class TitleExample(Scene):
    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version {manim.__version__}")
        self.add(banner, title)
```

<pre data-manim-binder data-manim-classname="TitleExample">
import manim

class TitleExample(Scene):
    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version {manim._\_version_\_}")
        self.add(banner, title)

</pre></div>

### Methods

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `font_size`           | The font size of the tex mobject.                                      |
| `hash_seed`           | A unique hash representing the result of the generated mobject points. |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(\*text_parts, include_underline=True, match_underline_width_to_text=False, underline_buff=0.25, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.
