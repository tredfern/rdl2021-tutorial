# Copyright (c) 2021 Trevor Redfern
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class Action:
  pass

class EscapeAction:
  pass

class MovementAction:
  def __init__(self, dx: int, dy: int):
    super().__init__()

    self.dx = dx
    self.dy = dy