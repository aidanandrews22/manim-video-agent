# BulletedList

Qualified name: `manim.mobject.text.tex\_mobject.BulletedList`

### *class* BulletedList(\*items, buff=0.5, dot_scale_factor=2, tex_environment=None, \*\*kwargs)

Bases: [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)

A bulleted list.

### Examples

<div id="bulletedlistexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: BulletedListExample <a class="headerlink" href="#bulletedlistexample">¶</a></p>![image](media/images/BulletedListExample-1.png)
```python
from manim import *

class BulletedListExample(Scene):
    def construct(self):
        blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
        blist.set_color_by_tex("Item 1", RED)
        blist.set_color_by_tex("Item 2", GREEN)
        blist.set_color_by_tex("Item 3", BLUE)
        self.add(blist)
```

<pre data-manim-binder data-manim-classname="BulletedListExample">
class BulletedListExample(Scene):
    def construct(self):
        blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
        blist.set_color_by_tex("Item 1", RED)
        blist.set_color_by_tex("Item 2", GREEN)
        blist.set_color_by_tex("Item 3", BLUE)
        self.add(blist)

</pre></div>

### Methods

| `fade_all_but`   |    |
|------------------|----|

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

#### \_original_\_init_\_(\*items, buff=0.5, dot_scale_factor=2, tex_environment=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.
