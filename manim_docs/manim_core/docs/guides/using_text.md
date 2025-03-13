# Rendering Text and Formulas

There are two different ways by which you can render **Text** in videos:

1. Using Pango ([`text_mobject`](../reference/manim.mobject.text.text_mobject.md#module-manim.mobject.text.text_mobject))
2. Using LaTeX ([`tex_mobject`](../reference/manim.mobject.text.tex_mobject.md#module-manim.mobject.text.tex_mobject))

If you want to render simple text, you should use either [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or
[`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText), or one of its derivatives like [`Paragraph`](../reference/manim.mobject.text.text_mobject.Paragraph.md#manim.mobject.text.text_mobject.Paragraph).
See [Text Without LaTeX](#using-text-objects) for more information.

LaTeX should be used when you need mathematical typesetting. See
[Text With LaTeX](#rendering-with-latex) for more information.

<a id="using-text-objects"></a>

## Text Without LaTeX

The simplest way to add text to your animations is to use the [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)
class. It uses the [Pango library](https://pango.gnome.org) to render text. With Pango, you can also
render non-English alphabets like 你好 or  こんにちは or 안녕하세요 or
مرحبا بالعالم.

Here is a simple *Hello World* animation.

<div id="helloworld" class="admonition admonition-manim-example">
<p class="admonition-title">Example: HelloWorld <a class="headerlink" href="#helloworld">¶</a></p>![image](media/images/HelloWorld-1.png)
```python
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)
```

<pre data-manim-binder data-manim-classname="HelloWorld">
class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)

</pre>

References: [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)

</div>

You can also use [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText) which allows the use of PangoMarkup
(see the documentation of [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText) for details) to render text.
For example:

<div id="singlelinecolor" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SingleLineColor <a class="headerlink" href="#singlelinecolor">¶</a></p>![image](media/images/SingleLineColor-1.png)
```python
from manim import *

class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        self.add(text)
```

<pre data-manim-binder data-manim-classname="SingleLineColor">
class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        self.add(text)

</pre>

References: [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText)

</div>

### Working with [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)

This section explains the properties of [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) and how can it be used
in your animations.

#### Using Fonts

You can set a different font using `font`.

#### NOTE
The font used must be installed in your system, and Pango should know
about it. You can get a list of fonts using `manimpango.list_fonts()`.

```pycon
>>> import manimpango
>>> manimpango.list_fonts()
[...]
```

<div id="fontsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: FontsExample <a class="headerlink" href="#fontsexample">¶</a></p>![image](media/images/FontsExample-1.png)
```python
from manim import *

class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.add(ft)
```

<pre data-manim-binder data-manim-classname="FontsExample">
class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.add(ft)

</pre></div>

#### Setting Slant and Weight

Slant is the style of the Text, and it can be `NORMAL` (the default),
`ITALIC` or `OBLIQUE`. Usually, for many fonts both `ITALIC` and
`OBLIQUE` look similar, but `ITALIC` uses **Roman Style**, whereas
`OBLIQUE` uses **Italic Style**.

Weight specifies the boldness of a font. You can see a list of weights in
`manimpango.Weight`.

<div id="slantsexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SlantsExample <a class="headerlink" href="#slantsexample">¶</a></p>![image](media/images/SlantsExample-1.png)
```python
from manim import *

class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)
```

<pre data-manim-binder data-manim-classname="SlantsExample">
class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)

</pre></div><div id="differentweight" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DifferentWeight <a class="headerlink" href="#differentweight">¶</a></p>![image](media/images/DifferentWeight-1.png)
```python
from manim import *

class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(
            sorted(
                {
                    weight: manimpango.Weight(weight).value
                    for weight in manimpango.Weight
                }.items(),
                key=lambda x: x[1],
            )
        )
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))
```

<pre data-manim-binder data-manim-classname="DifferentWeight">
class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(
            sorted(
                {
                    weight: manimpango.Weight(weight).value
                    for weight in manimpango.Weight
                }.items(),
                key=lambda x: x[1],
            )
        )
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))

</pre></div>

<a id="using-colors"></a>

#### Using Colors

You can set the color of the text using `color`:

<div id="simplecolor" class="admonition admonition-manim-example">
<p class="admonition-title">Example: SimpleColor <a class="headerlink" href="#simplecolor">¶</a></p>![image](media/images/SimpleColor-1.png)
```python
from manim import *

class SimpleColor(Scene):
    def construct(self):
        col = Text("RED COLOR", color=RED)
        self.add(col)
```

<pre data-manim-binder data-manim-classname="SimpleColor">
class SimpleColor(Scene):
    def construct(self):
        col = Text("RED COLOR", color=RED)
        self.add(col)

</pre></div>

You can use utilities like `t2c` for coloring specific characters.
This may be problematic if your text contains ligatures
as explained in [Iterating Text](#iterating-text).

`t2c` accepts two types of dictionaries,

* The keys can contain indices like `[2:-1]` or `[4:8]`,
  this works similar to how [slicing](https://realpython.com/python-strings/#string-slicing)
  works in Python. The values should be the color of the Text from `Color`.
* The keys contain words or characters which should be colored separately
  and the values should be the color from `Color`:

<div id="textt2cexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Textt2cExample <a class="headerlink" href="#textt2cexample">¶</a></p>![image](media/images/Textt2cExample-1.png)
```python
from manim import *

class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)
```

<pre data-manim-binder data-manim-classname="Textt2cExample">
class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)

</pre></div>

If you want to avoid problems when using colors (due to ligatures), consider using
`MarkupText`.

#### Using Gradients

You can add a gradient using `gradient`. The value must
be an iterable of any length:

<div id="gradientexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: GradientExample <a class="headerlink" href="#gradientexample">¶</a></p>![image](media/images/GradientExample-1.png)
```python
from manim import *

class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)
```

<pre data-manim-binder data-manim-classname="GradientExample">
class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)

</pre></div>

You can also use `t2g` for gradients with specific
characters of the text. It shares a similar syntax to [the
interface for colors](#using-colors):

<div id="t2gexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: t2gExample <a class="headerlink" href="#t2gexample">¶</a></p>![image](media/images/t2gExample-1.png)
```python
from manim import *

