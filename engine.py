# Copyright (c) 2021 Trevor Redfern
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

class Engine:
  def __init__(self, entities: Set[Entity], eventHandler: EventHandler, gameMap: GameMap, player: Entity):
    self.entities = entities
    self.eventHandler = eventHandler
    self.gameMap = gameMap
    self.player = player

  def handleEvents(self, events: Iterable[Any]) -> None:
    for event in events:
      action = self.eventHandler.dispatch(event)

      if action is None:
        continue
        
      action.perform(self, self.player)

  def render(self, console: Console, context: Context):
    self.gameMap.render(console)

    for entity in self.entities:
      console.print(entity.x, entity.y, entity.char, fg = entity.color)

    context.present(console)

    console.clear()
