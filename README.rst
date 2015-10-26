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

* Create a database, configure it in settings/local.py
* Install requirements
* Run migrations
