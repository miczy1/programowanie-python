class Board:
    def __init__(self, n=8):
        self.n = n
        self.queens = []  # Stan aktualnego rozwiązania
        self.solutions = []  # Lista znalezionych rozwiązań

    def place(self, col):
        self.queens.append(col)

    def remove(self):
        if self.queens:
            self.queens.pop()

    def is_safe(self, col):
        current_row = len(self.queens)

        for row, q_col in enumerate(self.queens):
            if q_col == col:
                return False

            if abs(current_row - row) == abs(col - q_col):
                return False

        return True

    def solve(self):
        self.solutions = []
        self._backtrack()
        return len(self.solutions)

    def _backtrack(self):
        if len(self.queens) == self.n:
            self.solutions.append(list(self.queens))
            return

        for col in range(self.n):
            if self.is_safe(col):
                self.place(col)  # Krok naprzód
                self._backtrack()  # Rekurencja
                self.remove()  # Nawrót (backtrack)


    def __len__(self):
        return len(self.queens)

    def __iter__(self):
        for row, col in enumerate(self.queens):
            yield (row, col)

    def __contains__(self, pos):
        if isinstance(pos, tuple) and len(pos) == 2:
            row, col = pos
            return 0 <= row < len(self.queens) and self.queens[row] == col
        return False

    def __str__(self):
        if not self.queens:
            return "Pusta plansza lub brak rozwiązania w bieżącym kontekście."

        lines = []
        lines.append(f"--- Plansza {self.n}x{self.n} ---")
        for row in range(self.n):
            line = []
            for col in range(self.n):
                if row < len(self.queens) and self.queens[row] == col:
                    line.append("Q")  # Królowa
                else:
                    line.append(".")  # Puste pole
            lines.append(" ".join(line))
        return "\n".join(lines)


def solve_n_queens(n=8):
    b = Board(n)
    count = b.solve()
    return count, b.solutions