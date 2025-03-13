# Matrix

Qualified name: `manim.mobject.matrix.Matrix`

### *class* Matrix(matrix, v_buff=0.8, h_buff=1.3, bracket_h_buff=0.25, bracket_v_buff=0.25, add_background_rectangles_to_entries=False, include_background_rectangle=False, element_to_mobject=<class 'manim.mobject.text.tex_mobject.MathTex'>, element_to_mobject_config={}, element_alignment_corner=array([ 1., -1., 0.]), left_bracket='[', right_bracket=']', stretch_brackets=True, bracket_config={}, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A mobject that displays a matrix on the screen.

* **Parameters:**
  * **matrix** (*Iterable*) – A numpy 2d array or list of lists.
  * **v_buff** (*float*) – Vertical distance between elements, by default 0.8.
  * **h_buff** (*float*) – Horizontal distance between elements, by default 1.3.
  * **bracket_h_buff** (*float*) – Distance of the brackets from the matrix, by default `MED_SMALL_BUFF`.
  * **bracket_v_buff** (*float*) – Height of the brackets, by default `MED_SMALL_BUFF`.
  * **add_background_rectangles_to_entries** (*bool*) – `True` if should add backgraound rectangles to entries, by default `False`.
  * **include_background_rectangle** (*bool*) – `True` if should include background rectangle, by default `False`.
  * **element_to_mobject** (*type* *[*[*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *]*) – The mobject class used to construct the elements, by default [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
  * **element_to_mobject_config** (*dict*) – Additional arguments to be passed to the constructor in `element_to_mobject`,
    by default `{}`.
  * **element_alignment_corner** (*Sequence* *[**float* *]*) – The corner to which elements are aligned, by default `DR`.
  * **left_bracket** (*str*) – The left bracket type, by default `"["`.
  * **right_bracket** (*str*) – The right bracket type, by default `"]"`.
  * **stretch_brackets** (*bool*) – `True` if should stretch the brackets to fit the height of matrix contents, by default `True`.
  * **bracket_config** (*dict*) – Additional arguments to be passed to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) when constructing
    the brackets.

### Examples

The first example shows a variety of uses of this module while the second example
exlpains the use of the options add_background_rectangles_to_entries and
include_background_rectangle.

<div id="matrixexamples" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MatrixExamples <a class="headerlink" href="#matrixexamples">¶</a></p>![image](media/images/MatrixExamples-2.png)
```python
from manim import *

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([[2, r"\pi"], [-1, 1]])
        m1 = Matrix([[2, 0, 4], [-1, 1, 5]],
            v_buff=1.3,
            h_buff=0.8,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF,
            left_bracket=r"\{",
            right_bracket=r"\}")
        m1.add(SurroundingRectangle(m1.get_columns()[1]))
        m2 = Matrix([[2, 1], [-1, 3]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        m3 = Matrix([[2, 1], [-1, 3]],
            left_bracket=r"\langle",
            right_bracket=r"\rangle")
        m4 = Matrix([[2, 1], [-1, 3]],
        ).set_column_colors(RED, GREEN)
        m5 = Matrix([[2, 1], [-1, 3]],
        ).set_row_colors(RED, GREEN)
        g = Group(
            m0,m1,m2,m3,m4,m5
        ).arrange_in_grid(buff=2)
        self.add(g)
```

<pre data-manim-binder data-manim-classname="MatrixExamples">
class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([[2, r"\\pi"], [-1, 1]])
        m1 = Matrix([[2, 0, 4], [-1, 1, 5]],
            v_buff=1.3,
            h_buff=0.8,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF,
            left_bracket=r"\\{",
            right_bracket=r"\\}")
        m1.add(SurroundingRectangle(m1.get_columns()[1]))
        m2 = Matrix([[2, 1], [-1, 3]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        m3 = Matrix([[2, 1], [-1, 3]],
            left_bracket=r"\\langle",
            right_bracket=r"\\rangle")
        m4 = Matrix([[2, 1], [-1, 3]],
        ).set_column_colors(RED, GREEN)
        m5 = Matrix([[2, 1], [-1, 3]],
        ).set_row_colors(RED, GREEN)
        g = Group(
            m0,m1,m2,m3,m4,m5
        ).arrange_in_grid(buff=2)
        self.add(g)

</pre></div><div id="backgroundrectanglesexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: BackgroundRectanglesExample <a class="headerlink" href="#backgroundrectanglesexample">¶</a></p>![image](media/images/BackgroundRectanglesExample-1.png)
```python
from manim import *

class BackgroundRectanglesExample(Scene):
    def construct(self):
        background= Rectangle().scale(3.2)
        background.set_fill(opacity=.5)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)
        m0 = Matrix([[12, -30], [-1, 15]],
            add_background_rectangles_to_entries=True)
        m1 = Matrix([[2, 0], [-1, 1]],
            include_background_rectangle=True)
        m2 = Matrix([[12, -30], [-1, 15]])
        g = Group(m0, m1, m2).arrange(buff=2)
        self.add(g)
```

<pre data-manim-binder data-manim-classname="BackgroundRectanglesExample">
class BackgroundRectanglesExample(Scene):
    def construct(self):
        background= Rectangle().scale(3.2)
        background.set_fill(opacity=.5)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)
        m0 = Matrix([[12, -30], [-1, 15]],
            add_background_rectangles_to_entries=True)
        m1 = Matrix([[2, 0], [-1, 1]],
            include_background_rectangle=True)
        m2 = Matrix([[12, -30], [-1, 15]])
        g = Group(m0, m1, m2).arrange(buff=2)
        self.add(g)

</pre></div>

### Methods

| [`add_background_to_entries`](#manim.mobject.matrix.Matrix.add_background_to_entries)   | Add a black background rectangle to the matrix, see above for an example.   |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`get_brackets`](#manim.mobject.matrix.Matrix.get_brackets)                             | Return the bracket mobjects.                                                |
| [`get_columns`](#manim.mobject.matrix.Matrix.get_columns)                               | Return columns of the matrix as VGroups.                                    |
| [`get_entries`](#manim.mobject.matrix.Matrix.get_entries)                               | Return the individual entries of the matrix.                                |
| [`get_mob_matrix`](#manim.mobject.matrix.Matrix.get_mob_matrix)                         | Return the underlying mob matrix mobjects.                                  |
| [`get_rows`](#manim.mobject.matrix.Matrix.get_rows)                                     | Return rows of the matrix as VGroups.                                       |
| [`set_column_colors`](#manim.mobject.matrix.Matrix.set_column_colors)                   | Set individual colors for each columns of the matrix.                       |
| [`set_row_colors`](#manim.mobject.matrix.Matrix.set_row_colors)                         | Set individual colors for each row of the matrix.                           |

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

#### \_add_brackets(left='[', right=']', \*\*kwargs)

Adds the brackets to the Matrix mobject.

See Latex document for various bracket types.

* **Parameters:**
  * **left** (*str*) – the left bracket, by default “[”
  * **right** (*str*) – the right bracket, by default “]”
* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

#### \_original_\_init_\_(matrix, v_buff=0.8, h_buff=1.3, bracket_h_buff=0.25, bracket_v_buff=0.25, add_background_rectangles_to_entries=False, include_background_rectangle=False, element_to_mobject=<class 'manim.mobject.text.tex_mobject.MathTex'>, element_to_mobject_config={}, element_alignment_corner=array([ 1., -1., 0.]), left_bracket='[', right_bracket=']', stretch_brackets=True, bracket_config={}, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **matrix** (*Iterable*)
  * **v_buff** (*float*)
  * **h_buff** (*float*)
  * **bracket_h_buff** (*float*)
  * **bracket_v_buff** (*float*)
  * **add_background_rectangles_to_entries** (*bool*)
  * **include_background_rectangle** (*bool*)
  * **element_to_mobject** (*type* *[*[*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *]*)
  * **element_to_mobject_config** (*dict*)
  * **element_alignment_corner** (*Sequence* *[**float* *]*)
  * **left_bracket** (*str*)
  * **right_bracket** (*str*)
  * **stretch_brackets** (*bool*)
  * **bracket_config** (*dict*)

#### add_background_to_entries()

Add a black background rectangle to the matrix,
see above for an example.

* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

#### get_brackets()

Return the bracket mobjects.

* **Returns:**
  Each VGroup contains a bracket
* **Return type:**
  List[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

### Examples

<div id="getbracketsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GetBracketsExample <a class="headerlink" href="#getbracketsexample">¶</a></p>![image](media/images/GetBracketsExample-1.png)
```python
from manim import *

class GetBracketsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 3], [1, 5]])
        bra = m0.get_brackets()
        colors = [BLUE, GREEN]
        for k in range(len(colors)):
            bra[k].set_color(colors[k])
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="GetBracketsExample">
class GetBracketsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\\\pi", 3], [1, 5]])
        bra = m0.get_brackets()
        colors = [BLUE, GREEN]
        for k in range(len(colors)):
            bra[k].set_color(colors[k])
        self.add(m0)

</pre></div>

#### get_columns()

Return columns of the matrix as VGroups.

* **Returns:**
  Each VGroup contains a column of the matrix.
* **Return type:**
  List[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

### Examples

<div id="getcolumnsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GetColumnsExample <a class="headerlink" href="#getcolumnsexample">¶</a></p>![image](media/images/GetColumnsExample-1.png)
```python
from manim import *

class GetColumnsExample(Scene):
    def construct(self):
        m0 = Matrix([[r"\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_columns()[1]))
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="GetColumnsExample">
class GetColumnsExample(Scene):
    def construct(self):
        m0 = Matrix([[r"\\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_columns()[1]))
        self.add(m0)

</pre></div>

#### get_entries()

Return the individual entries of the matrix.

* **Returns:**
  VGroup containing entries of the matrix.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

<div id="getentriesexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GetEntriesExample <a class="headerlink" href="#getentriesexample">¶</a></p>![image](media/images/GetEntriesExample-1.png)
```python
from manim import *

class GetEntriesExample(Scene):
    def construct(self):
        m0 = Matrix([[2, 3], [1, 5]])
        ent = m0.get_entries()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            ent[k].set_color(colors[k])
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="GetEntriesExample">
class GetEntriesExample(Scene):
    def construct(self):
        m0 = Matrix([[2, 3], [1, 5]])
        ent = m0.get_entries()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            ent[k].set_color(colors[k])
        self.add(m0)

</pre></div>

#### get_mob_matrix()

Return the underlying mob matrix mobjects.

* **Returns:**
  Each VGroup contains a row of the matrix.
* **Return type:**
  List[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

#### get_rows()

Return rows of the matrix as VGroups.

* **Returns:**
  Each VGroup contains a row of the matrix.
* **Return type:**
  List[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

### Examples

<div id="getrowsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GetRowsExample <a class="headerlink" href="#getrowsexample">¶</a></p>![image](media/images/GetRowsExample-1.png)
```python
from manim import *

class GetRowsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_rows()[1]))
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="GetRowsExample">
class GetRowsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\\\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_rows()[1]))
        self.add(m0)

</pre></div>

#### set_column_colors(\*colors)

Set individual colors for each columns of the matrix.

* **Parameters:**
  **colors** (*str*) – The list of colors; each color specified corresponds to a column.
* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

### Examples

<div id="setcolumncolorsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SetColumnColorsExample <a class="headerlink" href="#setcolumncolorsexample">¶</a></p>![image](media/images/SetColumnColorsExample-1.png)
```python
from manim import *

class SetColumnColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 1], [-1, 3]],
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="SetColumnColorsExample">
class SetColumnColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\\\pi", 1], [-1, 3]],
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(m0)

</pre></div>

#### set_row_colors(\*colors)

Set individual colors for each row of the matrix.

* **Parameters:**
  **colors** (*str*) – The list of colors; each color specified corresponds to a row.
* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

### Examples

<div id="setrowcolorsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SetRowColorsExample <a class="headerlink" href="#setrowcolorsexample">¶</a></p>![image](media/images/SetRowColorsExample-1.png)
```python
from manim import *

class SetRowColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 1], [-1, 3]],
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(m0)
```

<pre data-manim-binder data-manim-classname="SetRowColorsExample">
class SetRowColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\\\pi", 1], [-1, 3]],
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(m0)

</pre></div>
