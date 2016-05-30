========================
Indicar Process
========================

A project to schedule and control the download and processing of Landsat 8 Imagery.


Features
=========

* Register Scenes and Image files in the database and provides a web interface to put them available to download.
* Register some 'path' and 'row' coordinates to download all the next Scenes of this coordinates.
* Download past Landsat 5, 7 and 8 Scenes from AWS or Google Earth Engine. It provides also a form to users request download of Scenes.
* Process Landsat imagery generating NDVI, change_detection and other composition.


Instructions
=============

You can remove catalogo and tmsapi folders. It is just a workaround to solve IBAMA issues.

System dependencies
-------------

Before start install, verify if all system dependencies are supplied, see below:

- libgdal-dev 1.10
- dans-gdal-scripts 0.23-2
- postgis 2.1.4

***UBUNTU***

- python-numpy 1.8.2


- Create a database, configure it in settings/local.py
- Install requirements
- Run migrations

You can too remove urls about sentinel_catalog app, because that's a specific solution to CSR/IBAMA requests


Configuration
==============

To use the not_found_scenes_alert task function configure the following variables in your settings:

    SERVER_EMAIL = 'sender@yourserver.com'
    NOT_FOUND_SCENES_ADMIN_EMAILS = ['destination@server.com']

Imagery
-------------
The bands to download of landsat satellite might be listed in DOWNLOAD_BANDS variable in settings file.
E.g.
DOWNLOAD_BANDS = [4, 5, 6, 'QBA']

Catalogo
-------------

To use the task to process TMS. you need to define the below settings:

LANDSAT_PATH_FORMAT = Format of path to TMS images
URL_TMS_BASE = URL to available TMS scene
PNG_IMAGES_PATH = Path to place PNG image files
TMS_IMAGES_PATH = Path to place TMS image files



    
