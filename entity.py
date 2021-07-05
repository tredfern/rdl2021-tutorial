# Copyright (c) 2021 Trevor Redfern
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Tuple

class Entity:
  """
  The entity base class to represent the things
  """
  def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
    self.x = x
    self.y = y
    self.char = char
    self.color = color

  def move(self, dx: int, dy: int):
    self.x += dx
    self.y += dy