# SpaceScene

Qualified name: `manim\_physics.rigid\_mechanics.rigid\_mechanics.SpaceScene`

### *class* SpaceScene(renderer=None, \*\*kwargs)

Bases: `Scene`

A basis scene for all of rigid mechanics. The gravity vector
can be adjusted with `self.GRAVITY`.

### Methods

| [`add_body`](#manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene.add_body)                 | Bodies refer to pymunk's object.                |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [`make_rigid_body`](#manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene.make_rigid_body)   | Make any mobject movable by gravity.            |
| [`make_static_body`](#manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene.make_static_body) | Make any mobject interactable by rigid objects. |
| [`setup`](#manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene.setup)                       | Used internally                                 |
| [`stop_rigidity`](#manim_physics.rigid_mechanics.rigid_mechanics.SpaceScene.stop_rigidity)       | Stop the mobjects rigidity                      |

### Attributes

| `GRAVITY`   |                                        |
|-------------|----------------------------------------|
| `camera`    |                                        |
| `time`      | The time since the start of the scene. |

#### add_body(body)

Bodies refer to pymunk’s object.
This method ties Mobjects to their Bodies.

* **Parameters:**
  **body** (*Mobject*)

#### make_rigid_body(\*mobs, elasticity=0.8, density=1, friction=0.8)

Make any mobject movable by gravity.
Equivalent to `Scene`’s `add` function.

* **Parameters:**
  * **mobs** (*Mobject*) – The mobs to be made rigid.
  * **elasticity** (*float*)
  * **density** (*float*)
  * **friction** (*float*) – The attributes of the mobjects in regards to
    interacting with other rigid and static objects.

#### make_static_body(\*mobs, elasticity=1, friction=0.8)

Make any mobject interactable by rigid objects.

* **Parameters:**
  * **mobs** (*Mobject*) – The mobs to be made static.
  * **elasticity** (*float*)
  * **friction** (*float*) – The attributes of the mobjects in regards to
    interacting with rigid objects.
* **Return type:**
  None

#### setup()

Used internally

#### stop_rigidity(\*mobs)

Stop the mobjects rigidity

* **Parameters:**
  **mobs** (*Mobject*)
* **Return type:**
  None
