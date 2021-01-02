import numpy
import matplotlib.pyplot as plt

class coordinate :
    def __init__(self , x, y):
      self.x=x
      self.y=y

    @staticmethod
    def get_distance(a,b):
        return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))

    @staticmethod
    def get_distance(coords):
        dist = 0
        for first, second in zip( coords[:-1],coords [1:]):
            dist += coordinate.get_distance(first, second)
        dist += coordinate.get_distance( coords[0],coords [-1])
        return dist

if __name__ == '__main__':
    coords=[]
    for i in range(20):
        coords.append(coordinate(numpy.random.uniform(), numpy.random.uniform()))

    fig = plt.figure(figsize =(10,5))
    ax1=fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    for first , second in zip(coords[:-1],coords[1:]):
        ax1.plot([first.x , second.x],[first.y,second.y], 'b')
    ax1.plot([coords[0].x,coords[-1].x],[coords [0].y,coords[-1].y],'b')
    for c in coords:
        ax1.plot(c.x ,c.y ,'ro')

        plt.show()