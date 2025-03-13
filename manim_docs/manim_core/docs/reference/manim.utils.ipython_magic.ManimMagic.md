# ManimMagic

Qualified name: `manim.utils.ipython\_magic.ManimMagic`

### *class* ManimMagic(\*\*kwargs)

Bases: `Magics`

Create a configurable given a config config.

* **Parameters:**
  * **config** (*Config*) – If this is empty, default values are used. If config is a
    `Config` instance, it will be used to configure the
    instance.
  * **parent** (*Configurable instance* *,* *optional*) – The parent Configurable instance of this object.
  * **shell** (*InteractiveShell*)

### Notes

Subclasses of Configurable must call the `__init__()` method of
`Configurable` *before* doing anything else and using
`super()`:

```default
class MyConfigurable(Configurable):
    def __init__(self, config=None):
        super(MyConfigurable, self).__init__(config=config)
        # Then any other code you need to finish initialization.
```

This ensures that instances will be configured properly.

### Methods

| `add_additional_args`                                  |                                                 |
|--------------------------------------------------------|-------------------------------------------------|
| [`manim`](#manim.utils.ipython_magic.ManimMagic.manim) | Render Manim scenes contained in IPython cells. |

### Attributes

| `config`                | A trait whose value must be an instance of a specified class.                    |
|-------------------------|----------------------------------------------------------------------------------|
| `cross_validation_lock` | A contextmanager for running a block with our cross validation lock set to True. |
| `magics`                |                                                                                  |
| `options_table`         |                                                                                  |
| `parent`                | A trait whose value must be an instance of a specified class.                    |
| `registered`            |                                                                                  |
| `shell`                 |                                                                                  |

#### manim(line, cell=None, local_ns=None)

Render Manim scenes contained in IPython cells.
Works as a line or cell magic.

Please refer to [https://jupyter.org/](https://jupyter.org/) for more information about JupyterLab
and Jupyter notebooks.

Usage in line mode:

```default
%manim [CLI options] MyAwesomeScene
```

Usage in cell mode:

```default
%%manim [CLI options] MyAwesomeScene

class MyAweseomeScene(Scene):
    def construct(self):
        ...
```

Run `%manim --help` and `%manim render --help` for possible command line interface options.

#### NOTE
The maximal width of the rendered videos that are displayed in the notebook can be
configured via the `media_width` configuration option. The default is set to `25vw`,
which is 25% of your current viewport width. To allow the output to become as large
as possible, set `config.media_width = "100%"`.

The `media_embed` option will embed the image/video output in the notebook. This is
generally undesirable as it makes the notebooks very large, but is required on some
platforms (notably Google’s CoLab, where it is automatically enabled unless suppressed
by `config.embed = False`) and needed in cases when the notebook (or converted HTML
file) will be moved relative to the video locations. Use-cases include building
documentation with Sphinx and JupyterBook. See also the [`manim directive for Sphinx`](manim.utils.docbuild.manim_directive.md#module-manim.utils.docbuild.manim_directive).

### Examples

First make sure to put `import manim`, or even `from manim import *`
in a cell and evaluate it. Then, a typical Jupyter notebook cell for Manim
could look as follows:

```default
%%manim -v WARNING --disable_caching -qm BannerExample

config.media_width = "75%"
config.media_embed = True

class BannerExample(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner_large = ManimBanner(dark_theme=False).scale(0.7)
        self.play(banner_large.create())
        self.play(banner_large.expand())
```

Evaluating this cell will render and display the `BannerExample` scene defined in the body of the cell.

#### NOTE
In case you want to hide the red box containing the output progress bar, the `progress_bar` config
option should be set to `None`. This can also be done by passing `--progress_bar None` as a
CLI flag.

* **Parameters:**
  * **line** (*str*)
  * **cell** (*str* *|* *None*)
  * **local_ns** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
* **Return type:**
  None
