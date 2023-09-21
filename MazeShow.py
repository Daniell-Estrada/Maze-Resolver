from game2dboard import Board, Cell
import tkinter as tk

class MazeShow(Board):
    def __init__(self, maze: list, rutas: list) -> None:
        nrows = len(maze)
        ncols = len(maze[0])
        self.maze = maze
        self.rutas = rutas
        self.pos_actual = -1
        self.canvas = None
        self.label = None
        super().__init__(nrows, ncols)

    def navbar(self):
        self.canvas = tk.Canvas(self._root, bg='dark sea green',
                                width=100, height=50, highlightbackground='dark sea green')
        self.label = self.canvas.create_text(50, 25, font=('Arial', 14), fill='white')
        self.canvas.pack()

    def set_label(self, text):
        self.canvas.itemconfig(self.label, text=text)

    def configure(self) -> Board:
        self.title = 'Maze'
        self.cell_spacing = 3
        self.cell_size = 45
        self.margin = 10
        self.grid_color = "dark sea green"
        self.margin_color = "dark sea green"
        self.cell_color = 'sea green'
        self.on_key_press = self.key_press
        self._root.configure(bg='dark sea green')
        return self

    def move(self, key):
        if 0 <= key < len(self.rutas):
            self.set_label(f'Ruta {key + 1} / {len(self.rutas)}')

            for i in self.rutas[key]:
                self.pause(30, False)
                self.color_rutas(i[0], i[1], '#006FF8')

    def key_press(self, key):
        self.default_colors()

        match key:
            case 'Escape' | 'q':
                self.close()

            case 'Left' | 'Right':
                self.pos_actual += 1 if key == 'Right' else -1
                self.pos_actual %= len(self.rutas)
                self.move(self.pos_actual)

            case key if key.isdigit():
                key = int(key)
                self.move(key - 1)
                self.pos_actual = key -1

    def color_rutas(self, row, col,  bgcolor):
        x, y = self._rc2xy(row, col)
        newcell = Cell(self._canvas, x, y)
        newcell.bgcolor = bgcolor
        self._cells[row][col] = newcell

    def default_colors(self):
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.maze[row][col] == 0:
                    self.color_rutas(row, col, 'white')

                if self.maze[row][col] == 1:
                    self[row][col] = 'arbusto.png'

    def all_rutas(self) -> list:
        for i in range(len(self.rutas)):
            self.set_label(f'Ruta {i + 1} / {len(self.rutas)}')
            self.move(i)
            self.pause(300, False)
            self.default_colors()

    def _setupUI(self):
        self.navbar()
        super()._setupUI()
        self.default_colors()
        self.all_rutas()
        self.set_label(f'Maze')

    def show(self):
        self.configure()
        super().show()
