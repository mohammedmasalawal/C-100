class Car (object):
    def __init__(self,color,speed,model,company):
        self.color=color
        self.speed=speed
        self.model=model
        self.company=company

    def start(self):
        print("car started")
    
    def stop(self):
        print("car stopped")
    
    def accelerate(self):
        print("car acceierating")

    def change_gear(self):
        print("gear changed")

Buggati=Car ("red",500,"chiron","Buggati")
Buggati.start()
#print(Buggati.stop())
#print(Buggati.accelerate())
#print(Buggati.change_gear())
