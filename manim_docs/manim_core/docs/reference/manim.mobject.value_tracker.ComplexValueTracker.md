# ComplexValueTracker

Qualified name: `manim.mobject.value\_tracker.ComplexValueTracker`

### *class* ComplexValueTracker(value=0, \*\*kwargs)

Bases: [`ValueTracker`](manim.mobject.value_tracker.ValueTracker.md#manim.mobject.value_tracker.ValueTracker)

Tracks a complex-valued parameter.

When the value is set through `animate`, the value will take a straight path from the
source point to the destination point.

### Examples

<div id="complexvaluetrackerexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ComplexValueTrackerExample <a class="headerlink" href="#complexvaluetrackerexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ComplexValueTrackerExample-1.mp4">
</video>
```python
from manim import *

class ComplexValueTrackerExample(Scene):
    def construct(self):
        tracker = ComplexValueTracker(-2+1j)
        dot = Dot().add_updater(
            lambda x: x.move_to(tracker.points)
        )

        self.add(NumberPlane(), dot)

        self.play(tracker.animate.set_value(3+2j))
        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.play(tracker.animate.set_value(tracker.get_value() - 2j))
        self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))
```

<pre data-manim-binder data-manim-classname="ComplexValueTrackerExample">
class ComplexValueTrackerExample(Scene):
    def construct(self):
        tracker = ComplexValueTracker(-2+1j)
        dot = Dot().add_updater(
            lambda x: x.move_to(tracker.points)
        )

        self.add(NumberPlane(), dot)

        self.play(tracker.animate.set_value(3+2j))
        self.play(tracker.animate.set_value(tracker.get_value() \* 1j))
        self.play(tracker.animate.set_value(tracker.get_value() - 2j))
        self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))

</pre></div>

### Methods

| [`get_value`](#manim.mobject.value_tracker.ComplexValueTracker.get_value)   | Get the current value of this value tracker as a complex number.   |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------|
| [`set_value`](#manim.mobject.value_tracker.ComplexValueTracker.set_value)   | Sets a new complex value to the ComplexValueTracker                |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |

#### \_original_\_init_\_(value=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

#### get_value()

Get the current value of this value tracker as a complex number.

The value is internally stored as a points array [a, b, 0]. This can be accessed directly
to represent the value geometrically, see the usage example.

#### set_value(z)

Sets a new complex value to the ComplexValueTracker
