# LinearTransformationScene

Qualified name: `manim.scene.vector\_space\_scene.LinearTransformationScene`

### *class* LinearTransformationScene(include_background_plane=True, include_foreground_plane=True, background_plane_kwargs=None, foreground_plane_kwargs=None, show_coordinates=False, show_basis_vectors=True, basis_vector_stroke_width=6, i_hat_color=ManimColor('#83C167'), j_hat_color=ManimColor('#FC6255'), leave_ghost_vectors=False, \*\*kwargs)

Bases: [`VectorScene`](manim.scene.vector_space_scene.VectorScene.md#manim.scene.vector_space_scene.VectorScene)

This scene contains special methods that make it
especially suitable for showing linear transformations.

* **Parameters:**
  * **include_background_plane** (*bool*) – Whether or not to include the background plane in the scene.
  * **include_foreground_plane** (*bool*) – Whether or not to include the foreground plane in the scene.
  * **background_plane_kwargs** (*dict* *|* *None*) – Parameters to be passed to `NumberPlane` to adjust the background plane.
  * **foreground_plane_kwargs** (*dict* *|* *None*) – Parameters to be passed to `NumberPlane` to adjust the foreground plane.
  * **show_coordinates** (*bool*) – Whether or not to include the coordinates for the background plane.
  * **show_basis_vectors** (*bool*) – Whether to show the basis x_axis -> `i_hat` and y_axis -> `j_hat` vectors.
  * **basis_vector_stroke_width** (*float*) – The `stroke_width` of the basis vectors.
  * **i_hat_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the `i_hat` vector.
  * **j_hat_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the `j_hat` vector.
  * **leave_ghost_vectors** (*bool*) – Indicates the previous position of the basis vectors following a transformation.

### Examples

<div id="lineartransformationsceneexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LinearTransformationSceneExample <a class="headerlink" href="#lineartransformationsceneexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./LinearTransformationSceneExample-1.mp4">
</video>
```python
from manim import *

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()
```

<pre data-manim-binder data-manim-classname="LinearTransformationSceneExample">
class LinearTransformationSceneExample(LinearTransformationScene):
    def \_\_init_\_(self, \*\*kwargs):
        LinearTransformationScene._\_init_\_(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            \*\*kwargs
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()

</pre></div>

### Methods

| [`add_background_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_background_mobject)                             | Adds the mobjects to the special list self.background_mobjects.                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_foreground_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_foreground_mobject)                             | Adds the mobjects to the special list self.foreground_mobjects.                                                                                                                       |
| [`add_moving_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_moving_mobject)                                     | Adds the mobject to the special list self.moving_mobject, and adds a property to the mobject called mobject.target, which keeps track of what the mobject will move to or become etc. |
| [`add_special_mobjects`](#manim.scene.vector_space_scene.LinearTransformationScene.add_special_mobjects)                                 | Adds mobjects to a separate list that can be tracked, if these mobjects have some extra importance.                                                                                   |
| [`add_title`](#manim.scene.vector_space_scene.LinearTransformationScene.add_title)                                                       | Adds a title, after scaling it, adding a background rectangle, moving it to the top and adding it to foreground_mobjects adding it as a local variable of self.                       |
| [`add_transformable_label`](#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_label)                           | Method for creating, and animating the addition of a transformable label for the vector.                                                                                              |
| [`add_transformable_mobject`](#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_mobject)                       | Adds the mobjects to the special list self.transformable_mobjects.                                                                                                                    |
| [`add_unit_square`](#manim.scene.vector_space_scene.LinearTransformationScene.add_unit_square)                                           | Adds a unit square to the scene via self.get_unit_square.                                                                                                                             |
| [`add_vector`](#manim.scene.vector_space_scene.LinearTransformationScene.add_vector)                                                     | Adds a vector to the scene, and puts it in the special list self.moving_vectors.                                                                                                      |
| [`apply_function`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_function)                                             | Applies the given function to each of the mobjects in self.transformable_mobjects, and plays the animation showing this.                                                              |
| [`apply_inverse`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse)                                               | This method applies the linear transformation represented by the inverse of the passed matrix to the number plane, and each vector/similar mobject on it.                             |
| [`apply_inverse_transpose`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse_transpose)                           | Applies the inverse of the transformation represented by the given transposed matrix to the number plane and each vector/similar mobject on it.                                       |
| [`apply_matrix`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_matrix)                                                 | Applies the transformation represented by the given matrix to the number plane, and each vector/similar mobject on it.                                                                |
| [`apply_nonlinear_transformation`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_nonlinear_transformation)             | Applies the non-linear transformation represented by the given function to the number plane and each vector/similar mobject on it.                                                    |
| [`apply_transposed_matrix`](#manim.scene.vector_space_scene.LinearTransformationScene.apply_transposed_matrix)                           | Applies the transformation represented by the given transposed matrix to the number plane, and each vector/similar mobject on it.                                                     |
| [`get_ghost_vectors`](#manim.scene.vector_space_scene.LinearTransformationScene.get_ghost_vectors)                                       | Returns all ghost vectors ever added to `self`.                                                                                                                                       |
| [`get_matrix_transformation`](#manim.scene.vector_space_scene.LinearTransformationScene.get_matrix_transformation)                       | Returns a function corresponding to the linear transformation represented by the matrix passed.                                                                                       |
| [`get_moving_mobject_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_moving_mobject_movement)                   | This method returns an animation that moves a mobject in "self.moving_mobjects"  to its corresponding .target value.                                                                  |
| [`get_piece_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_piece_movement)                                     | This method returns an animation that moves an arbitrary mobject in "pieces" to its corresponding .target value.                                                                      |
| [`get_transformable_label_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_transformable_label_movement)         | This method returns an animation that moves all labels in "self.transformable_labels" to its corresponding .target .                                                                  |
| [`get_transposed_matrix_transformation`](#manim.scene.vector_space_scene.LinearTransformationScene.get_transposed_matrix_transformation) | Returns a function corresponding to the linear transformation represented by the transposed matrix passed.                                                                            |
| [`get_unit_square`](#manim.scene.vector_space_scene.LinearTransformationScene.get_unit_square)                                           | Returns a unit square for the current NumberPlane.                                                                                                                                    |
| [`get_vector_movement`](#manim.scene.vector_space_scene.LinearTransformationScene.get_vector_movement)                                   | This method returns an animation that moves a mobject in "self.moving_vectors"  to its corresponding .target value.                                                                   |
| [`setup`](#manim.scene.vector_space_scene.LinearTransformationScene.setup)                                                               | This is meant to be implemented by any scenes which are commonly subclassed, and have some common setup involved before the construct method is called.                               |
| `update_default_configs`                                                                                                                 |                                                                                                                                                                                       |
| [`write_vector_coordinates`](#manim.scene.vector_space_scene.LinearTransformationScene.write_vector_coordinates)                         | Returns a column matrix indicating the vector coordinates, after writing them to the screen, and adding them to the special list self.foreground_mobjects                             |

### Attributes

| `camera`   |                                        |
|------------|----------------------------------------|
| `time`     | The time since the start of the scene. |

#### add_background_mobject(\*mobjects)

Adds the mobjects to the special list
self.background_mobjects.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to add to the list.

#### add_foreground_mobject(\*mobjects)

Adds the mobjects to the special list
self.foreground_mobjects.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to add to the list

#### add_moving_mobject(mobject, target_mobject=None)

Adds the mobject to the special list
self.moving_mobject, and adds a property
to the mobject called mobject.target, which
keeps track of what the mobject will move to
or become etc.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to add to the list
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*) – What the moving_mobject goes to, etc.

#### add_special_mobjects(mob_list, \*mobs_to_add)

Adds mobjects to a separate list that can be tracked,
if these mobjects have some extra importance.

* **Parameters:**
  * **mob_list** (*list*) – The special list to which you want to add
    these mobjects.
  * **\*mobs_to_add** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to add.

#### add_title(title, scale_factor=1.5, animate=False)

Adds a title, after scaling it, adding a background rectangle,
moving it to the top and adding it to foreground_mobjects adding
it as a local variable of self. Returns the Scene.

* **Parameters:**
  * **title** (*str* *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)) – What the title should be.
  * **scale_factor** (*float*) – How much the title should be scaled by.
  * **animate** (*bool*) – Whether or not to animate the addition.
* **Returns:**
  The scene with the title added to it.
* **Return type:**
  [LinearTransformationScene](#manim.scene.vector_space_scene.LinearTransformationScene)

#### add_transformable_label(vector, label, transformation_name='L', new_label=None, \*\*kwargs)

Method for creating, and animating the addition of
a transformable label for the vector.

* **Parameters:**
  * **vector** ([*Vector*](manim.mobject.geometry.line.Vector.md#manim.mobject.geometry.line.Vector)) – The vector for which the label must be added.
  * **label** ([*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* *str*) – The MathTex/string of the label.
  * **transformation_name** (*str* *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)) – The name to give the transformation as a label.
  * **new_label** (*str* *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* *None*) – What the label should display after a Linear Transformation
  * **\*\*kwargs** – Any valid keyword argument of get_vector_label
* **Returns:**
  The MathTex of the label.
* **Return type:**
  [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

#### add_transformable_mobject(\*mobjects)

Adds the mobjects to the special list
self.transformable_mobjects.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to add to the list.

#### add_unit_square(animate=False, \*\*kwargs)

Adds a unit square to the scene via
self.get_unit_square.

* **Parameters:**
  * **animate** (*bool*) – Whether or not to animate the addition
    with DrawBorderThenFill.
  * **\*\*kwargs** – Any valid keyword arguments of
    self.get_unit_square()
* **Returns:**
  The unit square.
* **Return type:**
  [Square](manim.mobject.geometry.polygram.Square.md#manim.mobject.geometry.polygram.Square)

#### add_vector(vector, color=ManimColor('#FFFF00'), \*\*kwargs)

Adds a vector to the scene, and puts it in the special
list self.moving_vectors.

* **Parameters:**
  * **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow) *|* *list* *|* *tuple* *|* *ndarray*) – It can be a pre-made graphical vector, or the
    coordinates of one.
  * **color** (*str*) – The string of the hex color of the vector.
    This is only taken into consideration if
    ‘vector’ is not an Arrow. Defaults to YELLOW.
  * **\*\*kwargs** – Any valid keyword argument of VectorScene.add_vector.
* **Returns:**
  The arrow representing the vector.
* **Return type:**
  [Arrow](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)

#### apply_function(function, added_anims=[], \*\*kwargs)

Applies the given function to each of the mobjects in
self.transformable_mobjects, and plays the animation showing
this.

* **Parameters:**
  * **function** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function that affects each point
    of each mobject in self.transformable_mobjects.
  * **added_anims** (*list*) – Any other animations that need to be played
    simultaneously with this.
  * **\*\*kwargs** – Any valid keyword argument of a self.play() call.

#### apply_inverse(matrix, \*\*kwargs)

This method applies the linear transformation
represented by the inverse of the passed matrix
to the number plane, and each vector/similar mobject on it.

* **Parameters:**
  * **matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix whose inverse is to be applied.
  * **\*\*kwargs** – Any valid keyword argument of self.apply_matrix()

#### apply_inverse_transpose(t_matrix, \*\*kwargs)

Applies the inverse of the transformation represented
by the given transposed matrix to the number plane and each
vector/similar mobject on it.

* **Parameters:**
  * **t_matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.
  * **\*\*kwargs** – Any valid keyword argument of self.apply_transposed_matrix()

#### apply_matrix(matrix, \*\*kwargs)

Applies the transformation represented by the
given matrix to the number plane, and each vector/similar
mobject on it.

* **Parameters:**
  * **matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.
  * **\*\*kwargs** – Any valid keyword argument of self.apply_transposed_matrix()

#### apply_nonlinear_transformation(function, \*\*kwargs)

Applies the non-linear transformation represented
by the given function to the number plane and each
vector/similar mobject on it.

* **Parameters:**
  * **function** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function.
  * **\*\*kwargs** – Any valid keyword argument of self.apply_function()

#### apply_transposed_matrix(transposed_matrix, \*\*kwargs)

Applies the transformation represented by the
given transposed matrix to the number plane,
and each vector/similar mobject on it.

* **Parameters:**
  * **transposed_matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.
  * **\*\*kwargs** – Any valid keyword argument of self.apply_function()

#### get_ghost_vectors()

Returns all ghost vectors ever added to `self`. Each element is a `VGroup` of
two ghost vectors.

* **Return type:**
  [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### get_matrix_transformation(matrix)

Returns a function corresponding to the linear
transformation represented by the matrix passed.

* **Parameters:**
  **matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.

#### get_moving_mobject_movement(func)

This method returns an animation that moves a mobject
in “self.moving_mobjects”  to its corresponding .target value.
func is a function that determines where the .target goes.

* **Parameters:**
  **func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function that determines where the .target of
  the moving mobject goes.
* **Returns:**
  The animation of the movement.
* **Return type:**
  [Animation](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

#### get_piece_movement(pieces)

This method returns an animation that moves an arbitrary
mobject in “pieces” to its corresponding .target value.
If self.leave_ghost_vectors is True, ghosts of the original
positions/mobjects are left on screen

* **Parameters:**
  **pieces** (*list* *|* *tuple* *|* *ndarray*) – The pieces for which the movement must be shown.
* **Returns:**
  The animation of the movement.
* **Return type:**
  [Animation](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

#### get_transformable_label_movement()

This method returns an animation that moves all labels
in “self.transformable_labels” to its corresponding .target .

* **Returns:**
  The animation of the movement.
* **Return type:**
  [Animation](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

#### get_transposed_matrix_transformation(transposed_matrix)

Returns a function corresponding to the linear
transformation represented by the transposed
matrix passed.

* **Parameters:**
  **transposed_matrix** (*ndarray* *|* *list* *|* *tuple*) – The matrix.

#### get_unit_square(color=ManimColor('#FFFF00'), opacity=0.3, stroke_width=3)

Returns a unit square for the current NumberPlane.

* **Parameters:**
  * **color** (*str*) – The string of the hex color code of the color wanted.
  * **opacity** (*float*) – The opacity of the square
  * **stroke_width** (*float*) – The stroke_width in pixels of the border of the square
* **Return type:**
  [Square](manim.mobject.geometry.polygram.Square.md#manim.mobject.geometry.polygram.Square)

#### get_vector_movement(func)

This method returns an animation that moves a mobject
in “self.moving_vectors”  to its corresponding .target value.
func is a function that determines where the .target goes.

* **Parameters:**
  **func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function that determines where the .target of
  the moving mobject goes.
* **Returns:**
  The animation of the movement.
* **Return type:**
  [Animation](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

#### setup()

This is meant to be implemented by any scenes which
are commonly subclassed, and have some common setup
involved before the construct method is called.

#### write_vector_coordinates(vector, \*\*kwargs)

Returns a column matrix indicating the vector coordinates,
after writing them to the screen, and adding them to the
special list self.foreground_mobjects

* **Parameters:**
  * **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)) – The arrow representing the vector.
  * **\*\*kwargs** – Any valid keyword arguments of VectorScene.write_vector_coordinates
* **Returns:**
  The column matrix representing the vector.
* **Return type:**
  [Matrix](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)
