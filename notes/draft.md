Minimum Shmup



* a player vessel that can move on both axes X, Y (and both at the same time)
* a discrete 2D board



* non-player objects with
  * move patterns (eg enter from left side, leave from right side)
  * shoot patterns (create other non-player objects)
  * item drops ? drop down or left (in the opposite direction of the scroll)
  * or, stationary items with HP and also a TTL

Basic weapons:

* projectiles
* lasers (a stationary projectile which can rotate ?)

Handling collisions:

* Using a grid and a faction system (player, not player, or if there are several types of enemies, multiple more factions)



# shmupy

The goal; make a shmup.

That would be, a 2D board where the player controls a small vessel which can move on both axes. While the board does not move, the background does, giving an illusion of ongoing movement from the player's perspective, either vertically (going up) or horizontally (going right).

## Random ideas

We could mishmash this with other game genres such as race games (give power ups
