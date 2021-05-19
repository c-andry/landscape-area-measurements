# landscape-area-measurements
This repository contains a notebook for classifying landcover and calculating landscaped areas for an urban setting.
[![DOI](https://zenodo.org/badge/368932347.svg)](https://zenodo.org/badge/latestdoi/368932347)


## Background
In 2018, the state of California passed legislation related to water conservation and drought planning. This legislation will require all urban water retailers to meet state-defined annual water use targets. To meet these objectives, retailers will need to more closely track the different components of their water use budgets (e.g. residential indoor, residential outdoor, commercial outdoor, etc.).

This workflow focuses specifically on commercial parcels, and will outline an approach for retailers to remotely calculate the total landscaped area of these properties using classified 1 meter resolution NAIP imagery, county parcel data, and point locations of irrigation meters.

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

## Analysis Workflow
* Open landscape-area-measurements.ipynb notebook
* Change directory to where data are stored
* Run notebook
