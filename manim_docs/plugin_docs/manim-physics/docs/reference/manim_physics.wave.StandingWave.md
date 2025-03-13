# StandingWave

Qualified name: `manim\_physics.wave.StandingWave`

### *class* StandingWave(n=2, length=4, period=1, amplitude=1, \*\*kwargs)

Bases: `ParametricFunction`

A 2D standing wave.

* **Parameters:**
  * **n** (*int*) – Harmonic number.
  * **length** (*float*) – The length of the wave.
  * **period** (*float*) – The time taken for one full oscillation.
  * **amplitude** (*float*) – The maximum height of the wave.
  * **kwargs** – Additional parameters to be passed to `ParametricFunction`.

### Examples

<div id="standingwaveexamplescene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: StandingWaveExampleScene <a class="headerlink" href="#standingwaveexamplescene">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./StandingWaveExampleScene-1.mp4">
</video>
```python
from manim import *

from manim_physics import *

class StandingWaveExampleScene(Scene):
    def construct(self):
        wave1 = StandingWave(1)
        wave2 = StandingWave(2)
        wave3 = StandingWave(3)
        wave4 = StandingWave(4)
        waves = VGroup(wave1, wave2, wave3, wave4)
        waves.arrange(DOWN).move_to(ORIGIN)
        self.add(waves)
        for wave in waves:
            wave.start_wave()
        self.wait()
```

<pre data-manim-binder data-manim-classname="StandingWaveExampleScene">
from manim_physics import \*

class StandingWaveExampleScene(Scene):
    def construct(self):
        wave1 = StandingWave(1)
        wave2 = StandingWave(2)
        wave3 = StandingWave(3)
        wave4 = StandingWave(4)
        waves = VGroup(wave1, wave2, wave3, wave4)
        waves.arrange(DOWN).move_to(ORIGIN)
        self.add(waves)
        for wave in waves:
            wave.start_wave()
        self.wait()

</pre></div>

### Methods

| `start_wave`   |    |
|----------------|----|
| `stop_wave`    |    |

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
