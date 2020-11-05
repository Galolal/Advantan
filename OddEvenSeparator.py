class OddEvenSeparator:
    global l, ol, el

    def add_number(self, *args):
        global l
        l = []
        l.append(args)
        print(*l)

    def even(self):
        global l
        global ol
        el = []
        for i in l:
            for j in i:
                if j % 2 == 0:
                    el.append(j)
        print(el)

    def odd(self):
        global l
        global ol
        ol = []
        for i in l:
            for j in i:
                if j % 2 != 0:
                    ol.append(j)
        print(ol)
