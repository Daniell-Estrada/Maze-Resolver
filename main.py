from MazeValidator import MazeValidator
from MazeShow import MazeShow


def main():
    maze, rutas = MazeValidator('maze.csv').ouput()
    MazeShow(maze, rutas).show()


if __name__ == '__main__':
    main()
