# moving_camera_scene

A scene whose camera can be moved around.

#### SEE ALSO
[`moving_camera`](manim.camera.moving_camera.md#module-manim.camera.moving_camera)

### Examples

<div id="changingcamerawidthandrestore" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ChangingCameraWidthAndRestore <a class="headerlink" href="#changingcamerawidthandrestore">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ChangingCameraWidthAndRestore-1.mp4">
</video>
```python
from manim import *

class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))
```

<pre data-manim-binder data-manim-classname="ChangingCameraWidthAndRestore">
class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width \* 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))

</pre></div><div id="movingcameracenter" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MovingCameraCenter <a class="headerlink" href="#movingcameracenter">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./MovingCameraCenter-1.mp4">
</video>
```python
from manim import *

class MovingCameraCenter(MovingCameraScene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
        self.wait(0.3)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t))
```

<pre data-manim-binder data-manim-classname="MovingCameraCenter">
class MovingCameraCenter(MovingCameraScene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5).move_to(2 \* LEFT)
        t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 \* RIGHT)
        self.wait(0.3)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t))

</pre></div><div id="movingandzoomingcamera" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MovingAndZoomingCamera <a class="headerlink" href="#movingandzoomingcamera">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./MovingAndZoomingCamera-1.mp4">
</video>
```python
from manim import *

class MovingAndZoomingCamera(MovingCameraScene):
    def construct(self):
        s = Square(color=BLUE, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 * RIGHT)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))

        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))
```

<pre data-manim-binder data-manim-classname="MovingAndZoomingCamera">
class MovingAndZoomingCamera(MovingCameraScene):
    def construct(self):
        s = Square(color=BLUE, fill_opacity=0.5).move_to(2 \* LEFT)
        t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 \* RIGHT)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s).set(width=s.width\*2))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t).set(width=t.width\*2))

        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))

</pre></div><div id="movingcameraongraph" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MovingCameraOnGraph <a class="headerlink" href="#movingcameraongraph">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./MovingCameraOnGraph-1.mp4">
</video>
```python
from manim import *

class MovingCameraOnGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])

        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_1, dot_2)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.play(Restore(self.camera.frame))
        self.wait()
```

<pre data-manim-binder data-manim-classname="MovingCameraOnGraph">
class MovingCameraOnGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 \* PI])

        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_1, dot_2)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.play(Restore(self.camera.frame))
        self.wait()

</pre></div><div id="slidingmultiplescenes" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SlidingMultipleScenes <a class="headerlink" href="#slidingmultiplescenes">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./SlidingMultipleScenes-1.mp4">
</video>
```python
from manim import *

class SlidingMultipleScenes(MovingCameraScene):
    def construct(self):
        def create_scene(number):
            frame = Rectangle(width=16,height=9)
            circ = Circle().shift(LEFT)
            text = Tex(f"This is Scene {str(number)}").next_to(circ, RIGHT)
            frame.add(circ,text)
            return frame

        group = VGroup(*(create_scene(i) for i in range(4))).arrange_in_grid(buff=4)
        self.add(group)
        self.camera.auto_zoom(group[0], animate=False)
        for scene in group:
            self.play(self.camera.auto_zoom(scene))
            self.wait()

        self.play(self.camera.auto_zoom(group, margin=2))
```

<pre data-manim-binder data-manim-classname="SlidingMultipleScenes">
class SlidingMultipleScenes(MovingCameraScene):
    def construct(self):
        def create_scene(number):
            frame = Rectangle(width=16,height=9)
            circ = Circle().shift(LEFT)
            text = Tex(f"This is Scene {str(number)}").next_to(circ, RIGHT)
            frame.add(circ,text)
            return frame

        group = VGroup(\*(create_scene(i) for i in range(4))).arrange_in_grid(buff=4)
        self.add(group)
        self.camera.auto_zoom(group[0], animate=False)
        for scene in group:
            self.play(self.camera.auto_zoom(scene))
            self.wait()

        self.play(self.camera.auto_zoom(group, margin=2))

</pre></div>

### Classes

| [`MovingCameraScene`](manim.scene.moving_camera_scene.MovingCameraScene.md#manim.scene.moving_camera_scene.MovingCameraScene)   | This is a Scene, with special configurations and properties that make it suitable for cases where the camera must be moved around.   |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
