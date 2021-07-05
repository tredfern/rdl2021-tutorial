# Copyright (c) 2021 Trevor Redfern
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Tuple

import numpy as np

graphicDataType = np.dtype(
  [
    ("ch", np.int32),
    ("fg", "3B"),
    ("bg", "3B")
  ]
)

tileDataType = np.dtype(
  [
    ("walkable", np.bool),
    ("transparent", np.bool),
    ("dark", graphicDataType)
  ]
)

def newTile(
  *,
  walkable: int,
  transparent: int,
  dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]
) -> np.ndarray:
  return np.array((walkable, transparent, dark), dtype = tileDataType)

floor = newTile(
  walkable = True, transparent = True, dark = (ord(" "), (255, 255, 255), (50, 50, 150))
)
wall = newTile(
  walkable=False, transparent = False, dark = (ord(" "), (255, 255, 255), (0, 0, 100))
)