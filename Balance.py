class Balance:
    global l, r
    l = 0
    r = 0

    def add_right(self, weight):
        global r
        r += weight

    def add_left(self, weight):
        global l
        l += weight

    def result(self):
        global l, r
        if l > r:
            print("L")
        elif r > l:
            print("R")
        elif r == l:
            print('=')
