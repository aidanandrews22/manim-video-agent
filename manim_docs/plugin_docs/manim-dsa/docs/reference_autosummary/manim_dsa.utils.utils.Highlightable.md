# Highlightable

Qualified name: `manim\_dsa.utils.utils.Highlightable`

### *class* Highlightable

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A mixin class that provides functionality to highlight and unhighlight Manim objects.

#### highlighting

The highlight effect associated with the object, if any.

* **Type:**
  VMobject or None

### Methods

| [`highlight`](#manim_dsa.utils.utils.Highlightable.highlight)         | Highlight the object with the specified stroke color and width.   |
|-----------------------------------------------------------------------|-------------------------------------------------------------------|
| [`set_highlight`](#manim_dsa.utils.utils.Highlightable.set_highlight) | Set the highlight properties.                                     |
| [`unhighlight`](#manim_dsa.utils.utils.Highlightable.unhighlight)     | Remove the highlight from the object.                             |

#### highlight(stroke_color=ManimColor('#FC6255'), stroke_width=8)

Highlight the object with the specified stroke color and width.

* **Parameters:**
  * **stroke_color** (*ManimColor* *,* *optional*) – The color of the highlight stroke (default is RED).
  * **stroke_width** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The width of the highlight stroke (default is 8).
* **Returns:**
  The instance with the highlight applied.
* **Return type:**
  [Highlightable](#manim_dsa.utils.utils.Highlightable)

#### set_highlight(stroke_color=ManimColor('#FC6255'), stroke_width=8)

Set the highlight properties.

* **Parameters:**
  * **stroke_color** (*ManimColor* *,* *optional*) – The color of the highlight stroke (default is RED).
  * **stroke_width** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The width of the highlight stroke (default is 8).

#### unhighlight()

Remove the highlight from the object.

* **Returns:**
  The instance with the highlight removed.
* **Return type:**
  [Highlightable](#manim_dsa.utils.utils.Highlightable)
