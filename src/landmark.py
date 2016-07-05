import numpy as np
import matplotlib.pyplot as plt
import random as rdm

import utilities as uts
import coverage_planar_planner.msg as cms



class Landmark(object):


    def __init__(self,
            pos=np.array([0.0,0.0]),
            ori=np.array([1.0,0.0]),
            color='black'
            ):
        self._pos = np.array(pos)
        self._ori = uts.normalize(ori)
        self._color = color

    @classmethod
    def from_msg(cls, msg):
        pos = np.array(msg.position)
        ori = uts.normalize(np.array(msg.orientation))
        return cls(pos, ori)
        
    @classmethod
    def random(cls,
            xlim=(-1.0, 1.0),
            ylim=(-1.0, 1.0),
            ):
        x = rdm.uniform(*xlim)
        y = rdm.uniform(*ylim)
        pos = np.array([x,y])
        ori = uts.normalize(np.random.rand(2)-0.5)
        return cls(pos, ori)

    def to_msg(self):
        msg = cms.Landmark(position=self._pos, orientation=self._ori)
        return msg


    def __str__(self):
        string = "Landmark object for the coverage planner"
        string += "\nPosition: " + str(self._pos)
        string += "\nOrientation: " + str(self._ori)
        return string


    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = np.array(value)


    @property
    def ori(self):
        return self._ori

    @ori.setter
    def ori(self, value):
        self._ori = uts.normalize(value)


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value



    def draw(self,
            draw_orientation=True,
            scale=1.0,
            alpha=0.3,
            color=None
            ):

        if color==None:
            color=self._color
        x = self.pos[0]
        y = self.pos[1]
        point = plt.scatter(x,y,
            s=scale*5.0,
            marker='o',
            color=color,
            alpha=alpha)
        arrow = None
        if draw_orientation:
            vec = self._ori*scale*0.5
            arrow = plt.arrow(x, y, vec[0], vec[1],
                head_width=scale*0.15,
                head_length=scale*0.15,
                alpha=alpha,
                facecolor=color,
                edgecolor=color)
        return point, arrow
        
        
        
        
        
if __name__ == '__main__':
    lmk = Landmark()
    plt.figure()
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    lmk.draw()
    plt.show()
