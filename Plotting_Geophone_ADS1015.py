import time
import glob
import os

import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib import style
import numpy as np


style.use("ggplot")

def readFileAuto():
    files = glob.glob("{}/logs/Geophone_*.csv".format(os.getcwd()))
    readFile(files[0])
    
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
                
