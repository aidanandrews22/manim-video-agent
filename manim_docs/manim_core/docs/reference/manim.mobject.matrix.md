# matrix

Mobjects representing matrices.

### Examples

<div id="matrixexamples" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MatrixExamples <a class="headerlink" href="#matrixexamples">¶</a></p>![image](media/images/MatrixExamples-1.png)
```python
from manim import *

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 0], [-1, 1]])
        m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
            left_bracket="(",
            right_bracket=")")
        m2 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket=r"\{",
            right_bracket=r"\}")
        m3 = MobjectMatrix(
            [[Circle().scale(0.3), Square().scale(0.3)],
            [MathTex("\\pi").scale(2), Star().scale(0.3)]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
        self.add(g)
```

<pre data-manim-binder data-manim-classname="MatrixExamples">
class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["\\\\pi", 0], [-1, 1]])
        m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
            left_bracket="(",
            right_bracket=")")
        m2 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket=r"\\{",
            right_bracket=r"\\}")
        m3 = MobjectMatrix(
            [[Circle().scale(0.3), Square().scale(0.3)],
            [MathTex("\\\\pi").scale(2), Star().scale(0.3)]],
            left_bracket="\\\\langle",
            right_bracket="\\\\rangle")
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
        self.add(g)

</pre></div>

### Classes

| [`DecimalMatrix`](manim.mobject.matrix.DecimalMatrix.md#manim.mobject.matrix.DecimalMatrix)   | A mobject that displays a matrix with decimal entries on the screen.   |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [`IntegerMatrix`](manim.mobject.matrix.IntegerMatrix.md#manim.mobject.matrix.IntegerMatrix)   | A mobject that displays a matrix with integer entries on the screen.   |
| [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)                        | A mobject that displays a matrix on the screen.                        |
| [`MobjectMatrix`](manim.mobject.matrix.MobjectMatrix.md#manim.mobject.matrix.MobjectMatrix)   | A mobject that displays a matrix of mobject entries on the screen.     |

### Functions

### get_det_text(matrix, determinant=None, background_rect=False, initial_scale_factor=2)

Helper function to create determinant.

* **Parameters:**
  * **matrix** ([*Matrix*](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)) – The matrix whose determinant is to be created
  * **determinant** (*int* *|* *str* *|* *None*) – The value of the determinant of the matrix
  * **background_rect** (*bool*) – The background rectangle
  * **initial_scale_factor** (*float*) – The scale of the text det w.r.t the matrix
* **Returns:**
  A VGroup containing the determinant
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

<div id="determinantofamatrix" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DeterminantOfAMatrix <a class="headerlink" href="#determinantofamatrix">¶</a></p>![image](media/images/DeterminantOfAMatrix-1.png)
```python
from manim import *

class DeterminantOfAMatrix(Scene):
    def construct(self):
        matrix = Matrix([
            [2, 0],
            [-1, 1]
        ])

        # scaling down the `det` string
        det = get_det_text(matrix,
                    determinant=3,
                    initial_scale_factor=1)

        # must add the matrix
        self.add(matrix)
        self.add(det)
```

<pre data-manim-binder data-manim-classname="DeterminantOfAMatrix">
class DeterminantOfAMatrix(Scene):
    def construct(self):
        matrix = Matrix([
            [2, 0],
            [-1, 1]
        ])

        # scaling down the \`det\` string
        det = get_det_text(matrix,
                    determinant=3,
                    initial_scale_factor=1)

        # must add the matrix
        self.add(matrix)
        self.add(det)

</pre></div>

### matrix_to_mobject(matrix)

### matrix_to_tex_string(matrix)
