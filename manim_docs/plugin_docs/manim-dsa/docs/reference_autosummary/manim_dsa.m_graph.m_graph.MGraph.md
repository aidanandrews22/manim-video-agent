# MGraph

Qualified name: `manim\_dsa.m\_graph.m\_graph.MGraph`

### *class* MGraph(graph, nodes_position={}, style=<manim_dsa.constants.MGraphStyle._DefaultStyle object>)

Bases: [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict), [`Labelable`](manim_dsa.utils.utils.Labelable.md#manim_dsa.utils.utils.Labelable)

Manim Graph: a class for visualizing the graph structure using the Manim animation engine.

* **Parameters:**
  * **graph** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *]* *] or* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *,* [*list*](https://docs.python.org/3/library/stdtypes.html#list) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *]* *]* *for unweighted graph*) – list[list[tuple[str, str | int]]] or dict[str, list[tuple[str, str | int]]] for weighted graph
    The graph data, which can be weighted or unweighted.
  * **nodes_position** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict) *[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *,* *Vector3D* *]* *,* *optional*) – A dictionary mapping node labels to their positions as 3D vectors. Defaults to an empty dict.
  * **style** (`MGraphStyle`, optional) – The visual style to be applied to the graph. Defaults to MGraphStyle.DEFAULT.

### Methods

