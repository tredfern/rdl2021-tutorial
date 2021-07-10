# Copyright (c) 2021 Trevor Redfern
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from __future__ import annotations
from typing import Tuple, Iterator, List, TYPE_CHECKING
import random
import tcod
from game_map import GameMap
import tile_types

if TYPE_CHECKING:
  from entity import Entity

class RectangularRoom:  
  def __init__(self, x: int, y: int, width: int, height: int) -> None:
      self.x1 = x
      self.y1 = y
      self.x2 = x + width
      self.y2 = y + height

  @property
  def center(self) -> Tuple[int, int]:
    centerX = int((self.x1 + self.x2) / 2)
    centerY = int((self.y1 + self.y2) / 2)

    return centerX, centerY

  @property
  def inner(self) -> Tuple[slice, slice]:
    return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

  def intersects(self, other: RectangularRoom) -> bool:
    return (
      self.x1 <= other.x2 and
      self.x2 >= other.x1 and
      self.y1 <= other.y2 and
      self.y2 >= other.y1
    )


def generateDungeon(
  maxRooms: int,
  roomMinSize: int,
  roomMaxSize: int,
  mapWidth: int,
  mapHeight: int,
  player: Entity) -> GameMap:

  dungeon = GameMap(mapWidth, mapHeight)

  rooms: List[RectangularRoom] = []

  for r in range(maxRooms):
    roomWidth = random.randint(roomMinSize, roomMaxSize)
    roomHeight = random.randint(roomMinSize, roomMaxSize)

    x = random.randint(0, dungeon.width - roomWidth - 1)
    y = random.randint(0, dungeon.height - roomHeight - 1)

    newRoom = RectangularRoom(x, y, roomWidth, roomHeight)

    if any(newRoom.intersects(otherRoom) for otherRoom in rooms):
      continue
      
    dungeon.tiles[newRoom.inner] = tile_types.floor

    if len(rooms) == 0:
      player.x, player.y = newRoom.center
    else:
      for x, y in tunnelBetween(rooms[-1].center, newRoom.center):
        dungeon.tiles[x, y] = tile_types.floor

    rooms.append(newRoom)

  return dungeon

def tunnelBetween( start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
  x1, y1 = start
  x2, y2 = end

  if random.random() < 0.5:
    cornerX, cornerY = x2, y1
  else:
    cornerX, cornerY = x1, y2

  for x, y in tcod.los.bresenham((x1, y1), (cornerX, cornerY)).tolist():
    yield x, y
  
  for x, y in tcod.los.bresenham((cornerX, cornerY), (x2, y2)).tolist():
    yield x, y
  

