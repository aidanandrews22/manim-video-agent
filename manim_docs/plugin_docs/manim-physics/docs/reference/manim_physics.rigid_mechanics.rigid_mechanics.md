# rigid_mechanics

A gravity simulation space.

Most objects can be made into a rigid body (moves according to gravity
and collision) or a static body (stays still within the scene).

To use this feature, the [`SpaceScene`](manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene.md#manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene) must be used, to access
the specific functions of the space.

#### NOTE
* This feature utilizes the pymunk package. Although unnecessary,
  it might make it easier if you knew a few things on how to use it.

  [Official Documentation](http://www.pymunk.org/en/latest/pymunk.html)

  [Youtube Tutorial](https://youtu.be/pRk---rdrbo)
* A low frame rate might cause some objects to pass static objects as
  they don’t register collisions finely enough. Trying to increase the
  config frame rate might solve the problem.

### Examples

<div id="twoobjectsfalling" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TwoObjectsFalling <a class="headerlink" href="#twoobjectsfalling">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./TwoObjectsFalling-1.mp4">
</video>
```python
from manim import *

from manim_physics import *
# use a SpaceScene to utilize all specific rigid-mechanics methods
class TwoObjectsFalling(SpaceScene):
    def construct(self):
        circle = Circle().shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)

        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)

        ground = Line([-4, -3.5, 0], [4, -3.5, 0])
        wall1 = Line([-4, -3.5, 0], [-4, 3.5, 0])
        wall2 = Line([4, -3.5, 0], [4, 3.5, 0])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(rect),
        )
        self.make_rigid_body(rect, circle)  # Mobjects will move with gravity
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(5)
        # during wait time, the circle and rect would move according to the simulate updater
```

<pre data-manim-binder data-manim-classname="TwoObjectsFalling">
from manim_physics import \*
# use a SpaceScene to utilize all specific rigid-mechanics methods
class TwoObjectsFalling(SpaceScene):
    def construct(self):
        circle = Circle().shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)

        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP \* 2)
        rect.scale(0.5)

        ground = Line([-4, -3.5, 0], [4, -3.5, 0])
        wall1 = Line([-4, -3.5, 0], [-4, 3.5, 0])
        wall2 = Line([4, -3.5, 0], [4, 3.5, 0])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(rect),
        )
        self.make_rigid_body(rect, circle)  # Mobjects will move with gravity
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(5)
        # during wait time, the circle and rect would move according to the simulate updater

</pre></div>

### Classes

| [`Space`](manim_physics.rigid_mechanics.rigid_mechanics.Space.md#manim_physics.rigid_mechanics.rigid_mechanics.Space)                | An Abstract object for gravity.           |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [`SpaceScene`](manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene.md#manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene) | A basis scene for all of rigid mechanics. |

### Functions

### get_angle(mob)

Obtains the angle of the body from the mobject.
Used internally for updaters.

* **Parameters:**
  **mob** (*VMobject*)
* **Return type:**
  None

### get_shape(mob)

Obtains the shape of the body from the mobject

* **Parameters:**
  **mob** (*VMobject*)
* **Return type:**
  None
