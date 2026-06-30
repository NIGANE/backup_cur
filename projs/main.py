

class Dr:

    def __init__(self, x: int):
        self.x = x

    def __eq__(self, dr):
        if dr.x == self.x:
            return True
        return False


def pop(drones, drone):
    for dro in drones:
        if dro == drone:
            return (list(set(drones) - set([drone])))


arr = [Dr(1), Dr(2), Dr(3), Dr(4)]

print(pop(arr, Dr(1)))