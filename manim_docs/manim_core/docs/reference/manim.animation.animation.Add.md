# Add

Qualified name: `manim.animation.animation.Add`

### *class* Add(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Add Mobjects to a scene, without animating them in any other way. This
is similar to the [`Scene.add()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.add) method, but [`Add`](#manim.animation.animation.Add) is an
animation which can be grouped into other animations.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – One [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) or more to add to a scene.
  * **run_time** (*float*) – The duration of the animation after adding the `mobjects`. Defaults
    to 0, which means this is an instant animation without extra wait time
    after adding them.
  * **\*\*kwargs** (*Any*) – Additional arguments to pass to the parent [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) class.

### Examples

<div id="defaultaddscene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DefaultAddScene <a class="headerlink" href="#defaultaddscene">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./DefaultAddScene-1.mp4">
</video>
```python
from manim import *

class DefaultAddScene(Scene):
    def construct(self):
        text_1 = Text("I was added with Add!")
        text_2 = Text("Me too!")
        text_3 = Text("And me!")
        texts = VGroup(text_1, text_2, text_3).arrange(DOWN)
        rect = SurroundingRectangle(texts, buff=0.5)

        self.play(
            Create(rect, run_time=3.0),
            Succession(
                Wait(1.0),
                # You can Add a Mobject in the middle of an animation...
                Add(text_1),
                Wait(1.0),
                # ...or multiple Mobjects at once!
                Add(text_2, text_3),
            ),
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="DefaultAddScene">
class DefaultAddScene(Scene):
    def construct(self):
        text_1 = Text("I was added with Add!")
        text_2 = Text("Me too!")
        text_3 = Text("And me!")
        texts = VGroup(text_1, text_2, text_3).arrange(DOWN)
        rect = SurroundingRectangle(texts, buff=0.5)

        self.play(
            Create(rect, run_time=3.0),
            Succession(
                Wait(1.0),
                # You can Add a Mobject in the middle of an animation...
                Add(text_1),
                Wait(1.0),
                # ...or multiple Mobjects at once!
                Add(text_2, text_3),
            ),
        )
        self.wait()

</pre></div><div id="addwithruntimescene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: AddWithRunTimeScene <a class="headerlink" href="#addwithruntimescene">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./AddWithRunTimeScene-1.mp4">
</video>
```python
from manim import *

class AddWithRunTimeScene(Scene):
    def construct(self):
        # A 5x5 grid of circles
        circles = VGroup(
            *[Circle(radius=0.5) for _ in range(25)]
        ).arrange_in_grid(5, 5)

        self.play(
            Succession(
                # Add a run_time of 0.2 to wait for 0.2 seconds after
                # adding the circle, instead of using Wait(0.2) after Add!
                *[Add(circle, run_time=0.2) for circle in circles],
                rate_func=smooth,
            )
        )
        self.wait()
```

<pre data-manim-binder data-manim-classname="AddWithRunTimeScene">
class AddWithRunTimeScene(Scene):
    def construct(self):
        # A 5x5 grid of circles
        circles = VGroup(
            \*[Circle(radius=0.5) for \_ in range(25)]
        ).arrange_in_grid(5, 5)

        self.play(
            Succession(
                # Add a run_time of 0.2 to wait for 0.2 seconds after
                # adding the circle, instead of using Wait(0.2) after Add!
                \*[Add(circle, run_time=0.2) for circle in circles],
                rate_func=smooth,
            )
        )
        self.wait()

</pre></div>

### Methods

| [`begin`](#manim.animation.animation.Add.begin)                             | Begin the animation.                                                                                      |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`clean_up_from_scene`](#manim.animation.animation.Add.clean_up_from_scene) | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| [`finish`](#manim.animation.animation.Add.finish)                           | Finish the animation.                                                                                     |
| [`interpolate`](#manim.animation.animation.Add.interpolate)                 | Set the animation progress.                                                                               |
| [`update_mobjects`](#manim.animation.animation.Add.update_mobjects)         | Updates things like starting_mobject, and (for Transforms) target_mobject.                                |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(\*mobjects, run_time=0.0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **run_time** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None

#### clean_up_from_scene(scene)

Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.

This includes to [`remove()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is a remover.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene the animation should be cleaned up from.
* **Return type:**
  None

#### finish()

Finish the animation.

This method gets called when the animation is over.

* **Return type:**
  None

#### interpolate(alpha)

Set the animation progress.

This method gets called for every frame during an animation.

* **Parameters:**
  **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
  the end.
* **Return type:**
  None

#### update_mobjects(dt)

Updates things like starting_mobject, and (for
Transforms) target_mobject.  Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.

* **Parameters:**
  **dt** (*float*)
* **Return type:**
  None
