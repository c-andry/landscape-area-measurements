# landscape-area-measurements
This repository contains a notebook for classifying landcover from a single NAIP tile and calculating vegetation areas.

[![DOI](https://zenodo.org/badge/368932347.svg)](https://zenodo.org/badge/latestdoi/368932347)


## Background
In 2018, the state of California passed legislation related to water conservation and drought planning. This legislation will require all urban water retailers to meet state-defined annual water use targets. To meet these objectives, retailers will need to more closely track the different components of their water use budgets (e.g. residential indoor, residential outdoor, commercial outdoor, etc.).

This workflow focuses specifically on commercial parcels, and will outline an approach for retailers to remotely calculate the total landscaped area of these properties using classified 1 meter resolution NAIP imagery, county parcel data, and point locations of irrigation meters.

# Description of files in this repository
* landscape-area-measurements.ipynb : Notebook that classifies imagery and calculates total commercial landscaped area for a given agency's service area.
* lam-functions.py : Module containing functions for running notebook.
* landscape-area-measurements.html : Blog post outlining project and displaying results.

# Running this workflow

## Environment
This workflow utilizes the <a href="https://github.com/earthlab/earth-analytics-python-env" target="_blank"> earth-analytics-python environment </a>.

## Data used
* 4-band NAIP imagery rasters - Individual tiles can be downloaded from <a href="https://earthexplorer.usgs.gov/" target="_blank"> USGS Earth Explorer </a>.
* County parcel vector data - e.g. <a href="https://geohub.lacity.org/datasets/lahub::la-county-parcels/about" target="_blank"> LA County Parcel Data </a>.
* Landcover training polygon shapefile - For this workflow, training data for the 3 landcover classes were manually created in ArcGIS Pro.
=======
## Packages used
* geopandas
* matplotlib
* json
* requests
* earthpy
* xarray
* rioxarray
* rasterio
* shapely
* sklearn

## Analysis Workflow
* Create training dataset - I used ArcGIS Pro to manually draw polygons delineating pixels of known classes. Export data as a raster of same extent as NAIP tile and save to data/training folder.
* Clone landscape-area-measurements repo to local directory
* Open landscape-area-measurements.ipynb notebook
* Adjust file paths as needed for training data, NAIP tile, and any data-specific masks. 
* Run notebook