class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)
```

<pre data-manim-binder data-manim-classname="t2gExample">
class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)

</pre></div>

#### Setting Line Spacing

You can set the line spacing using `line_spacing`:

<div id="linespacing" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LineSpacing <a class="headerlink" href="#linespacing">¶</a></p>![image](media/images/LineSpacing-1.png)
```python
from manim import *

class LineSpacing(Scene):
    def construct(self):
        a = Text("Hello\nWorld", line_spacing=1)
        b = Text("Hello\nWorld", line_spacing=4)
        self.add(Group(a,b).arrange(LEFT, buff=5))
```

<pre data-manim-binder data-manim-classname="LineSpacing">
class LineSpacing(Scene):
    def construct(self):
        a = Text("Hello\\nWorld", line_spacing=1)
        b = Text("Hello\\nWorld", line_spacing=4)
        self.add(Group(a,b).arrange(LEFT, buff=5))

</pre></div>

<a id="disable-ligatures"></a>

#### Disabling Ligatures

By disabling ligatures you would get a one-to-one mapping between characters and
submobjects. This fixes the issues with coloring text.

#### WARNING
Be aware that using this method with text that heavily depends on
ligatures (Arabic text) may yield unexpected results.

You can disable ligatures by passing `disable_ligatures` to
`Text`. For example:

<div id="disableligature" class="admonition admonition-manim-example">
<p class="admonition-title">Example: DisableLigature <a class="headerlink" href="#disableligature">¶</a></p>![image](media/images/DisableLigature-1.png)
```python
from manim import *

class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature",font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli).arrange(DOWN, buff=.8))
```

<pre data-manim-binder data-manim-classname="DisableLigature">
class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature",font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli).arrange(DOWN, buff=.8))

</pre></div>

<a id="iterating-text"></a>

#### Iterating [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)

Text objects behave like [`VGroups`](../reference/manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup). Therefore, you can slice and index
the text.

For example, you can set each letter to different color by iterating it.

<div id="iteratecolor" class="admonition admonition-manim-example">
<p class="admonition-title">Example: IterateColor <a class="headerlink" href="#iteratecolor">¶</a></p>![image](media/images/IterateColor-1.png)
```python
from manim import *

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)
```

<pre data-manim-binder data-manim-classname="IterateColor">
class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)

</pre></div>

#### WARNING
Please note that [Ligature](https://en.wikipedia.org/wiki/Ligature_(writing)) can cause problems here. If you need a
one-to-one mapping of characters to submobjects you should pass
the `disable_ligatures` parameter to [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text).
See [Disabling Ligatures](#disable-ligatures).

### Working with [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText)

MarkupText is similar to [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text), the only difference between them is
that this accepts and processes PangoMarkup (which is similar to
html), instead of just rendering plain text.

Consult the documentation of [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText) for more details
and further references about PangoMarkup.

<div id="markuptest" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MarkupTest <a class="headerlink" href="#markuptest">¶</a></p>![image](media/images/MarkupTest-1.png)
```python
from manim import *

