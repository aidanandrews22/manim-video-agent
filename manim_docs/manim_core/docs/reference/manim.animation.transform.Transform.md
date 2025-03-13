# Transform

Qualified name: `manim.animation.transform.Transform`

### *class* Transform(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

A Transform transforms a Mobject into a target Mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) to be transformed. It will be mutated to become the `target_mobject`.
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*) – The target of the transformation.
  * **path_func** (*Callable* *|* *None*) – A function defining the path that the points of the `mobject` are being moved
    along until they match the points of the `target_mobject`, see [`utils.paths`](manim.utils.paths.md#module-manim.utils.paths).
  * **path_arc** (*float*) – The arc angle (in radians) that the points of `mobject` will follow to reach
    the points of the target if using a circular path arc, see `path_arc_centers`.
    See also [`manim.utils.paths.path_along_arc()`](manim.utils.paths.md#manim.utils.paths.path_along_arc).
  * **path_arc_axis** (*np.ndarray*) – The axis to rotate along if using a circular path arc, see `path_arc_centers`.
  * **path_arc_centers** (*np.ndarray*) – 

    The center of the circular arcs along which the points of `mobject` are
    moved by the transformation.

    If this is set and `path_func` is not set, then a `path_along_circles` path will be generated
    using the `path_arc` parameters and stored in `path_func`. If `path_func` is set, this and the
    other `path_arc` fields are set as attributes, but a `path_func` is not generated from it.
  * **replace_mobject_with_target_in_scene** (*bool*) – 

    Controls which mobject is replaced when the transformation is complete.

    If set to True, `mobject` will be removed from the scene and `target_mobject` will
    replace it. Otherwise, `target_mobject` is never added and `mobject` just takes its shape.

### Examples

<div id="transformpatharc" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TransformPathArc <a class="headerlink" href="#transformpatharc">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./TransformPathArc-1.mp4">
</video>
```python
from manim import *

class TransformPathArc(Scene):
    def construct(self):
        def make_arc_path(start, end, arc_angle):
            points = []
            p_fn = path_along_arc(arc_angle)
            # alpha animates between 0.0 and 1.0, where 0.0
            # is the beginning of the animation and 1.0 is the end.
            for alpha in range(0, 11):
                points.append(p_fn(start, end, alpha / 10.0))
            path = VMobject(stroke_color=YELLOW)
            path.set_points_smoothly(points)
            return path

        left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
        colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
        # Positive angles move counter-clockwise, negative angles move clockwise.
        examples = [-90, 0, 30, 90, 180, 270]
        anims = []
        for idx, angle in enumerate(examples):
            left_c = left.copy().shift((3 - idx) * UP)
            left_c.fill_color = colors[idx]
            right_c = left_c.copy().shift(4 * RIGHT)
            path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                                     arc_angle=angle * DEGREES)
            desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
            # Make the circles in front of the text in front of the arcs.
            self.add(
                path_arc.set_z_index(1),
                desc.set_z_index(2),
                left_c.set_z_index(3),
            )
            anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))

        self.play(*anims, run_time=2)
        self.wait()
```

<pre data-manim-binder data-manim-classname="TransformPathArc">
class TransformPathArc(Scene):
    def construct(self):
        def make_arc_path(start, end, arc_angle):
            points = []
            p_fn = path_along_arc(arc_angle)
            # alpha animates between 0.0 and 1.0, where 0.0
            # is the beginning of the animation and 1.0 is the end.
            for alpha in range(0, 11):
                points.append(p_fn(start, end, alpha / 10.0))
            path = VMobject(stroke_color=YELLOW)
            path.set_points_smoothly(points)
            return path

        left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT \* 2)
        colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
        # Positive angles move counter-clockwise, negative angles move clockwise.
        examples = [-90, 0, 30, 90, 180, 270]
        anims = []
        for idx, angle in enumerate(examples):
            left_c = left.copy().shift((3 - idx) \* UP)
            left_c.fill_color = colors[idx]
            right_c = left_c.copy().shift(4 \* RIGHT)
            path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                                     arc_angle=angle \* DEGREES)
            desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
            # Make the circles in front of the text in front of the arcs.
            self.add(
                path_arc.set_z_index(1),
                desc.set_z_index(2),
                left_c.set_z_index(3),
            )
            anims.append(Transform(left_c, right_c, path_arc=angle \* DEGREES))

        self.play(\*anims, run_time=2)
        self.wait()

</pre></div>

### Methods

| [`begin`](#manim.animation.transform.Transform.begin)                             | Begin the animation.                                                                                      |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`clean_up_from_scene`](#manim.animation.transform.Transform.clean_up_from_scene) | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| `create_target`                                                                   |                                                                                                           |
| `get_all_families_zipped`                                                         |                                                                                                           |
| [`get_all_mobjects`](#manim.animation.transform.Transform.get_all_mobjects)       | Get all mobjects involved in the animation.                                                               |
| `interpolate_submobject`                                                          |                                                                                                           |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, target_mobject=None, path_func=None, path_arc=0, path_arc_axis=array([0., 0., 1.]), path_arc_centers=None, replace_mobject_with_target_in_scene=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*)
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*)
  * **path_func** (*Callable* *|* *None*)
  * **path_arc** (*float*)
  * **path_arc_axis** (*ndarray*)
  * **path_arc_centers** (*ndarray*)
  * **replace_mobject_with_target_in_scene** (*bool*)
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

#### get_all_mobjects()

Get all mobjects involved in the animation.

Ordering must match the ordering of arguments to interpolate_submobject

* **Returns:**
  The sequence of mobjects.
* **Return type:**
  Sequence[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]
