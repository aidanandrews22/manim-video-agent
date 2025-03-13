# ApplyWave

Qualified name: `manim.animation.indication.ApplyWave`

### *class* ApplyWave(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Homotopy`](manim.animation.movement.Homotopy.md#manim.animation.movement.Homotopy)

Send a wave through the Mobject distorting it temporarily.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be distorted.
  * **direction** (*np.ndarray*) – The direction in which the wave nudges points of the shape
  * **amplitude** (*float*) – The distance points of the shape get shifted
  * **wave_func** (*Callable* *[* *[**float* *]* *,* *float* *]*) – The function defining the shape of one wave flank.
  * **time_width** (*float*) – The length of the wave relative to the width of the mobject.
  * **ripples** (*int*) – The number of ripples of the wave
  * **run_time** (*float*) – The duration of the animation.

### Examples

<div id="applyingwaves" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ApplyingWaves <a class="headerlink" href="#applyingwaves">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ApplyingWaves-1.mp4">
</video>
```python
from manim import *

class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("WaveWaveWaveWaveWave").scale(2)
        self.play(ApplyWave(tex))
        self.play(ApplyWave(
            tex,
            direction=RIGHT,
            time_width=0.5,
            amplitude=0.3
        ))
        self.play(ApplyWave(
            tex,
            rate_func=linear,
            ripples=4
        ))
```

<pre data-manim-binder data-manim-classname="ApplyingWaves">
class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("WaveWaveWaveWaveWave").scale(2)
        self.play(ApplyWave(tex))
        self.play(ApplyWave(
            tex,
            direction=RIGHT,
            time_width=0.5,
            amplitude=0.3
        ))
        self.play(ApplyWave(
            tex,
            rate_func=linear,
            ripples=4
        ))

</pre></div>

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, direction=array([0., 1., 0.]), amplitude=0.2, wave_func=<function smooth>, time_width=1, ripples=1, run_time=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **direction** (*ndarray*)
  * **amplitude** (*float*)
  * **wave_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **time_width** (*float*)
  * **ripples** (*int*)
  * **run_time** (*float*)
* **Return type:**
  None
