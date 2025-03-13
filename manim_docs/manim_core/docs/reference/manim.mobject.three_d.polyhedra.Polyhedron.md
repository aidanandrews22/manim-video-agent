# Polyhedron

Qualified name: `manim.mobject.three\_d.polyhedra.Polyhedron`

### *class* Polyhedron(vertex_coords, faces_list, faces_config={}, graph_config={})

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

An abstract polyhedra class.

In this implementation, polyhedra are defined with a list of vertex coordinates in space, and a list
of faces. This implementation mirrors that of a standard polyhedral data format (OFF, object file format).

* **Parameters:**
  * **vertex_coords** (*list* *[**list* *[**float* *]*  *|* *np.ndarray* *]*) – A list of coordinates of the corresponding vertices in the polyhedron. Each coordinate will correspond to
    a vertex. The vertices are indexed with the usual indexing of Python.
  * **faces_list** (*list* *[**list* *[**int* *]* *]*) – A list of faces. Each face is a sublist containing the indices of the vertices that form the corners of that face.
  * **faces_config** (*dict* *[**str* *,* *str* *|* *int* *|* *float* *|* *bool* *]*) – Configuration for the polygons representing the faces of the polyhedron.
  * **graph_config** (*dict* *[**str* *,* *str* *|* *int* *|* *float* *|* *bool* *]*) – Configuration for the graph containing the vertices and edges of the polyhedron.

### Examples

To understand how to create a custom polyhedra, let’s use the example of a rather simple one - a square pyramid.

<div id="squarepyramidscene" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SquarePyramidScene <a class="headerlink" href="#squarepyramidscene">¶</a></p>![image](media/images/SquarePyramidScene-1.png)
```python
from manim import *

class SquarePyramidScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        self.add(pyramid)
```

<pre data-manim-binder data-manim-classname="SquarePyramidScene">
class SquarePyramidScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 \* DEGREES, theta=30 \* DEGREES)
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        self.add(pyramid)

</pre></div>

In defining the polyhedron above, we first defined the coordinates of the vertices.
These are the corners of the square base, given as the first four coordinates in the vertex list,
and the apex, the last coordinate in the list.

Next, we define the faces of the polyhedron. The triangular surfaces of the pyramid are polygons
with two adjacent vertices in the base and the vertex at the apex as corners. We thus define these
surfaces in the first four elements of our face list. The last element defines the base of the pyramid.

The graph and faces of polyhedra can also be accessed and modified directly, after instantiation.
They are stored in the graph and faces attributes respectively.

<div id="polyhedronsubmobjects" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PolyhedronSubMobjects <a class="headerlink" href="#polyhedronsubmobjects">¶</a></p>![image](media/images/PolyhedronSubMobjects-1.png)
```python
from manim import *

class PolyhedronSubMobjects(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        octahedron = Octahedron(edge_length = 3)
        octahedron.graph[0].set_color(RED)
        octahedron.faces[2].set_color(YELLOW)
        self.add(octahedron)
```

<pre data-manim-binder data-manim-classname="PolyhedronSubMobjects">
class PolyhedronSubMobjects(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 \* DEGREES, theta=30 \* DEGREES)
        octahedron = Octahedron(edge_length = 3)
        octahedron.graph[0].set_color(RED)
        octahedron.faces[2].set_color(YELLOW)
        self.add(octahedron)

</pre></div>

### Methods

| [`create_faces`](#manim.mobject.three_d.polyhedra.Polyhedron.create_faces)               | Creates VGroup of faces from a list of face coordinates.   |
|------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [`extract_face_coords`](#manim.mobject.three_d.polyhedra.Polyhedron.extract_face_coords) | Extracts the coordinates of the vertices in the graph.     |
| [`get_edges`](#manim.mobject.three_d.polyhedra.Polyhedron.get_edges)                     | Creates list of cyclic pairwise tuples.                    |
| `update_faces`                                                                           |                                                            |

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

#### \_original_\_init_\_(vertex_coords, faces_list, faces_config={}, graph_config={})

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vertex_coords** (*list* *[**list* *[**float* *]*  *|* *ndarray* *]*)
  * **faces_list** (*list* *[**list* *[**int* *]* *]*)
  * **faces_config** (*dict* *[**str* *,* *str* *|* *int* *|* *float* *|* *bool* *]*)
  * **graph_config** (*dict* *[**str* *,* *str* *|* *int* *|* *float* *|* *bool* *]*)

#### create_faces(face_coords)

Creates VGroup of faces from a list of face coordinates.

* **Parameters:**
  **face_coords** (*list* *[**list* *[**list* *|* *ndarray* *]* *]*)
* **Return type:**
  [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### extract_face_coords()

Extracts the coordinates of the vertices in the graph.
Used for updating faces.

* **Return type:**
  list[list[*ndarray*]]

#### get_edges(faces_list)

Creates list of cyclic pairwise tuples.

* **Parameters:**
  **faces_list** (*list* *[**list* *[**int* *]* *]*)
* **Return type:**
  list[tuple[int, int]]
