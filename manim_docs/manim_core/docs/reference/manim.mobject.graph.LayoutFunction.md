# LayoutFunction

Qualified name: `manim.mobject.graph.LayoutFunction`

### *class* LayoutFunction(\*args, \*\*kwargs)

Bases: `Protocol`

A protocol for automatic layout functions that compute a layout for a graph to be used in `change_layout()`.

#### NOTE
The layout function must be a pure function, i.e., it must not modify the graph passed to it.

### Examples

Here is an example that arranges nodes in an n x m grid in sorted order.

<div id="customlayoutexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CustomLayoutExample <a class="headerlink" href="#customlayoutexample">¶</a></p>![image](media/images/CustomLayoutExample-1.png)
```python
from manim import *

class CustomLayoutExample(Scene):
    def construct(self):
        import numpy as np
        import networkx as nx

        # create custom layout
        def custom_layout(
            graph: nx.Graph,
            scale: float | tuple[float, float, float] = 2,
            n: int | None = None,
            *args: Any,
            **kwargs: Any,
        ):
            nodes = sorted(list(graph))
            height = len(nodes) // n
            return {
                node: (scale * np.array([
                    (i % n) - (n-1)/2,
                    -(i // n) + height/2,
                    0
                ])) for i, node in enumerate(graph)
            }

        # draw graph
        n = 4
        graph = Graph(
            [i for i in range(4 * 2 - 1)],
            [(0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (4, 5), (5, 6)],
            labels=True,
            layout=custom_layout,
            layout_config={'n': n}
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="CustomLayoutExample">
class CustomLayoutExample(Scene):
    def construct(self):
        import numpy as np
        import networkx as nx

        # create custom layout
        def custom_layout(
            graph: nx.Graph,
            scale: float | tuple[float, float, float] = 2,
            n: int | None = None,
            \*args: Any,
            \*\*kwargs: Any,
        ):
            nodes = sorted(list(graph))
            height = len(nodes) // n
            return {
                node: (scale \* np.array([
                    (i % n) - (n-1)/2,
                    -(i // n) + height/2,
                    0
                ])) for i, node in enumerate(graph)
            }

        # draw graph
        n = 4
        graph = Graph(
            [i for i in range(4 \* 2 - 1)],
            [(0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (4, 5), (5, 6)],
            labels=True,
            layout=custom_layout,
            layout_config={'n': n}
        )
        self.add(graph)

</pre></div>

Several automatic layouts are provided by manim, and can be used by passing their name as the `layout` parameter to `change_layout()`.
Alternatively, a custom layout function can be passed to `change_layout()` as the `layout` parameter. Such a function must adhere to the [`LayoutFunction`](#manim.mobject.graph.LayoutFunction) protocol.

The [`LayoutFunction`](#manim.mobject.graph.LayoutFunction) s provided by manim are illustrated below:

- Circular Layout: places the vertices on a circle

<div id="circularlayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CircularLayout <a class="headerlink" href="#circularlayout">¶</a></p>![image](media/images/CircularLayout-1.png)
```python
from manim import *

class CircularLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="circular",
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="CircularLayout">
class CircularLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="circular",
            labels=True
        )
        self.add(graph)

</pre></div>
- Kamada Kawai Layout: tries to place the vertices such that the given distances between them are respected

<div id="kamadakawailayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: KamadaKawaiLayout <a class="headerlink" href="#kamadakawailayout">¶</a></p>![image](media/images/KamadaKawaiLayout-1.png)
```python
from manim import *

class KamadaKawaiLayout(Scene):
    def construct(self):
        from collections import defaultdict
        distances: dict[int, dict[int, float]] = defaultdict(dict)

        # set desired distances
        distances[1][2] = 1  # distance between vertices 1 and 2 is 1
        distances[2][3] = 1  # distance between vertices 2 and 3 is 1
        distances[3][4] = 2  # etc
        distances[4][5] = 3
        distances[5][6] = 5
        distances[6][1] = 8

        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)],
            layout="kamada_kawai",
            layout_config={"dist": distances},
            layout_scale=4,
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="KamadaKawaiLayout">
class KamadaKawaiLayout(Scene):
    def construct(self):
        from collections import defaultdict
        distances: dict[int, dict[int, float]] = defaultdict(dict)

        # set desired distances
        distances[1][2] = 1  # distance between vertices 1 and 2 is 1
        distances[2][3] = 1  # distance between vertices 2 and 3 is 1
        distances[3][4] = 2  # etc
        distances[4][5] = 3
        distances[5][6] = 5
        distances[6][1] = 8

        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)],
            layout="kamada_kawai",
            layout_config={"dist": distances},
            layout_scale=4,
            labels=True
        )
        self.add(graph)

</pre></div>
- Partite Layout: places vertices into distinct partitions

<div id="partitelayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PartiteLayout <a class="headerlink" href="#partitelayout">¶</a></p>![image](media/images/PartiteLayout-1.png)
```python
from manim import *

class PartiteLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="partite",
            layout_config={"partitions": [[1,2],[3,4],[5,6]]},
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="PartiteLayout">
class PartiteLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="partite",
            layout_config={"partitions": [[1,2],[3,4],[5,6]]},
            labels=True
        )
        self.add(graph)

</pre></div>
- Planar Layout: places vertices such that edges do not cross

<div id="planarlayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PlanarLayout <a class="headerlink" href="#planarlayout">¶</a></p>![image](media/images/PlanarLayout-1.png)
```python
from manim import *

class PlanarLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="planar",
            layout_scale=4,
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="PlanarLayout">
class PlanarLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="planar",
            layout_scale=4,
            labels=True
        )
        self.add(graph)

</pre></div>
- Random Layout: randomly places vertices

<div id="randomlayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: RandomLayout <a class="headerlink" href="#randomlayout">¶</a></p>![image](media/images/RandomLayout-1.png)
```python
from manim import *

class RandomLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="random",
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="RandomLayout">
class RandomLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="random",
            labels=True
        )
        self.add(graph)

</pre></div>
- Shell Layout: places vertices in concentric circles

<div id="shelllayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShellLayout <a class="headerlink" href="#shelllayout">¶</a></p>![image](media/images/ShellLayout-1.png)
```python
from manim import *

class ShellLayout(Scene):
    def construct(self):
        nlist = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [(1, 2), (2, 3), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (7, 3), (8, 3), (8, 1), (9, 1)],
            layout="shell",
            layout_config={"nlist": nlist},
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="ShellLayout">
class ShellLayout(Scene):
    def construct(self):
        nlist = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [(1, 2), (2, 3), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 3), (7, 3), (8, 3), (8, 1), (9, 1)],
            layout="shell",
            layout_config={"nlist": nlist},
            labels=True
        )
        self.add(graph)

</pre></div>
- Spectral Layout: places vertices using the eigenvectors of the graph Laplacian (clusters nodes which are an approximation of the ratio cut)

<div id="spectrallayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SpectralLayout <a class="headerlink" href="#spectrallayout">¶</a></p>![image](media/images/SpectralLayout-1.png)
```python
from manim import *

class SpectralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spectral",
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="SpectralLayout">
class SpectralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spectral",
            labels=True
        )
        self.add(graph)

</pre></div>
- Sprial Layout: places vertices in a spiraling pattern

<div id="spirallayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SpiralLayout <a class="headerlink" href="#spirallayout">¶</a></p>![image](media/images/SpiralLayout-1.png)
```python
from manim import *

class SpiralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spiral",
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="SpiralLayout">
class SpiralLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spiral",
            labels=True
        )
        self.add(graph)

</pre></div>
- Spring Layout: places nodes according to the Fruchterman-Reingold force-directed algorithm (attempts to minimize edge length while maximizing node separation)

<div id="springlayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SpringLayout <a class="headerlink" href="#springlayout">¶</a></p>![image](media/images/SpringLayout-1.png)
```python
from manim import *

class SpringLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spring",
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="SpringLayout">
class SpringLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6],
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (5, 1), (1, 3), (3, 5)],
            layout="spring",
            labels=True
        )
        self.add(graph)

</pre></div>
- Tree Layout: places vertices into a tree with a root node and branches (can only be used with legal trees)

<div id="treelayout" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TreeLayout <a class="headerlink" href="#treelayout">¶</a></p>![image](media/images/TreeLayout-1.png)
```python
from manim import *

class TreeLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7],
            [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)],
            layout="tree",
            layout_config={"root_vertex": 1},
            labels=True
        )
        self.add(graph)
```

<pre data-manim-binder data-manim-classname="TreeLayout">
class TreeLayout(Scene):
    def construct(self):
        graph = Graph(
            [1, 2, 3, 4, 5, 6, 7],
            [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)],
            layout="tree",
            layout_config={"root_vertex": 1},
            labels=True
        )
        self.add(graph)

</pre></div>

### Methods
