	PARCIAL 2 BIG DATA
-Alejandro Rodriguez
-Andress Arana
Funcionamiento del sistema distribuido.

Para el nodo lider.
1. Descargar ngrok y ejecutar seguido de http 5000
2.Ir a carpeta Server, ejecutar datos.py para descargar de internet el archivo covid mas reciente automaticamente, aparecerá ya descomprimido
3.Ejecutar un split en git bash para separar el archivo en n partes (xaa, xab, xac,..)
[split -b 500M <nombre del archivo.csv>]
4.Compartit los archivos separados por flask ejecutando server.py 

Para los otros nodos del cluster

1.Ir a carpeta user, ejecutar user.py para descargar archivo reducido
2.Cargar archivo a coleccion de mongo atlas
3.Editar processing.py para conectarse a mongo, ejecutarlo y revisar output con datos de salida.