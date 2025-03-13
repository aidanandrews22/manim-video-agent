# AnnularSector

Qualified name: `manim.mobject.geometry.arc.AnnularSector`

### *class* AnnularSector(inner_radius=1, outer_radius=2, angle=1.5707963267948966, start_angle=0, fill_opacity=1, stroke_width=0, color=ManimColor('#FFFFFF'), \*\*kwargs)

Bases: [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)

A sector of an annulus.

* **Parameters:**
  * **inner_radius** (*float*) – The inside radius of the Annular Sector.
  * **outer_radius** (*float*) – The outside radius of the Annular Sector.
  * **angle** (*float*) – The clockwise angle of the Annular Sector.
  * **start_angle** (*float*) – The starting clockwise angle of the Annular Sector.
  * **fill_opacity** (*float*) – The opacity of the color filled in the Annular Sector.
  * **stroke_width** (*float*) – The stroke width of the Annular Sector.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color filled into the Annular Sector.
  * **kwargs** (*Any*)

### Examples

<div id="annularsectorexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: AnnularSectorExample <a class="headerlink" href="#annularsectorexample">¶</a></p>![image](media/images/AnnularSectorExample-1.png)
```python
from manim import *

class AnnularSectorExample(Scene):
    def construct(self):
        # Changes background color to clearly visualize changes in fill_opacity.
        self.camera.background_color = WHITE

        # The default parameter start_angle is 0, so the AnnularSector starts from the +x-axis.
        s1 = AnnularSector(color=YELLOW).move_to(2 * UL)

        # Different inner_radius and outer_radius than the default.
        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=45 * DEGREES, color=RED).move_to(2 * UR)

        # fill_opacity is typically a number > 0 and <= 1. If fill_opacity=0, the AnnularSector is transparent.
        s3 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=PI, fill_opacity=0.25, color=BLUE).move_to(2 * DL)

        # With a negative value for the angle, the AnnularSector is drawn clockwise from the start value.
        s4 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=-3 * PI / 2, color=GREEN).move_to(2 * DR)

        self.add(s1, s2, s3, s4)
```

<pre data-manim-binder data-manim-classname="AnnularSectorExample">
class AnnularSectorExample(Scene):
    def construct(self):
        # Changes background color to clearly visualize changes in fill_opacity.
        self.camera.background_color = WHITE

        # The default parameter start_angle is 0, so the AnnularSector starts from the +x-axis.
        s1 = AnnularSector(color=YELLOW).move_to(2 \* UL)

        # Different inner_radius and outer_radius than the default.
        s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=45 \* DEGREES, color=RED).move_to(2 \* UR)

        # fill_opacity is typically a number > 0 and <= 1. If fill_opacity=0, the AnnularSector is transparent.
        s3 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=PI, fill_opacity=0.25, color=BLUE).move_to(2 \* DL)

        # With a negative value for the angle, the AnnularSector is drawn clockwise from the start value.
        s4 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=-3 \* PI / 2, color=GREEN).move_to(2 \* DR)

        self.add(s1, s2, s3, s4)

</pre></div>

### Methods

| [`generate_points`](#manim.mobject.geometry.arc.AnnularSector.generate_points)   | Initializes `points` and therefore the shape.   |
|----------------------------------------------------------------------------------|-------------------------------------------------|
| [`init_points`](#manim.mobject.geometry.arc.AnnularSector.init_points)           | Initializes `points` and therefore the shape.   |

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

#### \_original_\_init_\_(inner_radius=1, outer_radius=2, angle=1.5707963267948966, start_angle=0, fill_opacity=1, stroke_width=0, color=ManimColor('#FFFFFF'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **inner_radius** (*float*)
  * **outer_radius** (*float*)
  * **angle** (*float*)
  * **start_angle** (*float*)
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)
* **Return type:**
  None

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None

#### init_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None
