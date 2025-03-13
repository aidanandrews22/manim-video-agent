# CyclicReplace

Qualified name: `manim.animation.transform.CyclicReplace`

### *class* CyclicReplace(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

An animation moving mobjects cyclically.

In particular, this means: the first mobject takes the place
of the second mobject, the second one takes the place of
the third mobject, and so on. The last mobject takes the
place of the first one.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – List of mobjects to be transformed.
  * **path_arc** (*float*) – The angle of the arc (in radians) that the mobjects will follow to reach
    their target.
  * **kwargs** – Further keyword arguments that are passed to [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform).

### Examples

<div id="cyclicreplaceexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CyclicReplaceExample <a class="headerlink" href="#cyclicreplaceexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./CyclicReplaceExample-1.mp4">
</video>
```python
from manim import *

class CyclicReplaceExample(Scene):
    def construct(self):
        group = VGroup(Square(), Circle(), Triangle(), Star())
        group.arrange(RIGHT)
        self.add(group)

        for _ in range(4):
            self.play(CyclicReplace(*group))
```

<pre data-manim-binder data-manim-classname="CyclicReplaceExample">
class CyclicReplaceExample(Scene):
    def construct(self):
        group = VGroup(Square(), Circle(), Triangle(), Star())
        group.arrange(RIGHT)
        self.add(group)

        for \_ in range(4):
            self.play(CyclicReplace(\*group))

</pre></div>

### Methods

| `create_target`   |    |
|-------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(\*mobjects, path_arc=1.5707963267948966, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **path_arc** (*float*)
* **Return type:**
  None
