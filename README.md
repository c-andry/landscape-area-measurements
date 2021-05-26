# landscape-area-measurements
This repository contains a notebook for classifying landcover and calculating landscaped areas for an urban setting.

[![DOI](https://zenodo.org/badge/368932347.svg)](https://zenodo.org/badge/latestdoi/368932347)


## Background
In 2018, the state of California passed legislation related to water conservation and drought planning. This legislation will require all urban water retailers to meet state-defined annual water use targets. To meet these objectives, retailers will need to more closely track the different components of their water use budgets (e.g. residential indoor, residential outdoor, commercial outdoor, etc.).

This workflow focuses specifically on commercial parcels, and will outline an approach for retailers to remotely calculate the total landscaped area of these properties using classified 1 meter resolution NAIP imagery, county parcel data, and point locations of irrigation meters.

<<<<<<< HEAD
# Description of files in this repository
* landscape-area-measurements.ipynb : Notebook that classifies imagery and calculates total commercial landscaped area for a given agency's service area.
* lam-functions.py : Module containing functions for running notebook.
* landscape-area-measurements.html : Blog post describing project and displaying results.

# Running this workflow

## Environment
This workflow utilizes the <a href="https://github.com/earthlab/earth-analytics-python-env" target="_blank"> earth-analytics-python environment </a>.

## Data used
* 4-band NAIP imagery rasters - Individual tiles can be downloaded from <a href="https://earthexplorer.usgs.gov/" target="_blank"> USGS Earth Explorer </a>.
* County parcel shapefile - e.g. <a href="https://geohub.lacity.org/datasets/lahub::la-county-parcels/about" target="_blank"> LA County Parcel Data </a>.
* Landcover training polygon shapefile - For this workflow, shapefile was manually created in ArcGIS Pro.
* Agency (or area of interest) service area boundary shapefile
=======
## Packages used
* geopandas
* matplotlib
* earthpy
* rioxarray
* rasterio
* scikit-learn

## Data used
* 4-band NAIP imagery rasters
* County parcel shapefile
* Landcover training polygon shapefile
* Agency (or area of interest) service area boundary shapefile

## Description of files in this repository
landscape-area-measurements.ipynb : Notebook that classifies imagery and calculates total commercial landscaped area for a given agency's service area.
>>>>>>> f4aa171bd156a301f04b8b121921c57e48b34d4b

## Analysis Workflow
* Open landscape-area-measurements.ipynb notebook
* Change directory to where data are stored
* Run notebook
