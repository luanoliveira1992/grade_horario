from python import Grade

class Populacao():
    grades = None;
    tamPop = None;
    
    def __init__(self, tamPop):
        self.grades = []
        self.tamPop = tamPop;
        for i in range(0,self.tamPop):
            self.grades.append(Grade())
            
        