# paths

Functions determining transformation paths between sets of points.

### Functions

### clockwise_path()

This function transforms each point by moving clockwise around a half circle.

### Examples

<div id="clockwisepathexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ClockwisePathExample <a class="headerlink" href="#clockwisepathexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ClockwisePathExample-1.mp4">
</video>
```python
from manim import *

class ClockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.clockwise_path(),
                run_time=2,
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="ClockwisePathExample">
class ClockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            \*[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            \*[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.clockwise_path(),
                run_time=2,
            )
        )
        self.wait()

</pre></div>
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### counterclockwise_path()

This function transforms each point by moving counterclockwise around a half circle.

### Examples

<div id="counterclockwisepathexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CounterclockwisePathExample <a class="headerlink" href="#counterclockwisepathexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./CounterclockwisePathExample-1.mp4">
</video>
```python
from manim import *

class CounterclockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.counterclockwise_path(),
                run_time=2,
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="CounterclockwisePathExample">
class CounterclockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            \*[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            \*[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.counterclockwise_path(),
                run_time=2,
            )
        )
        self.wait()

</pre></div>
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### path_along_arc(arc_angle, axis=array([0., 0., 1.]))

This function transforms each point by moving it along a circular arc.

* **Parameters:**
  * **arc_angle** (*float*) – The angle each point traverses around a circular arc.
  * **axis** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – The axis of rotation.
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### Examples

<div id="pathalongarcexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PathAlongArcExample <a class="headerlink" href="#pathalongarcexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./PathAlongArcExample-1.mp4">
</video>
```python
from manim import *

class PathAlongArcExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_arc(TAU * 2 / 3),
                run_time=3,
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="PathAlongArcExample">
class PathAlongArcExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            \*[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            \*[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_arc(TAU \* 2 / 3),
                run_time=3,
            )
        )
        self.wait()

</pre></div>

### path_along_circles(arc_angle, circles_centers, axis=array([0., 0., 1.]))

This function transforms each point by moving it roughly along a circle, each with its own specified center.

The path may be seen as each point smoothly changing its orbit from its starting position to its destination.

* **Parameters:**
  * **arc_angle** (*float*) – The angle each point traverses around the quasicircle.
  * **circles_centers** (*ndarray*) – The centers of each point’s quasicircle to rotate around.
  * **axis** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – The axis of rotation.
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### Examples

<div id="pathalongcirclesexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PathAlongCirclesExample <a class="headerlink" href="#pathalongcirclesexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./PathAlongCirclesExample-1.mp4">
</video>
```python
from manim import *

class PathAlongCirclesExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        circle_center = Dot(3 * LEFT)
        self.add(circle_center)

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_circles(
                    2 * PI, circle_center.get_center()
                ),
                run_time=3,
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="PathAlongCirclesExample">
class PathAlongCirclesExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            \*[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            \*[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        circle_center = Dot(3 \* LEFT)
        self.add(circle_center)

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_circles(
                    2 \* PI, circle_center.get_center()
                ),
                run_time=3,
            )
        )
        self.wait()

</pre></div>

### spiral_path(angle, axis=array([0., 0., 1.]))

This function transforms each point by moving along a spiral to its destination.

* **Parameters:**
  * **angle** (*float*) – The angle each point traverses around a spiral.
  * **axis** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – The axis of rotation.
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### Examples

<div id="spiralpathexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SpiralPathExample <a class="headerlink" href="#spiralpathexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./SpiralPathExample-1.mp4">
</video>
```python
from manim import *

class SpiralPathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.spiral_path(2 * TAU),
                run_time=5,
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="SpiralPathExample">
class SpiralPathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            \*[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            \*[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.spiral_path(2 \* TAU),
                run_time=5,
            )
        )
        self.wait()

</pre></div>

### straight_path()

Simplest path function. Each point in a set goes in a straight path toward its destination.

### Examples

<div id="straightpathexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: StraightPathExample <a class="headerlink" href="#straightpathexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./StraightPathExample-1.mp4">
</video>
```python
from manim import *

class StraightPathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            *[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.straight_path(),
                run_time=2,
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="StraightPathExample">
class StraightPathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            \*[
                Dot(LEFT + pos, color=color)
                for pos, color in zip([UP, DOWN, LEFT], colors)
            ]
        )

        finish_points = VGroup(
            \*[
                Dot(RIGHT + pos, color=color)
                for pos, color in zip([ORIGIN, UP, DOWN], colors)
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.straight_path(),
                run_time=2,
            )
        )
        self.wait()

</pre></div>
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)
