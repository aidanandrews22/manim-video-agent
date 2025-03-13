# MArray

Qualified name: `manim\_dsa.m\_collection.m\_array.MArray`

### *class* MArray(arr=[], direction=array([1., 0., 0.]), style=<manim_dsa.constants.MArrayStyle._DefaultStyle object>)

Bases: `MCollection`

Manim Array: a class for visualizing the array structure using the Manim animation engine.

* **Parameters:**
  * **arr** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *,* *optional*) – The initial list of values to populate the array. Default is an empty list.
  * **direction** (*Vector3D* *,* *optional*) – The direction in which to arrange the elements. Default is RIGHT.
  * **margin** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The margin between elements in the array. Default is 0.
  * **style** (*MArrayStyle._DefaultStyle* *,* *optional*) – The style configuration for the elements. Default is MArrayStyle.DEFAULT.

### Methods

| [`add_indexes`](#manim_dsa.m_collection.m_array.MArray.add_indexes)   | Adds indexes to each element in the array, displaying them in the specified direction.     |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [`append`](#manim_dsa.m_collection.m_array.MArray.append)             | Appends a new element to the end of the array.                                             |
| [`pop`](#manim_dsa.m_collection.m_array.MArray.pop)                   | Removes the element at the specified index and shifts all subsequent elements accordingly. |

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

#### add_indexes(direction=array([0., 1., 0.]), buff=0.25)

Adds indexes to each element in the array, displaying them in the specified direction.

* **Parameters:**
  * **direction** (*Vector3D* *,* *optional*) – The direction in which to display the indices relative to the elements.
    Default is UP.
  * **buff** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The buffer distance between the element and its index.
    Default is DEFAULT_MOBJECT_TO_MOBJECT_BUFFER.
* **Returns:**
  The instance of the [`MArray`](#manim_dsa.m_collection.m_array.MArray) with the specified element removed.
* **Return type:**
  self
* **Raises:**
  [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception) – If the specified direction is parallel to the array’s growth direction.

### Notes

If indices are already enabled, this method returns immediately without making any changes.

#### append(value)

Appends a new element to the end of the array. If indexing is enabled,
the new element will also be assigned an index based on its position in the array.

* **Parameters:**
  **value** (*Any*) – The value to append. It will be converted to a string representation.
* **Returns:**
  The instance of the [`MArray`](#manim_dsa.m_collection.m_array.MArray) with the newly appended element.
* **Return type:**
  self

#### pop(index=-1)

Removes the element at the specified index and shifts all subsequent elements accordingly.
If indexing is enabled, it also updates the indices of the remaining elements.

* **Parameters:**
  **index** ([*int*](https://docs.python.org/3/library/functions.html#int) *,* *optional*) – The index of the element to be removed. Default is -1, which removes the last element.
* **Returns:**
  The instance of the [`MArray`](#manim_dsa.m_collection.m_array.MArray) with the specified element removed.
* **Return type:**
  self
