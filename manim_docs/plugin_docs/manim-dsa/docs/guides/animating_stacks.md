# Animating Stacks

## Manim Stack - MStack

In this section, you’ll find all the methods available to manipulate a `MStack` (short for Manim Stack 😄). Like all `MObject` structures, you can animate these methods using the `.animate` method, allowing you to animate each operation provided by Manim DSA.
Otherwise, methods will run without any animations.

You can also access each element in a `MStack` using the `[]` operator and specifying the element’s index.

## Creating a MStack

To represent a stack, initialize an object of type `MStack`. As the first parameter, provide a list of values to insert into the `MStack`. Optionally, you can specify the distance between each element and customize the theme of the `MStack` (see customizing_a_mstack).

Here’s an example that creates a `MStack` with a list of five numbers.

<div id="creation" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Creation <a class="headerlink" href="#creation">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./Creation-2.mp4">
</video>
```python
from manim import *

from manim_dsa import *

class Creation(Scene):
    def construct(self):
        mStack = MStack([1, 2, 3, 4, 5]).scale(0.7)
        self.play(Create(mStack))
        self.wait()
```

<pre data-manim-binder data-manim-classname="Creation">
from manim_dsa import \*

class Creation(Scene):
    def construct(self):
        mStack = MStack([1, 2, 3, 4, 5]).scale(0.7)
        self.play(Create(mStack))
        self.wait()

</pre></div>

<a id="customizing-a-stack"></a>

## Customizing a MStack

ManimDSA provides various options for customizing the colors and styles of a MStack. You can use these options by passing a predefined style configuration from the `MStackStyle` class using the `style` parameter. Refer to `MStackStyle` for more details. Alternatively, you can define a custom style to suit your needs.

In the following example, we use the `GREEN` style for the `MStack`.

<div id="customcreation" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CustomCreation <a class="headerlink" href="#customcreation">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./CustomCreation-2.mp4">
</video>
```python
from manim import *

from manim_dsa import *

class CustomCreation(Scene):
    def construct(self):
        mStack = MStack(
            [1, 2, 3, 4, 5],
            style=MStackStyle.GREEN
        ).scale(0.7)
        self.play(Create(mStack))
        self.wait()
```

<pre data-manim-binder data-manim-classname="CustomCreation">
from manim_dsa import \*

class CustomCreation(Scene):
    def construct(self):
        mStack = MStack(
            [1, 2, 3, 4, 5],
            style=MStackStyle.GREEN
        ).scale(0.7)
        self.play(Create(mStack))
        self.wait()

</pre></div>

## Inserting an element to a MStack

The `append()` method allows you to insert an element in a `MStack`. The new element automatically inherits the properties specified in the configuration dictionaries.

In the example below, we create a `MStack` and then use the `append()` method to insert a new element.

<div id="append" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Append <a class="headerlink" href="#append">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./Append-2.mp4">
</video>
```python
from manim import *

from manim_dsa import *

class Append(Scene):
    def construct(self):
        mStack = (
            MStack(
                [1, 2, 3, 4, 5],
                style=MStackStyle.BLUE,
            ).scale(0.7)
        )
        self.play(Create(mStack))
        self.play(mStack.animate.append(6))
        self.wait()
```

<pre data-manim-binder data-manim-classname="Append">
from manim_dsa import \*

class Append(Scene):
    def construct(self):
        mStack = (
            MStack(
                [1, 2, 3, 4, 5],
                style=MStackStyle.BLUE,
            ).scale(0.7)
        )
        self.play(Create(mStack))
        self.play(mStack.animate.append(6))
        self.wait()

</pre></div>

## Removing an element from a MStack

The `pop()` method allows you to remove the last element inserted in a `MStack`, as you can see in the example below.

<div id="pop" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Pop <a class="headerlink" href="#pop">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./Pop-2.mp4">
</video>
```python
from manim import *

from manim import *
from manim_dsa import *

class Pop(Scene):
    def construct(self):
        mStack = (
            MStack(
                [1, 2, 3, 4, 5],
                style=MStackStyle.BLUE
            )#.scale(0.7) for some strange reason it's not needed T_T
        )
        self.play(Create(mStack))
        self.play(mStack.animate.pop())
        self.wait()
```

<pre data-manim-binder data-manim-classname="Pop">
from manim import \*
from manim_dsa import \*

class Pop(Scene):
    def construct(self):
        mStack = (
            MStack(
                [1, 2, 3, 4, 5],
                style=MStackStyle.BLUE
            )#.scale(0.7) for some strange reason it's not needed T_T
        )
        self.play(Create(mStack))
        self.play(mStack.animate.pop())
        self.wait()

</pre></div>
