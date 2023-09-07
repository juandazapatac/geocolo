# RASTER ANALYST
# All units in meters

#Imports
from tools import ask_elevation,menu1,menu2,ndvi_raster

def run():
    # UI
    menu=input("""Welcome to your Raster Analyst,
                  Press 1 to see the cells above a specific level
                  Press 2 to see the average height
                  Press 3 to calculate the NDVI
                  :""")
    if menu=="1":
        elevation=ask_elevation()
        print(menu1(elevation))
    if menu=="2":
        print(menu2(),"m")
    if menu=="3":
        print(ndvi_raster)        

if __name__=="__main__":
    run()