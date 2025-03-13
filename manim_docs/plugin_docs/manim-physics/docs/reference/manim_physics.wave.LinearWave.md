# LinearWave

Qualified name: `manim\_physics.wave.LinearWave`

### *class* LinearWave(wavelength=1, period=1, amplitude=0.1, x_range=[-5, 5], y_range=[-5, 5], \*\*kwargs)

Bases: [`RadialWave`](manim_physics.wave.RadialWave.md#manim_physics.wave.RadialWave)

A 3D Surface with waves in one direction.

* **Parameters:**
  * **wavelength** (*float*) – The wavelength of the wave.
  * **period** (*float*) – The period of the wave.
  * **amplitude** (*float*) – The amplitude of the wave.
  * **x_range** (*Iterable* *[**float* *]*) – The range of the wave in the x direction.
  * **y_range** (*Iterable* *[**float* *]*) – The range of the wave in the y direction.
  * **kwargs** – Additional parameters to be passed to `Surface`.

### Examples

<div id="linearwaveexamplescene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LinearWaveExampleScene <a class="headerlink" href="#linearwaveexamplescene">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./LinearWaveExampleScene-1.mp4">
</video>
```python
from manim import *

class LinearWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 * DEGREES, -45 * DEGREES)
        wave = LinearWave()
        self.add(wave)
        wave.start_wave()
        self.wait()
        wave.stop_wave()
```

<pre data-manim-binder data-manim-classname="LinearWaveExampleScene">
class LinearWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 \* DEGREES, -45 \* DEGREES)
        wave = LinearWave()
        self.add(wave)
        wave.start_wave()
        self.wait()
        wave.stop_wave()

</pre></div>

### Methods

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
