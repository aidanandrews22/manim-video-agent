# mobject

Base classes for objects that can be displayed.

### Type Aliases

### *class* TimeBasedUpdater

```default
Callable[['Mobject', float], object]
```

### *class* NonTimeBasedUpdater

```default
Callable[['Mobject'], object]
```

### *class* Updater

```default
`NonTimeBasedUpdater`` | `TimeBasedUpdater``
```

### Classes

| [`Group`](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group)       | Groups together multiple [`Mobjects`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).   |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) | Mathematical Object: base class for objects that can be displayed on screen.                             |

### Functions

### override_animate(method)

Decorator for overriding method animations.

This allows to specify a method (returning an [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
which is called when the decorated method is used with the `.animate` syntax
for animating the application of a method.

#### SEE ALSO
[`Mobject.animate`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.animate)

#### NOTE
Overridden methods cannot be combined with normal or other overridden
methods using method chaining with the `.animate` syntax.

### Examples

<div id="animationoverrideexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: AnimationOverrideExample <a class="headerlink" href="#animationoverrideexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./AnimationOverrideExample-1.mp4">
</video>
```python
from manim import *

class CircleWithContent(VGroup):
    def __init__(self, content):
        super().__init__()
        self.circle = Circle()
        self.content = content
        self.add(self.circle, content)
        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.content, **anim_args)
        self.clear_content()
        return anim

class AnimationOverrideExample(Scene):
    def construct(self):
        t = Text("hello!")
        my_mobject = CircleWithContent(t)
        self.play(Create(my_mobject))
        self.play(my_mobject.animate.clear_content())
        self.wait()
```

<pre data-manim-binder data-manim-classname="AnimationOverrideExample">
class CircleWithContent(VGroup):
    def \_\_init_\_(self, content):
        super()._\_init_\_()
        self.circle = Circle()
        self.content = content
        self.add(self.circle, content)
        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def \_clear_content_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.content, \*\*anim_args)
        self.clear_content()
        return anim

class AnimationOverrideExample(Scene):
    def construct(self):
        t = Text("hello!")
        my_mobject = CircleWithContent(t)
        self.play(Create(my_mobject))
        self.play(my_mobject.animate.clear_content())
        self.wait()

</pre></div>
* **Return type:**
  *LambdaType*
