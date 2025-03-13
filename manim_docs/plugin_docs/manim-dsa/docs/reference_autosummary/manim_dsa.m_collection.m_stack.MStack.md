# MStack

Qualified name: `manim\_dsa.m\_collection.m\_stack.MStack`

### *class* MStack(arr=[], buff=0.1, style=<manim_dsa.constants.MStackStyle._DefaultStyle object>)

Bases: `MCollection`

Manim Stack: a class for visualizing the stack structure using the Manim animation engine.

* **Parameters:**
  * **arr** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *,* *optional*) – The initial list of values to populate the stack. Default is an empty list.
  * **buff** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The buffer (margin) between elements in the stack. Default is 0.1.
  * **style** (*MStackStyle._DefaultStyle* *,* *optional*) – The style configuration for the stack elements. Default is MStackStyle.DEFAULT.

### Methods

| [`add_label`](#manim_dsa.m_collection.m_stack.MStack.add_label)             | Adds a label to the stack.                               |
|-----------------------------------------------------------------------------|----------------------------------------------------------|
| [`append`](#manim_dsa.m_collection.m_stack.MStack.append)                   | Appends a new value to the top of the stack.             |
| [`get_spawn_point`](#manim_dsa.m_collection.m_stack.MStack.get_spawn_point) | Calculates the drop point for new elements in the stack. |
| [`pop`](#manim_dsa.m_collection.m_stack.MStack.pop)                         | Removes the top element from the stack.                  |

### Inherited Attributes

| `animate`            | Used to animate the application of any method of `self`.               |
|----------------------|------------------------------------------------------------------------|
| `color`              |                                                                        |
| `depth`              | The depth of the mobject.                                              |
| `fill_color`         | If there are multiple colors (for gradient) this returns the first one |
| `height`             | The height of the mobject.                                             |
| `n_points_per_curve` |                                                                        |
| `sheen_factor`       |                                                                        |
| `stroke_color`       |                                                                        |
| `width`              | The width of the mobject.                                              |

#### add_label(text, direction=array([0., 1., 0.]), buff=0.5, \*\*kwargs)

Adds a label to the stack.

* **Parameters:**
  * **text** (*Text*) – The label text.
  * **direction** (*Vector3D* *,* *optional*) – The direction in which to position the label. Default is UP.
  * **buff** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The distance (buffer) between the stack and the label. Default is 0.5.
  * **\*\*kwargs** – Additional keyword arguments that are passed to the function next_to() of the
    underlying add_label method.
* **Returns:**
  The instance of the [`MStack`](#manim_dsa.m_collection.m_stack.MStack) with the label added.
* **Return type:**
  self

#### append(value)

Appends a new value to the top of the stack.

* **Parameters:**
  **value** (*Any*) – The value to be added to the stack. It will be converted to a string representation.
* **Returns:**
  The instance of the [`MStack`](#manim_dsa.m_collection.m_stack.MStack) with the newly appended element.
* **Return type:**
  self

#### get_spawn_point()

Calculates the drop point for new elements in the stack.

* **Returns:**
  The spawn point position in 3D space.
* **Return type:**
  Point3D

#### pop()

Removes the top element from the stack.

* **Returns:**
  The instance of the [`MStack`](#manim_dsa.m_collection.m_stack.MStack) with the top element removed.
* **Return type:**
  self
