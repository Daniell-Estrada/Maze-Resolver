from copy import deepcopy
from csv import reader


class MazeValidator:
    def __init__(self, path_maze: str) -> None:
        self._path_maze = path_maze
        self.__maze = []
        self.__rutas = []

    @property
    def maze(self) -> list:
        return self.__maze

    @maze.setter
    def maze(self, maze: list):
        self.__maze = maze

    @property
    def rutas(self):
        return self.__rutas

    @rutas.setter
    def rutas(self, rutas: list):
        self.__rutas = rutas

    def read_maze(self) -> None:
        maze = []

        with open(self._path_maze, 'r', encoding='utf-8',) as file:
            maze_reader = reader(file, delimiter=',', skipinitialspace=True)

            for row in maze_reader:
                maze.append([int(cell) for cell in row])

        self.maze = maze

    def maze_verify(self):
        self.read_maze()
        maze = deepcopy(self.maze)

        def size(x): return len(maze[x])

        dirc = [[0, col] for col in range(size(0)) if maze[0][col] == 0]
        dirc += [[row, 0] for row in range(len(maze)) if maze[row][0] == 0]
        dirc += [[row, size(0) - 1]
                 for row in range(len(maze)) if maze[row][-1] == 0]
        dirc += [[len(maze) - 1, col]
                 for col in range(size(-1)) if maze[-1][col] == 0]

        self.solve(maze, dirc[0], dirc[1]) if len(dirc) >= 2 else None
        return self.rutas

    def solve(self, maze, starts, ends, ruta=[]):
        rows = len(maze)
        cols = len(maze[0])

        s_row, s_col = starts
        e_row, e_col = ends

        if [s_row, s_col] in [rows, cols] or maze[s_row][s_col] == 1:
            return False

        if s_row == e_row and s_col == e_col:
            ruta.append([s_row, s_col])

            if not ruta in self.rutas:
                self.rutas.append(ruta)

            return True

        maze[s_row][s_col] = 1

        pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in pos:
            starts = [s_row + i[0], s_col + i[1]]
            self.solve(maze, starts, ends, [*ruta, [s_row, s_col]])

        maze[s_row][s_col] = 0

    def ouput(self):
        if self.maze_verify():
            maze = self.maze
            rutas = self.rutas

            return [maze, sorted(rutas)]

        print('No se puede resolver el laberinto')
        exit(-1)
