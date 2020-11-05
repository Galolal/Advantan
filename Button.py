class Button:
    global c
    c = 0

    def click(self):
        global c
        c += 1

    def click_count(self):
        global c
        print(c)

    def reset(self):
        global c
        c = 0
