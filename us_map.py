#https://stackoverflow.com/questions/55598249/showing-alaska-and-hawaii-in-cartopy-map

import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom

# A function that draws inset map, ++
# ===================================
def add_insetmap(axes_extent, map_extent, state_name, facecolor, edgecolor, geometry):
    # create new axes, set its projection
    use_projection = ccrs.Mercator()     # preserve shape well
    #use_projection = ccrs.PlateCarree()   # large distortion in E-W for Alaska
    geodetic = ccrs.Geodetic(globe=ccrs.Globe(datum='WGS84'))
    sub_ax = plt.axes(axes_extent, projection=use_projection)  # normal units
    sub_ax.set_extent(map_extent, geodetic)  # map extents

    # add basic land, coastlines of the map
    # you may comment out if you don't need them
    sub_ax.add_feature(cartopy.feature.LAND)
    sub_ax.coastlines()

    sub_ax.set_title(state_name)

    # add map `geometry` here
    sub_ax.add_geometries([geometry], ccrs.PlateCarree(), \
                          facecolor=facecolor, edgecolor=edgecolor)
    # +++ more features can be added here +++

    # plot box around the map
    extent_box = sgeom.box(map_extent[0], map_extent[2], map_extent[1], map_extent[3])
    sub_ax.add_geometries([extent_box], ccrs.PlateCarree(), color='none', linewidth=0.05)


def make_map(map_data,cmap,data_range,map_title):   
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
    
    ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())
    
    shapename = 'admin_1_states_provinces_lakes_shp'
    states_shp = shpreader.natural_earth(resolution='110m',
                                         category='cultural', name=shapename)
    
    
    
    ax.background_patch.set_visible(False)
    ax.outline_patch.set_visible(False)
    
    ax.set_title(map_title)
    
    for state in shpreader.Reader(states_shp).records():
    
    
        edgecolor = 'black'
    
        try:
            # use the name of this state to get pop_density
            facecolor = map_data[state.attributes['postal']]
        except:
            facecolor = "white"
    
    
        # special handling for the 3 states
        # ---------------------------------
        if state.attributes['postal'] in ('AK', 'HI','DC'):
            
            state_name = state.attributes['postal']
    
            # prep map settings
            # experiment with the numbers in both `_extents` for your best results
            if state_name == 'AK':
                map_extent = (-178, -135, 46, 73)    # degrees: (lonmin,lonmax,latmin,latmax)
                axes_extent = (0.04, 0.06, 0.29, 0.275) # axes units: 0 to 1, (LLx,LLy,width,height)
    
            if state_name == 'HI':
                map_extent = (-162, -152, 15, 25)
                axes_extent = (0.27, 0.06, 0.15, 0.15)
                
            if state_name == 'DC':
                map_extent = (-77.2, -76.85, 38.74, 39.03)  
                axes_extent = (0.8, 0.5, 0.07, 0.07)
    
            # add inset maps
            add_insetmap(axes_extent, map_extent, state_name, \
                         facecolor, \
                         edgecolor, \
                         state.geometry)
    
        # the other (conterminous) states go here
        else:
            # `state.geometry` is the polygon to plot
            ax.add_geometries([state.geometry], ccrs.PlateCarree(),
                              facecolor=facecolor, edgecolor=edgecolor)
    
 
    sm = plt.cm.ScalarMappable(cmap=cmap,norm=plt.Normalize(data_range[0],data_range[1]))
    sm._A = []
    plt.colorbar(sm,ax=ax,fraction=0.02)
    
    plt.show()