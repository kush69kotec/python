import time


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for elem in TrafficLight.__color:
            print(elem)
            time.sleep(TrafficLight.__color[elem])


a = TrafficLight()
a.running()
