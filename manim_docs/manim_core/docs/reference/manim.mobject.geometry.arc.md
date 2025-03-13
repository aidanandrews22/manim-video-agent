# arc

Mobjects that are curved.

### Examples

<div id="usefulannotations" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UsefulAnnotations <a class="headerlink" href="#usefulannotations">¶</a></p>![image](media/images/UsefulAnnotations-1.png)
```python
from manim import *

class UsefulAnnotations(Scene):
    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii")
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE))
        m4 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -5)
        m5 = CurvedArrow(2*LEFT, 2*RIGHT, radius= 8)
        m6 = CurvedDoubleArrow(ORIGIN, 2*RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i-3))
```

<pre data-manim-binder data-manim-classname="UsefulAnnotations">
class UsefulAnnotations(Scene):
    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii")
        m3 = LabeledDot(MathTex(r"\\alpha").set_color(ORANGE))
        m4 = CurvedArrow(2\*LEFT, 2\*RIGHT, radius= -5)
        m5 = CurvedArrow(2\*LEFT, 2\*RIGHT, radius= 8)
        m6 = CurvedDoubleArrow(ORIGIN, 2\*RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN \* (i-3))

</pre></div>

### Classes

| [`AnnotationDot`](manim.mobject.geometry.arc.AnnotationDot.md#manim.mobject.geometry.arc.AnnotationDot)                | A dot with bigger radius and bold stroke to annotate scenes.                                                       |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [`AnnularSector`](manim.mobject.geometry.arc.AnnularSector.md#manim.mobject.geometry.arc.AnnularSector)                | A sector of an annulus.                                                                                            |
| [`Annulus`](manim.mobject.geometry.arc.Annulus.md#manim.mobject.geometry.arc.Annulus)                                  | Region between two concentric [`Circles`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle). |
| [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)                                              | A circular arc.                                                                                                    |
| [`ArcBetweenPoints`](manim.mobject.geometry.arc.ArcBetweenPoints.md#manim.mobject.geometry.arc.ArcBetweenPoints)       | Inherits from Arc and additionally takes 2 points between which the arc is spanned.                                |
| [`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.md#manim.mobject.geometry.arc.ArcPolygon)                         | A generalized polygon allowing for points to be connected with arcs.                                               |
| [`ArcPolygonFromArcs`](manim.mobject.geometry.arc.ArcPolygonFromArcs.md#manim.mobject.geometry.arc.ArcPolygonFromArcs) | A generalized polygon allowing for points to be connected with arcs.                                               |
| [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle)                                     | A circle.                                                                                                          |
| [`CubicBezier`](manim.mobject.geometry.arc.CubicBezier.md#manim.mobject.geometry.arc.CubicBezier)                      | A cubic Bézier curve.                                                                                              |
| [`CurvedArrow`](manim.mobject.geometry.arc.CurvedArrow.md#manim.mobject.geometry.arc.CurvedArrow)                      |                                                                                                                    |
| [`CurvedDoubleArrow`](manim.mobject.geometry.arc.CurvedDoubleArrow.md#manim.mobject.geometry.arc.CurvedDoubleArrow)    |                                                                                                                    |
| [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot)                                              | A circle with a very small radius.                                                                                 |
| [`Ellipse`](manim.mobject.geometry.arc.Ellipse.md#manim.mobject.geometry.arc.Ellipse)                                  | A circular shape; oval, circle.                                                                                    |
| [`LabeledDot`](manim.mobject.geometry.arc.LabeledDot.md#manim.mobject.geometry.arc.LabeledDot)                         | A [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot) containing a label in its center.      |
| [`Sector`](manim.mobject.geometry.arc.Sector.md#manim.mobject.geometry.arc.Sector)                                     | A sector of a circle.                                                                                              |
| [`TipableVMobject`](manim.mobject.geometry.arc.TipableVMobject.md#manim.mobject.geometry.arc.TipableVMobject)          | Meant for shared functionality between Arc and Line.                                                               |
