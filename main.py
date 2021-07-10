#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generateDungeon

def main() -> None:
  screenWidth = 80
  screenHeight = 50
  mapWidth = 80
  mapHeight = 45

  roomMaxSize = 10
  roomMinSize = 6
  maxRooms = 30

  tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
  eventHandler = EventHandler()

  player = Entity(int(screenWidth / 2), int(screenHeight / 2), "@", (255, 255, 255))
  npc = Entity(int(screenWidth / 2) - 5, int(screenHeight / 2), "N", (255, 255, 0))
  entities = { player, npc }

  gameMap = generateDungeon(maxRooms, roomMinSize, roomMaxSize, mapWidth, mapHeight, player)
  engine = Engine(entities, eventHandler, gameMap, player)

  with tcod.context.new_terminal(
    screenWidth,
    screenHeight,
    tileset = tileset,
    title = "Fairhaven Adventures",
    vsync = True
  ) as context:
    rootConsole = tcod.Console(screenWidth, screenHeight, order = "F")
    while (True):
      engine.render(rootConsole, context)

      engine.handleEvents(tcod.event.wait())

if __name__ == "__main__":
  main()