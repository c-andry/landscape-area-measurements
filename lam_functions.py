# Define functions used in the landscape-area-measurements notebook
import numpy as np
import json
import requests
import pandas as pd
import geopandas as gpd
import numpy.ma as ma
import xarray as xr
import rioxarray as rxr
import rasterio as rio
from rasterio.crs import CRS
from shapely.geometry import Polygon, shape, mapping

def clean_array_plot(xr_obj):
    """Takes a single xarray object as an input and produces a cleaned numpy
    array output for plotting.

    Parameters
    ----------
    xr_obj : xarray DataArray
        xarray object containing null values

    Returns
    ----------
    masked_array : numpy array
        masked numpy array
    """
    masked_array = ma.masked_array(xr_obj.values,  xr_obj.isnull())

    return masked_array


def get_cii_parcel_polygons(naip_tile):
    """Retrieves non-residential/CII parcel polygons for extent of
    input NAIP tile using City of Los Angeles : LA County
    Parcels API.

    Parameters
    ----------
    naip_tile : xarray DataArray
        NAIP tile to use as bounds of API query

    Returns
    -------
    cii_parcel_gdf : GeoDataFrame
        GeoDataFrame of all CII parcel polygons in tile area
    """
    cii_uses = ['Recreational',
                'Commercial',
                'Insitutitonal',
                'Government',
                'Industrial']
    crs_wgs84 = CRS.from_string('EPSG:4326')

    naip_tile_reproj = naip_tile.rio.reproject(crs_wgs84)
    (xmin, ymin, xmax, ymax) = naip_tile_reproj.rio.bounds()

    center_geom_str = "CENTER_LAT%20%3E%3D%20"+str(ymin)+"%20AND%20CENTER_LAT%20%3C%3D%20"+str(
        ymax)+"%20AND%20CENTER_LON%20%3E%3D%20"+str(xmin)+"%20AND%20CENTER_LON%20%3C%3D%20"+str(xmax)

    parcel_gdf_list = []

    for use in cii_uses:
        use_parcel_url = "https://public.gis.lacounty.gov/public/rest/services/LACounty_Cache/LACounty_Parcel/MapServer/0/query?where=" + \
            center_geom_str+"AND%20UseType%3D'"+use + \
            "'&outFields=APN,SitusCity,SitusZIP,UseType,UseDescription,LAT_LON,OBJECTID&outSR=4326&f=json"
        try:
            return_dict = json.loads(requests.get(use_parcel_url).text)
        except ConnectionError:
            print('Connection could not be made to database.')
        parcel_df = pd.DataFrame(columns=[x["name"]
                                          for x in return_dict["fields"]])
        parcel_df.insert(loc=7, column='geometry', value=np.nan)
        parcel_df['geometry'] = parcel_df['geometry'].astype('geometry')

        for i in np.arange(0, len(return_dict['features']), 1):
            att_dict = return_dict['features'][i]['attributes']
            parcel_df = parcel_df.append(att_dict, ignore_index=True)
            geom_dict = return_dict['features'][i]['geometry']
            geom_df = pd.DataFrame(
                data=[str(geom_dict['rings'])], columns=['geometry'])
            poly_data = Polygon(eval(geom_df.geometry.loc[0])[0])
            poly_gdf = gpd.GeoSeries(poly_data)
            parcel_df.loc[i]['geometry'] = poly_gdf[0]

        parcel_gdf = gpd.GeoDataFrame(parcel_df,
                                      geometry=parcel_df['geometry'],
                                      crs=crs_wgs84)
        parcel_gdf_list.append(parcel_gdf)
    cii_parcel_gdf = pd.concat(parcel_gdf_list)
    return cii_parcel_gdf


def mask_and_fill(xr_obj, valid_range, fill_value):
    """Masks xarray object using specified valid range and fills nan
    values with fill_value to use as RandomForestClassifier feature input.

    Parameters
    ----------
    xr_obj : xarray DataArray
        DataArray with values to mask and fill

    valid_range : tuple
        The min and max valid range for the data. All pixels with values
        outside of this range will be masked.

    fill_value : integer
        Value to replace nan values

    Returns
    -------
    masked_filled_array : xarray DataArray
        DataArray with masked and filled values.
    """
    # Define and apply mask
    mask = ((xr_obj < valid_range[0]) | (xr_obj > valid_range[1]))
    masked_array = xr_obj.where( ~xr.where(mask, True, False))
    # Fill nan values with specified fill_value
    masked_filled_array = masked_array.fillna(fill_value)

    return masked_filled_array
