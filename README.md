# geojsonio
Tool to pass GeoJSON data from the UNIX standard input to the geojson.io

# installation
1. Check that you have python installed.
2. Clone this repo ```git clone https://github.com/gardster/geojsonio.git```
3. Add alias to your .bashrc file ```echo 'alias geojsonio="~/code/geojsonio/geojsonio.py"'```

# usage
```echo '{"type": "Feature","properties": {},"geometry": {"type": "LineString","coordinates": [[38,56],[28,54]]}}' | geojsonio```
Visualise data from a PostgreSQL
```psql -c "select ST_AsGeoJSON(ST_Transform(geom, 4326)) from geo_table limit 1;" | sed "3q;d" | geojsonio```
