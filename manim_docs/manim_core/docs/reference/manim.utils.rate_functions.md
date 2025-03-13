# rate_functions

A selection of rate functions, i.e., *speed curves* for animations.
Please find a standard list at [https://easings.net/](https://easings.net/). Here is a picture
for the non-standard ones

<div id="ratefuncexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RateFuncExample <a class="headerlink" href="#ratefuncexample">¶</a></p>![image](media/images/RateFuncExample-1.png)
```python
from manim import *

class RateFuncExample(Scene):
    def construct(self):
        x = VGroup()
        for k, v in rate_functions.__dict__.items():
            if "function" in str(v):
                if (
                    not k.startswith("__")
                    and not k.startswith("sqrt")
                    and not k.startswith("bezier")
                ):
                    try:
                        rate_func = v
                        plot = (
                            ParametricFunction(
                                lambda x: [x, rate_func(x), 0],
                                t_range=[0, 1, .01],
                                use_smoothing=False,
                                color=YELLOW,
                            )
                            .stretch_to_fit_width(1.5)
                            .stretch_to_fit_height(1)
                        )
                        plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                        plot_title = (
                            Text(rate_func.__name__, weight=BOLD)
                            .scale(0.5)
                            .next_to(plot_bg, UP, buff=0.1)
                        )
                        x.add(VGroup(plot_bg, plot, plot_title))
                    except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
                        pass
        x.arrange_in_grid(cols=8)
        x.height = config.frame_height
        x.width = config.frame_width
        x.move_to(ORIGIN).scale(0.95)
        self.add(x)
```

<pre data-manim-binder data-manim-classname="RateFuncExample">
class RateFuncExample(Scene):
    def construct(self):
        x = VGroup()
        for k, v in rate_functions._\_dict_\_.items():
            if "function" in str(v):
                if (
                    not k.startswith("_\_")
                    and not k.startswith("sqrt")
                    and not k.startswith("bezier")
                ):
                    try:
                        rate_func = v
                        plot = (
                            ParametricFunction(
                                lambda x: [x, rate_func(x), 0],
                                t_range=[0, 1, .01],
                                use_smoothing=False,
                                color=YELLOW,
                            )
                            .stretch_to_fit_width(1.5)
                            .stretch_to_fit_height(1)
                        )
                        plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                        plot_title = (
                            Text(rate_func._\_name_\_, weight=BOLD)
                            .scale(0.5)
                            .next_to(plot_bg, UP, buff=0.1)
                        )
                        x.add(VGroup(plot_bg, plot, plot_title))
                    except: # because functions \`not_quite_there\`, \`function squish_rate_func\` are not working.
                        pass
        x.arrange_in_grid(cols=8)
        x.height = config.frame_height
        x.width = config.frame_width
        x.move_to(ORIGIN).scale(0.95)
        self.add(x)

</pre></div>

There are primarily 3 kinds of standard easing functions:

1. Ease In - The animation has a smooth start.
2. Ease Out - The animation has a smooth end.
3. Ease In Out - The animation has a smooth start as well as smooth end.

#### NOTE
The standard functions are not exported, so to use them you do something like this:
rate_func=rate_functions.ease_in_sine
On the other hand, the non-standard functions, which are used more commonly, are exported and can be used directly.

<div id="ratefunctions1example" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RateFunctions1Example <a class="headerlink" href="#ratefunctions1example">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./RateFunctions1Example-1.mp4">
</video>
```python
from manim import *

class RateFunctions1Example(Scene):
    def construct(self):
        line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
        line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
        line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

        dot1 = Dot().move_to(line1.get_left())
        dot2 = Dot().move_to(line2.get_left())
        dot3 = Dot().move_to(line3.get_left())

        label1 = Tex("Ease In").next_to(line1, RIGHT)
        label2 = Tex("Ease out").next_to(line2, RIGHT)
        label3 = Tex("Ease In Out").next_to(line3, RIGHT)

        self.play(
            FadeIn(VGroup(line1, line2, line3)),
            FadeIn(VGroup(dot1, dot2, dot3)),
            Write(VGroup(label1, label2, label3)),
        )
        self.play(
            MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            run_time=7
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="RateFunctions1Example">
class RateFunctions1Example(Scene):
    def construct(self):
        line1 = Line(3\*LEFT, 3\*RIGHT).shift(UP).set_color(RED)
        line2 = Line(3\*LEFT, 3\*RIGHT).set_color(GREEN)
        line3 = Line(3\*LEFT, 3\*RIGHT).shift(DOWN).set_color(BLUE)

        dot1 = Dot().move_to(line1.get_left())
        dot2 = Dot().move_to(line2.get_left())
        dot3 = Dot().move_to(line3.get_left())

        label1 = Tex("Ease In").next_to(line1, RIGHT)
        label2 = Tex("Ease out").next_to(line2, RIGHT)
        label3 = Tex("Ease In Out").next_to(line3, RIGHT)

        self.play(
            FadeIn(VGroup(line1, line2, line3)),
            FadeIn(VGroup(dot1, dot2, dot3)),
            Write(VGroup(label1, label2, label3)),
        )
        self.play(
            MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            run_time=7
        )
        self.wait()

</pre></div>

### Classes

| [`RateFunction`](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)   |    |
|--------------------------------------------------------------------------------------------------------|----|

### Functions

### double_smooth(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_back(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_bounce(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_circ(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_cubic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_elastic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_expo(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_back(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_bounce(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_circ(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_cubic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_elastic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_expo(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_quad(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_quart(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_quint(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_sine(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_quad(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_quart(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_quint(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_sine(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_back(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_bounce(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_circ(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_cubic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_elastic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_expo(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_quad(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_quart(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_quint(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_sine(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### exponential_decay(t, half_life=0.1)

* **Parameters:**
  * **t** (*float*)
  * **half_life** (*float*)
* **Return type:**
  float

### linear(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### lingering(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### not_quite_there(func=<function smooth>, proportion=0.7)

* **Parameters:**
  * **func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **proportion** (*float*)
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)

### running_start(t, pull_factor=-0.5)

* **Parameters:**
  * **t** (*float*)
  * **pull_factor** (*float*)
* **Return type:**
  float

### rush_from(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### rush_into(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### slow_into(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### smooth(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### smoothererstep(t)

Implementation of the 3rd order SmoothStep sigmoid function.
The 1st, 2nd and 3rd derivatives (speed, acceleration and jerk) are zero at the endpoints.
[https://en.wikipedia.org/wiki/Smoothstep](https://en.wikipedia.org/wiki/Smoothstep)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### smootherstep(t)

Implementation of the 2nd order SmoothStep sigmoid function.
The 1st and 2nd derivatives (speed and acceleration) are zero at the endpoints.
[https://en.wikipedia.org/wiki/Smoothstep](https://en.wikipedia.org/wiki/Smoothstep)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### smoothstep(t)

Implementation of the 1st order SmoothStep sigmoid function.
The 1st derivative (speed) is zero at the endpoints.
[https://en.wikipedia.org/wiki/Smoothstep](https://en.wikipedia.org/wiki/Smoothstep)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### squish_rate_func(func, a=0.4, b=0.6)

* **Parameters:**
  * **func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **a** (*float*)
  * **b** (*float*)
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)

### there_and_back(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### there_and_back_with_pause(t, pause_ratio=0.3333333333333333)

* **Parameters:**
  * **t** (*float*)
  * **pause_ratio** (*float*)
* **Return type:**
  float

### unit_interval(function)

* **Parameters:**
  **function** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)

### wiggle(t, wiggles=2)

* **Parameters:**
  * **t** (*float*)
  * **wiggles** (*float*)
* **Return type:**
  float

### zero(function)

* **Parameters:**
  **function** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)
