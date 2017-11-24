import time


class timer:

    def __enter__(self):
        #print('вход в блок')
        self.t0 = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        #print('выход из блока')
        t1 = time.time()
        total = t1 - self.t0
        print(total)


