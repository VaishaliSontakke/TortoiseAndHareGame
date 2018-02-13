class tortoise:

    def __init__(self):
        self.countsteps = 0
        self.no_steps_sec = 1


    def walk(self):
        self.countsteps += self.no_steps_sec

    def stop_for_food(self):
        return

    def is_reached(self, max_steps):
        if self.countsteps == max_steps:
            return True
        return False

