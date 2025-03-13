# RadialWave

Qualified name: `manim\_physics.wave.RadialWave`

### *class* RadialWave(\*sources, wavelength=1, period=1, amplitude=0.1, x_range=[-5, 5], y_range=[-5, 5], \*\*kwargs)

Bases: `Surface`

A 3D Surface with waves moving radially.

* **Parameters:**
  * **sources** (*Optional* *[**np.ndarray* *]*) – The sources of disturbance.
  * **wavelength** (*float*) – The wavelength of the wave.
  * **period** (*float*) – The period of the wave.
  * **amplitude** (*float*) – The amplitude of the wave.
  * **x_range** (*Iterable* *[**float* *]*) – The range of the wave in the x direction.
  * **y_range** (*Iterable* *[**float* *]*) – The range of the wave in the y direction.
  * **kwargs** – Additional parameters to be passed to `Surface`.

### Examples

<div id="radialwaveexamplescene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RadialWaveExampleScene <a class="headerlink" href="#radialwaveexamplescene">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./RadialWaveExampleScene-1.mp4">
</video>
```python
from manim import *

class RadialWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 * DEGREES, -45 * DEGREES)
        wave = RadialWave(
            LEFT * 2 + DOWN * 5,  # Two source of waves
            RIGHT * 2 + DOWN * 5,
            checkerboard_colors=[BLUE_D],
            stroke_width=0,
        )
        self.add(wave)
        wave.start_wave()
        self.wait()
        wave.stop_wave()
```

<pre data-manim-binder data-manim-classname="RadialWaveExampleScene">
class RadialWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 \* DEGREES, -45 \* DEGREES)
        wave = RadialWave(
            LEFT \* 2 + DOWN \* 5,  # Two source of waves
            RIGHT \* 2 + DOWN \* 5,
            checkerboard_colors=[BLUE_D],
            stroke_width=0,
        )
        self.add(wave)
        wave.start_wave()
        self.wait()
        wave.stop_wave()

</pre></div>

### Methods

| [`start_wave`](#manim_physics.wave.RadialWave.start_wave)   | Animate the wave propagation.        |
|-------------------------------------------------------------|--------------------------------------|
| [`stop_wave`](#manim_physics.wave.RadialWave.stop_wave)     | Stop animating the wave propagation. |

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

#### start_wave()

Animate the wave propagation.

#### stop_wave()

Stop animating the wave propagation.