class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)
```

<pre data-manim-binder data-manim-classname="MarkupTest">
class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)

</pre></div>

<a id="rendering-with-latex"></a>

## Text With LaTeX

Just as you can use [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) to add text to your videos, you can
use [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) to insert LaTeX.

For example,

<div id="hellolatex" class="admonition admonition-manim-example">
<p class="admonition-title">Example: HelloLaTeX <a class="headerlink" href="#hellolatex">¶</a></p>![image](media/images/HelloLaTeX-1.png)
```python
from manim import *

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="HelloLaTeX">
class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\\LaTeX", font_size=144)
        self.add(tex)

</pre></div>

#### NOTE
Note that we are using a raw string (`r'...'`) instead of a regular string (`'...'`).
This is because TeX code uses a lot of special characters - like `\` for example - that
have special meaning within a regular python string. An alternative would have been to
write `\\` to escape the backslash: `Tex('\\LaTeX')`.

### Working with [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

Everything passed to [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) is in math mode by default. To be more precise,
[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) is processed within an `align*` environment. You can achieve a
similar effect with [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) by enclosing your formula with `$` symbols:
`$\xrightarrow{x^6y^8}$`:

<div id="mathtexdemo" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MathTeXDemo <a class="headerlink" href="#mathtexdemo">¶</a></p>![image](media/images/MathTeXDemo-1.png)
```python
from manim import *

class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))
```

<pre data-manim-binder data-manim-classname="MathTeXDemo">
class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))

</pre></div>

### LaTeX commands and keyword arguments

We can use any standard LaTeX commands in the AMS maths packages. Such
as the `mathtt` math-text type or the `looparrowright` arrow.

<div id="amslatex" class="admonition admonition-manim-example">
<p class="admonition-title">Example: AMSLaTeX <a class="headerlink" href="#amslatex">¶</a></p>![image](media/images/AMSLaTeX-1.png)
```python
from manim import *

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="AMSLaTeX">
class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\\mathtt{H} \\looparrowright$ \\LaTeX', font_size=144)
        self.add(tex)

</pre></div>

On the Manim side, the [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) class also accepts attributes to
change the appearance of the output. This is very similar to the
[`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) class. For example, the `color` keyword changes the
color of the TeX mobject.

<div id="latexattributes" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LaTeXAttributes <a class="headerlink" href="#latexattributes">¶</a></p>![image](media/images/LaTeXAttributes-1.png)
```python
from manim import *

class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="LaTeXAttributes">
class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \\LaTeX', color=BLUE, font_size=144)
        self.add(tex)

</pre></div>

### Extra LaTeX Packages

Some commands require special packages to be loaded into the TeX template.
For example, to use the `mathscr` script, we need to add the `mathrsfs`
package. Since this package isn’t loaded into Manim’s tex template by default,
we have to add it manually.

<div id="addpackagelatex" class="admonition admonition-manim-example">
<p class="admonition-title">Example: AddPackageLatex <a class="headerlink" href="#addpackagelatex">¶</a></p>![image](media/images/AddPackageLatex-1.png)
```python
from manim import *

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="AddPackageLatex">
class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\\usepackage{mathrsfs}")
        tex = Tex(
            r"$\\mathscr{H} \\rightarrow \\mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)

</pre></div>

### Substrings and parts

The TeX mobject can accept multiple strings as arguments. Afterwards you can
refer to the individual parts either by their index (like `tex[1]`), or by
selecting parts of the tex code. In this example, we set the color
of the `\bigstar` using `set_color_by_tex()`:

<div id="latexsubstrings" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LaTeXSubstrings <a class="headerlink" href="#latexsubstrings">¶</a></p>![image](media/images/LaTeXSubstrings-1.png)
```python
from manim import *

class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="LaTeXSubstrings">
class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\\bigstar$', r'\\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)

</pre></div>

Note that `set_color_by_tex()` colors the entire substring containing
the Tex, not just the specific symbol or Tex expression. Consider the following example:

<div id="incorrectlatexsubstringcoloring" class="admonition admonition-manim-example">
<p class="admonition-title">Example: IncorrectLaTeXSubstringColoring <a class="headerlink" href="#incorrectlatexsubstringcoloring">¶</a></p>![image](media/images/IncorrectLaTeXSubstringColoring-1.png)
```python
from manim import *

class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)
```

