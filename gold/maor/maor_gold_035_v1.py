# Created by maor

from utils.reading_tasks import read_task
from src.hexagen import HexagonsGame, Tile, Shape, Line, Circle, Triangle

task_index = 35
gold_boards = list(read_task(task_index)['gold_boards'])

HexagonsGame.start()

# description:
# task index: 35, image: P01C02T09, collection round: 1, category: bounded iteration, group: train
# agreement scores: [[1, 1, 1], [0, 0, 1.0], [0.29, 0.29, 1.0], [0.2, 0.18, 0.8], [0.29, 0.09, 0.44], [0.32, 0.1, 0.34]]

'''
1. On the bottom of the board, count over to the 5th cell that extends down from
the body.
'''


'''
2. Skip the first 5 cells in that column and color the 6th cell red.
'''
tile1 = Tile(column=10, row = -6)
tile1.draw('red')

'''
3. Create a ring by coloring all cells touching the cell in the previous step blue.
'''
neighbors = tile1.neighbors()
neighbors.draw('blue')

'''
4. From the bottom and top most cells in the previous step, skip the cell touching
the 2 diagonal edges and paint the next cell on the diagonal red.
'''
tile2 = neighbors.get(criterion='up_right')
tile2.draw('red')

'''
5. Repeat step 3 for all four new red cells, but this time use orange.
'''


'''
6. Uncolor all red cells.
'''

HexagonsGame.plot(gold_boards=gold_boards, multiple=0)
