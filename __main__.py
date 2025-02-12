"""
ANN




"""

import numpy as np

x=np.array([[0.1,-1.2,-0.3,0.2,-1,-0.0],[0,1.2,-1,-2,0.9,0.2]])

biases = 0.3

class NN:
    def __init__(self):
        self.Y=np.array([0.1,0.2,0.2,0.1,0.8,0.8])
    def forward(self,X):
        self.Y = (self.Y * X) + biases
        self.ReLU()


    def backProp(self):...

    def ReLU(self):
        p = 0
        for i in  self.Y:
            self.block=len(i)
            q=0
            for j in i:
                if(j < 0): self.Y[p][q] = 0;
                q+=1 
            p+=1;
    
    def lookUp(self):
        print(self.Y)

    def clean(self):
        self.Y=np.zeros(len(self.Y)*self.block)

nn = NN()
nn.forward(x)
# nn.ReLU()
for i in range(10):
    print(f"interation :: {i}")
    nn.forward(x)
    nn.lookUp()

nn.clean()
nn.lookUp()



