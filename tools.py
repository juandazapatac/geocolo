# Imports
import csv
import numpy as np

# Functions
def ask_elevation():
    elevation=float(input("Insert the elevation in meters: "))
    return elevation
    
def menu1(e):
    dem1=np.where(dem>=e,dem,0).astype(np.int64)
    return dem1

def menu2():
    return dem.mean()

# csv data manipulation
with open("./DEM_example.csv") as csvfile:
    reader=csv.reader(csvfile)
    dem=np.array(list(reader),dtype=np.int64)
    
with open("./band4.csv") as csvfile:
    band4_raster=np.array(list(csv.reader(csvfile)),dtype=np.int64)

with open("./band5.csv") as csvfile:
    band5_raster=np.array(list(csv.reader(csvfile)),dtype=np.int64)

# NDVI calculation
ndvi_raster=(band5_raster-band4_raster)/(band5_raster+band4_raster)
np.save("ndvi_array",ndvi_raster)

