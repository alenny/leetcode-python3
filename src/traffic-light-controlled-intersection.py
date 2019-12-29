import threading

class TrafficLight:
    def __init__(self):
        self.activeRoad = 1
        self.lightLock = threading.Lock()

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        self.lightLock.acquire()
        try:
            if self.activeRoad != roadId:
                turnGreen()
                self.activeRoad = 2 if self.activeRoad == 1 else 1
            crossCar()
        finally:
            self.lightLock.release()