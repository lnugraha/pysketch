### Suitable for resource intensive objects

import time

class Producer:
    """ aResource Intensive Object """
    def produce(self):
        print("Producer is busy")

    def meet(self):
        print("Available now")

class Proxy:
    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        print("Artist is checking if the priducer is available")
        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()

        else:
            time.sleep(2)
            print("Producer is busy")

p = Proxy()
p.produce()

#p.occupied() = 'Yes'
#p.produce()