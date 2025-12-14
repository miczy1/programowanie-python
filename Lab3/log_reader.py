import os

class LogReader:
    def __init__(self, filename, keyword):
        self.filename = filename
        self.keyword = keyword
        self.file = None

        try:
            if os.path.exists(filename):
                self.file = open(filename, 'r', encoding='utf-8')
            else:
                print(f"Błąd: Plik '{filename}' nie istnieje.")
        except IOError as e:
            print(f"Błąd otwarcia pliku: {e}")

    def __iter__(self):
        return self

    def __next__(self):
        if not self.file:
            raise StopIteration

        while True:
            line = self.file.readline()

            if not line:
                self.close_file()
                raise StopIteration

            if self.keyword in line:
                return line.strip()

    def close_file(self):
        if self.file and not self.file.closed:
            self.file.close()

    def __del__(self):
        self.close_file()