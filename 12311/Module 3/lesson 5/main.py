import time

class Timer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is IndexError:
            return True
        t = time.time() - self.start
        print('Итоговое время работы', t, 'сек.')



timer  = Timer()
with timer:
    l = [i for i in range(1_00)]
    l[101]