# SampleSpace

Qualified name: `manim.mobject.graphing.probability.SampleSpace`

### *class* SampleSpace(height=3, width=3, fill_color=ManimColor('#444444'), fill_opacity=1, stroke_width=0.5, stroke_color=ManimColor('#BBBBBB'), default_label_scale_val=1)

Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle)

A mobject representing a twodimensional rectangular
sampling space.

### Examples

<div id="examplesamplespace" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ExampleSampleSpace <a class="headerlink" href="#examplesamplespace">¶</a></p>![image](media/images/ExampleSampleSpace-1.png)
```python
from manim import *

class ExampleSampleSpace(Scene):
    def construct(self):
        poly1 = SampleSpace(stroke_width=15, fill_opacity=1)
        poly2 = SampleSpace(width=5, height=3, stroke_width=5, fill_opacity=0.5)
        poly3 = SampleSpace(width=2, height=2, stroke_width=5, fill_opacity=0.1)
        poly3.divide_vertically(p_list=np.array([0.37, 0.13, 0.5]), colors=[BLACK, WHITE, GRAY], vect=RIGHT)
        poly_group = VGroup(poly1, poly2, poly3).arrange()
        self.add(poly_group)
```

<pre data-manim-binder data-manim-classname="ExampleSampleSpace">
class ExampleSampleSpace(Scene):
    def construct(self):
        poly1 = SampleSpace(stroke_width=15, fill_opacity=1)
        poly2 = SampleSpace(width=5, height=3, stroke_width=5, fill_opacity=0.5)
        poly3 = SampleSpace(width=2, height=2, stroke_width=5, fill_opacity=0.1)
        poly3.divide_vertically(p_list=np.array([0.37, 0.13, 0.5]), colors=[BLACK, WHITE, GRAY], vect=RIGHT)
        poly_group = VGroup(poly1, poly2, poly3).arrange()
        self.add(poly_group)

</pre></div>

### Methods

| `add_braces_and_labels`             |    |
|-------------------------------------|----|
| `add_label`                         |    |
| `add_title`                         |    |
| `complete_p_list`                   |    |
| `divide_horizontally`               |    |
| `divide_vertically`                 |    |
| `get_bottom_braces_and_labels`      |    |
| `get_division_along_dimension`      |    |
| `get_horizontal_division`           |    |
| `get_side_braces_and_labels`        |    |
| `get_subdivision_braces_and_labels` |    |
| `get_top_braces_and_labels`         |    |
| `get_vertical_division`             |    |

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

#### \_original_\_init_\_(height=3, width=3, fill_color=ManimColor('#444444'), fill_opacity=1, stroke_width=0.5, stroke_color=ManimColor('#BBBBBB'), default_label_scale_val=1)

Initialize self.  See help(type(self)) for accurate signature.
