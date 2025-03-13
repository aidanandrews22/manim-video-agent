# Labelable

Qualified name: `manim\_dsa.utils.utils.Labelable`

### *class* Labelable

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A mixin class that provides functionality to add a label to Manim objects.

#### label

The label associated with the object, if any.

* **Type:**
  Text or None

### Methods

| [`add_label`](#manim_dsa.utils.utils.Labelable.add_label)   | Add a label to the object.       |
|-------------------------------------------------------------|----------------------------------|
| [`has_label`](#manim_dsa.utils.utils.Labelable.has_label)   | Check if the object has a label. |

#### add_label(text, direction=array([0., 1., 0.]), buff=0.5, \*\*kwargs)

Add a label to the object.

* **Parameters:**
  * **text** (*Text*) – The Text object to use as the label.
  * **direction** (*Vector3D* *,* *optional*) – The direction to place the label relative to the object (default is UP).
  * **buff** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The distance between the object and the label (default is 0.5).
  * **\*\*kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Additional keyword arguments for positioning.
* **Returns:**
  The instance with the label added.
* **Return type:**
  [Labelable](#manim_dsa.utils.utils.Labelable)

#### has_label()

Check if the object has a label.

* **Returns:**
  True if the object has a label, otherwise False.
* **Return type:**
  [bool](https://docs.python.org/3/library/functions.html#bool)
