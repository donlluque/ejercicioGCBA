# ejercicioGCBA
Prueba tecnica entrevista para GCBA

Se requiere desarrollar una API RESTful utilizando Python (3.9.7) y Flask (2.2.2), que permita realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una base de datos PostgreSQL (13.7+) con PostGIS (3.2.2). La base de datos contiene información geoespacial de las estaciones meteorológicas de una región.

La API debe ser capaz de realizar las siguientes operaciones:

1. Crear una nueva estación meteorológica, proporcionando su ubicación geoespacial (latitud y longitud) y otros datos como el nombre, la altitud y la fecha de instalación.
2. Obtener una lista de todas las estaciones meteorológicas almacenadas en la base de datos.
3. Obtener los datos de una estación meteorológica específica, proporcionando su identificador único.
4. Actualizar los datos de una estación meteorológica existente, proporcionando su identificador único y los nuevos datos a actualizar.
5. Eliminar una estación meteorológica existente, proporcionando su identificador único.
Se anexan los scripts de SQL de DDL y de carga de datos.
