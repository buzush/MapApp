# mapapp

System Requirements
===================
* Postgres and PostGIS
  * Windows: Use the GUI Installer
  * Ubuntu14.04: `postgresql`, `postgis`,`postgresql-9.3-postgis-2.1`
* For windows - Install [OSGeo4w](http://trac.osgeo.org/osgeo4w/) - choose advanced option, search for GDAL and mark the `gdal` library option

Project Installation
====================
1. Clone the repo.
2. Switch / create virtualenv.
3. pip install -r requirements.txt
4. run from mapapp/: python manage.py runserver
