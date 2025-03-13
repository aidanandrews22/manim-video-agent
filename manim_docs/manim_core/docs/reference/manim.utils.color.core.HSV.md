# HSV

Qualified name: `manim.utils.color.core.HSV`

### *class* HSV(hsv, alpha=1.0)

Bases: [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

HSV Color Space

### Methods

### Attributes

| `h`          |    |
|--------------|----|
| `hue`        |    |
| `s`          |    |
| `saturation` |    |
| `v`          |    |
| `value`      |    |
* **Parameters:**
  * **hsv** ([*HSV_Array_Float*](manim.typing.md#manim.typing.HSV_Array_Float) *|* [*HSV_Tuple_Float*](manim.typing.md#manim.typing.HSV_Tuple_Float) *|* [*HSVA_Array_Float*](manim.typing.md#manim.typing.HSVA_Array_Float) *|* [*HSVA_Tuple_Float*](manim.typing.md#manim.typing.HSVA_Tuple_Float))
  * **alpha** (*float*)

#### *classmethod* \_from_internal(value)

This method is intended to be overwritten by custom color space classes
which are subtypes of [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).

The method constructs a new object of the given class by transforming the value
in the internal format `[r,g,b,a]` into a format which the constructor of the
custom class can understand. Look at [`HSV`](#manim.utils.color.core.HSV) for an example.

* **Parameters:**
  **value** ([*ManimColorInternal*](manim.typing.md#manim.typing.ManimColorInternal))
* **Return type:**
  *Self*

#### *property* \_internal_space *: ndarray[Any, dtype[\_ScalarType_co]]*

This is a readonly property which is a custom representation for color space
operations. It is used for operators and can be used when implementing a custom
color space.

#### *property* \_internal_value *: [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)*

Return the internal value of the current [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) as an
`[r,g,b,a]` float array.

* **Returns:**
  Internal color representation.
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)