<pre data-manim-binder data-manim-classname="IncorrectLaTeXSubstringColoring">
class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \\frac{1}{2} x^2 + \\frac{1}{6} x^3 + \\cdots + \\frac{1}{n!} x^n + \\cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

</pre></div>

As you can see, this colors the entire equation yellow, contrary to what
may be expected. To color only `x` yellow, we have to do the following:

<div id="correctlatexsubstringcoloring" class="admonition admonition-manim-example">
<p class="admonition-title">Example: CorrectLaTeXSubstringColoring <a class="headerlink" href="#correctlatexsubstringcoloring">¶</a></p>![image](media/images/CorrectLaTeXSubstringColoring-1.png)
```python
from manim import *

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)
```

<pre data-manim-binder data-manim-classname="CorrectLaTeXSubstringColoring">
class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \\frac{1}{2} x^2 + \\frac{1}{6} x^3 + \\cdots + \\frac{1}{n!} x^n + \\cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

</pre></div>

By setting `substrings_to_isolate` to `x`, we split up the
[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) into substrings automatically and isolate the `x` components
into individual substrings. Only then can `set_color_by_tex()` be used
to achieve the desired result.

Note that Manim also supports a custom syntax that allows splitting
a TeX string into substrings easily: simply enclose parts of your formula
that you want to isolate with double braces. In the string
`MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")`, the rendered mobject
will consist of the substrings `a^2`, `+`, `b^2`, `=`, and `c^2`.
This makes transformations between similar text fragments easy
to write using [`TransformMatchingTex`](../reference/manim.animation.transform_matching_parts.TransformMatchingTex.md#manim.animation.transform_matching_parts.TransformMatchingTex).

### Using `index_labels` to work with complicated strings

You might sometimes be working with a very complicated [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) mobject
that makes it difficult to work with its individual components. This is
where the debugging function [`index_labels()`](../reference/manim.utils.debug.md#manim.utils.debug.index_labels) is very useful.

The method shows the index of a mobject’s submobjects, allowing you
to easily find the components of the mobject you would like to change.

<div id="indexlabelsmathtex" class="admonition admonition-manim-example">
<p class="admonition-title">Example: IndexLabelsMathTex <a class="headerlink" href="#indexlabelsmathtex">¶</a></p>![image](media/images/IndexLabelsMathTex-1.png)
```python
from manim import *

class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        self.add(text)
```

<pre data-manim-binder data-manim-classname="IndexLabelsMathTex">
class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        self.add(text)

</pre></div>

### LaTeX Maths Fonts - The Template Library

Changing fonts in LaTeX when typesetting mathematical formulae is
trickier than regular text. It requires changing the template that is used
to compile the TeX. Manim comes with a collection of [`TexFontTemplates`](../reference/manim.utils.tex_templates.TexFontTemplates.md#manim.utils.tex_templates.TexFontTemplates)
ready for you to use. These templates will all work in math mode:

<div id="latexmathfonts" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LaTeXMathFonts <a class="headerlink" href="#latexmathfonts">¶</a></p>![image](media/images/LaTeXMathFonts-1.png)
```python
from manim import *

class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="LaTeXMathFonts">
class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        self.add(tex)

</pre></div>

Manim also has a [`TexTemplateLibrary`](../reference/manim.utils.tex_templates.TexTemplateLibrary.md#manim.utils.tex_templates.TexTemplateLibrary) containing the TeX
templates used by 3Blue1Brown. One example is the ctex template,
used for typesetting Chinese script. For this to work, the ctex LaTeX package
must be installed on your system. Furthermore, if you are only
typesetting Text, you probably do not need [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) at all, and
should use [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) instead.

<div id="latextemplatelibrary" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LaTeXTemplateLibrary <a class="headerlink" href="#latextemplatelibrary">¶</a></p>![image](media/images/LaTeXTemplateLibrary-1.png)
```python
from manim import *

class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="LaTeXTemplateLibrary">
class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\\\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)

</pre></div>

### Aligning formulae

[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) mobject is typeset in the LaTeX  `align*`
environment. This means you can use the `&` alignment character
when typesetting multiline formulae:

<div id="latexalignenvironment" class="admonition admonition-manim-example">
<p class="admonition-title">Example: LaTeXAlignEnvironment <a class="headerlink" href="#latexalignenvironment">¶</a></p>![image](media/images/LaTeXAlignEnvironment-1.png)
```python
from manim import *

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)
```

<pre data-manim-binder data-manim-classname="LaTeXAlignEnvironment">
class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\\\ &= 5 + 1 \\\\ &= 6', font_size=96)
        self.add(tex)

</pre></div>
