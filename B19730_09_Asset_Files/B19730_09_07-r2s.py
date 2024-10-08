import pickle
from linecache import getline
import shapefile

def pix2coord(gt,x,y):
    w = gt[0]
    h = gt[1]
    ox = gt[2]
    oy = gt[3]
    pw = gt[4]
    ph = gt[4]
    cx = ox + (x * pw)
    cy = (oy + (ph*h)) - (y * ph)
    return cx, cy

        
with open("path.p", "rb") as pathFile:
    path = pickle.load(pathFile)

# Parse the header
hdr = [getline("path.asc", i) for i in range(1, 7)]
gt = [float(ln.split(" ")[-1].strip()) for ln in hdr]
    
coords = []

for y,x in path:
    coords.append(pix2coord(gt,x,y))

with shapefile.Writer("path", shapeType=shapefile.POLYLINE) as w:
    w.field("NAME")
    w.record("LeastCostPath")
    w.line([coords])
    