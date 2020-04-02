import time
import glob
import os

import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib import style
import numpy as np


style.use("ggplot")
__where = 0

def findLastFile():
    files = glob.glob("{}/logs/Geophone_*.csv".format(os.getcwd()))
    return files[0]

def readFileAuto(**kwargs):
    files = glob.glob("{}/logs/Geophone_*.csv".format(os.getcwd()))
    return readFile(files[0],**kwargs)
    
def readFile(filename, waittime=0.14, timestamp = False, xs=None, vals=[], vols=[]):
    if timestamp:
        xs = []
    with open(filename,"r") as f:
        while 1:
            where = f.tell()
            line = f.readline()
            if not line:
                time.sleep(waittime)
                f.seek(where)
                continue
            vol = None
            val = None
            x = None
            if timestamp:
                x,val,vol = line.split(",")
                xs.append(x)
            else:
                val, vol = line.split(",")
            vals.append(int(val))
            vols.append(float(vol))
            
def readLine(fileStream, waittime=0.14, timestamp = False):
    global __where
    fileStream.seek(__where)
    print("First where: {}".format(__where))
    while 1:
        line = fileStream.readline()
        __where = fileStream.tell()
        print("Second where: {}".format(__where))

        if not line:
            time.sleep(waittime)
            fileStream.seek(__where)
            continue
        vol = None
        val = None
        x = None
        if timestamp:
            x,val,vol = line.split(",")
            #xs.append(x)
        else:
            val, vol = line.split(",")
        #vals.append(int(val))
        #vols.append(float(vol))
        return (x,[int(val),float(vol[:-2])],__where)
    
def animate(i,ax,xs,ys,val_vol,fileStream,timestamp,segment):
    for j in range(segment):
        x,res,where = readLine(fileStream=fileStream,timestamp=timestamp)
        if timestamp:
            xs.append(x)
        ys.append(res[val_vol])
        global __where
        print((__where,where,res))
    
    ax.clear()
    #NOISE LEVEL 1320,1460
    ax.set_ylim(-1000,5000)
    ys = ys[-3000:]
    if timestamp:
        xs = xs[-3000:]
        ax.plot(xs, ys)
    else:
        ax.plot(ys)
    strings = ["Raw Value","Voltage"]
    stringTime = ""
    xlab =""
    if timestamp:
        stringTime = " against Time"
        xlab = "Time"
    plt.title(["{}{}".format(strings[val_vol],stringTime)])
    plt.xlabel(xlab)
    plt.ylabel(strings[val_vol])
    
def plotting(val_vol,timestamp,file = None,interval=1,segment=100):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    if file == None:
        file = findLastFile()
    
    with open(file,"r") as f:
        f.readline()
        global __where
        __where = f.tell()
        ani = animation.FuncAnimation(fig,animate,fargs=(ax,[],[],val_vol,f,timestamp,segment),interval=interval)
        plt.show()
