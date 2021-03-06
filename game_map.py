# Copyright (c) 2021 Trevor Redfern
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np
from tcod.console import Console

import tile_types

class GameMap:
  def __init__(self, width: int, height: int) -> None:
      self.width, self.height = width, height
      self.tiles = np.full((width, height), fill_value=tile_types.wall, order = "F")

  def inBounds(self, x: int, y: int) -> bool:
    return 0 <= x < self.width and 0 <= y < self.height

  def render(self, console: Console):
    console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]

