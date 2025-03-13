# mobject_update_utils

Utility functions for continuous animation of mobjects.

### Functions

### always(method, \*args, \*\*kwargs)

* **Parameters:**
  **method** (*Callable*)
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### always_redraw(func)

Redraw the mobject constructed by a function every frame.

This function returns a mobject with an attached updater that
continuously regenerates the mobject according to the
specified function.

* **Parameters:**
  **func** (*Callable* *[* *[* *]* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – A function without (required) input arguments that returns
  a mobject.
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

<div id="tangentanimation" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TangentAnimation <a class="headerlink" href="#tangentanimation">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./TangentAnimation-1.mp4">
</video>
```python
from manim import *

class TangentAnimation(Scene):
    def construct(self):
        ax = Axes()
        sine = ax.plot(np.sin, color=RED)
        alpha = ValueTracker(0)
        point = always_redraw(
            lambda: Dot(
                sine.point_from_proportion(alpha.get_value()),
                color=BLUE
            )
        )
        tangent = always_redraw(
            lambda: TangentLine(
                sine,
                alpha=alpha.get_value(),
                color=YELLOW,
                length=4
            )
        )
        self.add(ax, sine, point, tangent)
        self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)
```

<pre data-manim-binder data-manim-classname="TangentAnimation">
class TangentAnimation(Scene):
    def construct(self):
        ax = Axes()
        sine = ax.plot(np.sin, color=RED)
        alpha = ValueTracker(0)
        point = always_redraw(
            lambda: Dot(
                sine.point_from_proportion(alpha.get_value()),
                color=BLUE
            )
        )
        tangent = always_redraw(
            lambda: TangentLine(
                sine,
                alpha=alpha.get_value(),
                color=YELLOW,
                length=4
            )
        )
        self.add(ax, sine, point, tangent)
        self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)

</pre></div>

### always_rotate(mobject, rate=0.3490658503988659, \*\*kwargs)

A mobject which is continuously rotated at a certain rate.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be rotated.
  * **rate** (*float*) – The angle which the mobject is rotated by
    over one second.
  * **kwags** – Further arguments to be passed to [`Mobject.rotate()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.rotate).
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

<div id="spinningtriangle" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SpinningTriangle <a class="headerlink" href="#spinningtriangle">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./SpinningTriangle-1.mp4">
</video>
```python
from manim import *

class SpinningTriangle(Scene):
    def construct(self):
        tri = Triangle().set_fill(opacity=1).set_z_index(2)
        sq = Square().to_edge(LEFT)

        # will keep spinning while there is an animation going on
        always_rotate(tri, rate=2*PI, about_point=ORIGIN)

        self.add(tri, sq)
        self.play(sq.animate.to_edge(RIGHT), rate_func=linear, run_time=1)
```

<pre data-manim-binder data-manim-classname="SpinningTriangle">
class SpinningTriangle(Scene):
    def construct(self):
        tri = Triangle().set_fill(opacity=1).set_z_index(2)
        sq = Square().to_edge(LEFT)

        # will keep spinning while there is an animation going on
        always_rotate(tri, rate=2\*PI, about_point=ORIGIN)

        self.add(tri, sq)
        self.play(sq.animate.to_edge(RIGHT), rate_func=linear, run_time=1)

</pre></div>

### always_shift(mobject, direction=array([1., 0., 0.]), rate=0.1)

A mobject which is continuously shifted along some direction
at a certain rate.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to shift.
  * **direction** (*ndarray* *[**float64* *]*) – The direction to shift. The vector is normalized, the specified magnitude
    is not relevant.
  * **rate** (*float*) – Length in Manim units which the mobject travels in one
    second along the specified direction.
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

<div id="shiftingsquare" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShiftingSquare <a class="headerlink" href="#shiftingsquare">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ShiftingSquare-1.mp4">
</video>
```python
from manim import *

class ShiftingSquare(Scene):
    def construct(self):
        sq = Square().set_fill(opacity=1)
        tri = Triangle()
        VGroup(sq, tri).arrange(LEFT)

        # construct a square which is continuously
        # shifted to the right
        always_shift(sq, RIGHT, rate=5)

        self.add(sq)
        self.play(tri.animate.set_fill(opacity=1))
```

<pre data-manim-binder data-manim-classname="ShiftingSquare">
class ShiftingSquare(Scene):
    def construct(self):
        sq = Square().set_fill(opacity=1)
        tri = Triangle()
        VGroup(sq, tri).arrange(LEFT)

        # construct a square which is continuously
        # shifted to the right
        always_shift(sq, RIGHT, rate=5)

        self.add(sq)
        self.play(tri.animate.set_fill(opacity=1))

</pre></div>

### assert_is_mobject_method(method)

* **Parameters:**
  **method** (*Callable*)
* **Return type:**
  None

### cycle_animation(animation, \*\*kwargs)

* **Parameters:**
  **animation** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
* **Return type:**
  [Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### f_always(method, \*arg_generators, \*\*kwargs)

More functional version of always, where instead
of taking in args, it takes in functions which output
the relevant arguments.

* **Parameters:**
  **method** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *None* *]*)
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### turn_animation_into_updater(animation, cycle=False, delay=0, \*\*kwargs)

Add an updater to the animation’s mobject which applies
the interpolation and update functions of the animation

If cycle is True, this repeats over and over.  Otherwise,
the updater will be popped upon completion

The `delay` parameter is the delay (in seconds) before the animation starts..

### Examples

<div id="welcometomanim" class="admonition admonition-manim-example">
<p class="admonition-title">Example: WelcomeToManim <a class="headerlink" href="#welcometomanim">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./WelcomeToManim-1.mp4">
</video>
```python
from manim import *

class WelcomeToManim(Scene):
    def construct(self):
        words = Text("Welcome to")
        banner = ManimBanner().scale(0.5)
        VGroup(words, banner).arrange(DOWN)

        turn_animation_into_updater(Write(words, run_time=0.9))
        self.add(words)
        self.wait(0.5)
        self.play(banner.expand(), run_time=0.5)
```

<pre data-manim-binder data-manim-classname="WelcomeToManim">
class WelcomeToManim(Scene):
    def construct(self):
        words = Text("Welcome to")
        banner = ManimBanner().scale(0.5)
        VGroup(words, banner).arrange(DOWN)

        turn_animation_into_updater(Write(words, run_time=0.9))
        self.add(words)
        self.wait(0.5)
        self.play(banner.expand(), run_time=0.5)

</pre></div>
* **Parameters:**
  * **animation** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **cycle** (*bool*)
  * **delay** (*float*)
* **Return type:**
  [Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)