| `add_curved_edge`                                                              |                                                                                                                     |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [`add_edge`](#manim_dsa.m_graph.m_graph.MGraph.add_edge)                       | Adds a new edge between two nodes in the graph.                                                                     |
| [`add_label`](#manim_dsa.m_graph.m_graph.MGraph.add_label)                     | Adds a label to the graph with specified alignment and buffer.                                                      |
| [`add_node`](#manim_dsa.m_graph.m_graph.MGraph.add_node)                       | Adds a new node to the graph with a specified name and position.                                                    |
| [`node_layout`](#manim_dsa.m_graph.m_graph.MGraph.node_layout)                 | Applies a specified layout algorithm to arrange the nodes in the graph.                                             |
| [`set_edges_highlight`](#manim_dsa.m_graph.m_graph.MGraph.set_edges_highlight) | This method iterates through all the edges in the graph and applies the specified highlight color and stroke width. |
| [`set_nodes_highlight`](#manim_dsa.m_graph.m_graph.MGraph.set_nodes_highlight) | This method iterates through all the nodes in the graph and applies the specified highlight color and stroke width. |
| `show_backward_edge`                                                           |                                                                                                                     |

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

#### *class* CurvedEdge(line, node1_center, node2_center, node1_radius, node2_radius, arrow=True, node_angle=1.0471975511965976, arc_angle=1.0471975511965976)

Bases: [`Edge`](#manim_dsa.m_graph.m_graph.MGraph.Edge)

Represents a curved edge in the graph, connecting two nodes with an arc.

* **Parameters:**
  * **line** (*ArcBetweenPoints*) – The ArcBetweenPoints object representing the edge.
  * **node1_center** (*Point3D*) – The 3D coordinates of the center of the first node.
  * **node2_center** (*Point3D*) – The 3D coordinates of the center of the second node.
  * **node1_radius** ([*float*](https://docs.python.org/3/library/functions.html#float)) – The radius of the first node.
  * **node2_radius** ([*float*](https://docs.python.org/3/library/functions.html#float)) – The radius of the second node.
  * **arrow** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *,* *optional*) – Whether to include an arrow on the edge. Defaults to True.
  * **node_angle** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The angle between the line connecting the nodes and the direction of the arc. Defaults to PI/3.
  * **arc_angle** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The angle of the arc between the two nodes. Defaults to PI/3.

#### weighted(label, label_distance=0.3)

Assigns a label (the weight) to the edge and positions it relative to the edge.

* **Parameters:**
  * **label** (*Text*) – The label to be assigned to the edge.
  * **label_distance** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The distance from the edge to position the label. Defaults to 0.3.
* **Returns:**
  The instance of the :class:

  ```
  `
  ```

  Edge’ with the assigned label.
* **Return type:**
  self

#### *class* Edge(line, arrow=True)

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup), [`Highlightable`](manim_dsa.utils.utils.Highlightable.md#manim_dsa.utils.utils.Highlightable), [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

An abstract class that represents an edge in the graph.

* **Parameters:**
  * **line** (*Line* *or* *ArcBetweenPoints*) – The line or arc that visually represents the edge between two nodes.
  * **arrow** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *,* *optional*) – If True, an arrowhead is added to the edge. Defaults to True.

#### highlight(stroke_color=ManimColor('#FC6255'), stroke_width=8)

Highlights the edge with a specified color and stroke width.

* **Parameters:**
  * **stroke_color** (*ManimColor* *,* *optional*) – The color to be used for highlighting the edge. Defaults to RED.
  * **stroke_width** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The width of the stroke used for highlighting. Defaults to 8.
* **Returns:**
  The instance of the :class:

  ```
  `
  ```

  Edge’ with the applied highlight.
* **Return type:**
  self

#### is_weighted()

Checks if the edge is weighted by examining the presence of a label.

* **Returns:**
  True if the edge has a label (indicating it is weighted), False otherwise.
* **Return type:**
  [bool](https://docs.python.org/3/library/functions.html#bool)

#### set_highlight(stroke_color=ManimColor('#FC6255'), stroke_width=8)

Sets the highlight properties for the edge.

* **Parameters:**
  * **stroke_color** (*ManimColor* *,* *optional*) – The color to be used for highlighting the edge. Defaults to RED.
  * **stroke_width** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The width of the stroke used for highlighting. Defaults to 8.
* **Returns:**
  The instance of the `Edge` with the applied highlight.
* **Return type:**
  self

#### weighted(label)

Assigns a label to the edge, indicating that it is weighted.

* **Parameters:**
  **label** (*Text*) – The label to be assigned to the edge, representing its weight or any other relevant information.
* **Returns:**
  The instance of the :class:

  ```
  `
  ```

  Edge’ with the applied highlight.
* **Return type:**
  self

#### *class* Node(circle, label)

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup), [`Highlightable`](manim_dsa.utils.utils.Highlightable.md#manim_dsa.utils.utils.Highlightable)

A class that represents a node (or vertex) of the graph.

* **Parameters:**
  * **circle** (*Circle*) – The circular shape that visually represents the node.
  * **label** (*Text*) – The text label associated with the node.

#### get_radius()

Returns the radius of the node’s circle.

* **Returns:**
  The radius of the node’s circle.
* **Return type:**
  [float](https://docs.python.org/3/library/functions.html#float)

#### *class* StraightEdge(line, node1_center, node2_center, node1_radius, node2_radius, arrow=True)

Bases: [`Edge`](#manim_dsa.m_graph.m_graph.MGraph.Edge)

Represents a straight edge in the graph, connecting two nodes with a straight line.

* **Parameters:**
  * **line** (*Line*) – The Line object representing the edge.
  * **node1_center** (*Point3D*) – The 3D coordinates of the center of the first node.
  * **node2_center** (*Point3D*) – The 3D coordinates of the center of the second node.
  * **node1_radius** ([*float*](https://docs.python.org/3/library/functions.html#float)) – The radius of the first node.
  * **node2_radius** ([*float*](https://docs.python.org/3/library/functions.html#float)) – The radius of the second node.
  * **arrow** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *,* *optional*) – Whether to include an arrow on the edge. Defaults to True.

#### weighted(label, label_distance=0.3)

Assigns a label (the weight) to the edge and positions it relative to the edge.

* **Parameters:**
  * **label** (*Text*) – The label to be assigned to the edge.
  * **label_distance** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The distance from the edge to position the label. Defaults to 0.3.
* **Returns:**
  The instance of the :class:

  ```
  `
  ```

  Edge’ with the assigned label.
* **Return type:**
  self

#### add_edge(node1_name, node2_name, weight=None, label_distance=0.2)

Adds a new edge between two nodes in the graph.

* **Parameters:**
  * **node1_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the first node.
  * **node2_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the second node.
  * **weight** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The weight of the edge. If not provided, the edge will be unweighted.
  * **label_distance** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The distance from the edge where the label should be placed. Defaults to 0.2.
* **Returns:**
  The updated instance of the :class:’MGraph’ with the new edge added.
* **Return type:**
  self

#### add_label(text, direction=array([0., 1., 0.]), buff=0.5, \*\*kwargs)

Adds a label to the graph with specified alignment and buffer.

* **Parameters:**
  * **text** (*Text*) – The label text to be added to the graph.
  * **direction** (*Vector3D* *,* *optional*) – The direction in which the label should be positioned relative to the graph.
    Defaults to UP.
  * **buff** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The distance between the graph and the label.
    Defaults to 0.5.
  * **\*\*kwargs** – Additional keyword arguments that are passed to the function next_to() of the
    underlying add_label method.
* **Returns:**
  The updated instance of the :class:’MGraph’ with the label added.
* **Return type:**
  self

#### add_node(name, position=array([0., 0., 0.]))

Adds a new node to the graph with a specified name and position.

* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The name of the node to be added.
  * **position** (*Point3D* *,* *optional*) – The 3D position where the node will be placed. Defaults to ORIGIN.
* **Returns:**
  The updated instance of the :class:

  ```
  `
  ```

  MGraph’ with the new node added.
* **Return type:**
  self

#### node_layout(layout='kamada_kawai_layout')

Applies a specified layout algorithm to arrange the nodes in the graph.

* **Parameters:**
  **layout** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *,* *optional*) – The name of the layout algorithm to be applied to the nodes.
  Defaults to ‘kamada_kawai_layout’. Other common layout options may include ‘spring_layout’, ‘circular_layout’,
  ‘shell_layout’, and others supported by the underlying graph library.
  A full list of available layouts can be found in the NetworkX documentation:
  [https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
* **Returns:**
  The updated instance of the :class:’MGraph’ with nodes arranged according to the specified layout.
* **Return type:**
  self

#### set_edges_highlight(color=ManimColor('#FC6255'), width=8)

This method iterates through all the edges in the graph and applies the specified highlight color and stroke width.

* **Parameters:**
  * **color** (*ManimColor* *,* *optional*) – The color to be used for highlighting the edges.
    Defaults to RED.
  * **width** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The stroke width of the highlight.
    Defaults to 8.
* **Returns:**
  The updated instance of the :class:’MGraph’ with all edges highlighted.
* **Return type:**
  self

#### set_nodes_highlight(color=ManimColor('#FC6255'), width=8)

This method iterates through all the nodes in the graph and applies the specified highlight color and stroke width.

* **Parameters:**
  * **color** (*ManimColor* *,* *optional*) – The color to be used for highlighting the nodes.
    Defaults to RED.
  * **width** ([*float*](https://docs.python.org/3/library/functions.html#float) *,* *optional*) – The stroke width of the highlight.
    Defaults to 8.
* **Returns:**
  The updated instance of the MGraph with all nodes highlighted.
* **Return type:**
  self
