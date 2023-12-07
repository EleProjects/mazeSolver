from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(25, 25, 50, 50)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(50, 50, 75, 75)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(75, 75, 100, 100)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(100, 100, 125, 125)

    win.wait_for_close()

main()