# Copyright (c) 2021 Trevor Redfern
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from engine import Engine
  from entity import Entity


class Action:
  def perform(self, engine: Engine, entity: Entity) -> None:
    raise NotImplementedError()

class EscapeAction:
  def perform(self, engine: Engine, entity: Entity) -> None:
    raise SystemExit()

class MovementAction:
  def __init__(self, dx: int, dy: int):
    super().__init__()

    self.dx = dx
    self.dy = dy

  def perform(self, engine: Engine, entity: Entity) -> None:
    destX = entity.x + self.dx
    destY = entity.y + self.dy

    if not engine.gameMap.inBounds(destX, destY):
      return
    
    if not engine.gameMap.tiles["walkable"][destX, destY]:
      return

    entity.move(self.dx, self.dy)