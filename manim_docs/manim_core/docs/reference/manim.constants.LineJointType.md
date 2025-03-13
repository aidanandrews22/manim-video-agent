# LineJointType

Qualified name: `manim.constants.LineJointType`

### *class* LineJointType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: `Enum`

Collection of available line joint types.

See the example below for a visual illustration of the different
joint types.

### Examples

<div id="linejointvariants" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LineJointVariants <a class="headerlink" href="#linejointvariants">¶</a></p>![image](media/images/LineJointVariants-1.png)
```python
from manim import *

class LineJointVariants(Scene):
    def construct(self):
        mob = VMobject(stroke_width=20, color=GREEN).set_points_as_corners([
            np.array([-2, 0, 0]),
            np.array([0, 0, 0]),
            np.array([-2, 1, 0]),
        ])
        lines = VGroup(*[mob.copy() for _ in range(len(LineJointType))])
        for line, joint_type in zip(lines, LineJointType):
            line.joint_type = joint_type

        lines.arrange(RIGHT, buff=1)
        self.add(lines)
        for line in lines:
            label = Text(line.joint_type.name).next_to(line, DOWN)
            self.add(label)
```

<pre data-manim-binder data-manim-classname="LineJointVariants">
class LineJointVariants(Scene):
    def construct(self):
        mob = VMobject(stroke_width=20, color=GREEN).set_points_as_corners([
            np.array([-2, 0, 0]),
            np.array([0, 0, 0]),
            np.array([-2, 1, 0]),
        ])
        lines = VGroup(\*[mob.copy() for \_ in range(len(LineJointType))])
        for line, joint_type in zip(lines, LineJointType):
            line.joint_type = joint_type

        lines.arrange(RIGHT, buff=1)
        self.add(lines)
        for line in lines:
            label = Text(line.joint_type.name).next_to(line, DOWN)
            self.add(label)

</pre></div>

### Attributes

| `AUTO`   |    |
|----------|----|
| `ROUND`  |    |
| `BEVEL`  |    |
| `MITER`  |    |
