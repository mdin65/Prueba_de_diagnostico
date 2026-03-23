# Prueba_de_diagnostico

se tiene que elegir el commit de esta manera:
# Analyze single commit
Repository('path/to/the/repo', single='6411e3096dd2070438a17b225f44475136e54e3a').traverse_commits()

o sino hacerlo desde una fecha en especifico:
# Since 8/10/2016
Repository('path/to/the/repo', since=datetime(2016, 10, 8, 17, 0, 0)).traverse_commits()

ESTO FILTRA SI SON JAVA O PYTHON:

# Only commit that modified "Matricula.javax"
Repository('path/to/the/repo', filepath='Matricula.javax').traverse_commits()

# Only commits that modified a java file
Repository('path/to/the/repo', only_modifications_with_file_types=['.java']).traverse_commits()


## ---------------------------------------------------------------
## ---------------------------------------------------------------
## ---------------------------------------------------------------

mmm no use docker sino que hice un localserver en la carpeta en donde tenemos este python y el html con python -m http.server 8000 en el cmd
esto hace un json y despues lo sube en el html y lo deja bonito con una buena cantidad de ia o sino nose como hacerlo :PPP
