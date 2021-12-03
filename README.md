# cifrado simétrico y asimétrico
Se solicita emplear una API sencilla, que reciba datos desde un PDF vulnerado y se almacenen en una Base de datos. Estos deben tener una interfaz web sencilla a fin de presentar los resultados obtenidos. Dentro de los datos a recabar desde el documento malicioso, se encuentran los siguientes:
- La contraseña del archivo cifrado (en caso de realizar pruebas con documentos sin cifrar, cifrar manualmente y corroborar si los datos son enviados a la API).
- La dirección IP de quien abre el PDF.
- El sistema operativo y su versión.
## Stack de tecnologías
Para la actividad propuesta se hará uso de python flask y mongodb, los cuales deben ser instalados previamente para hacer uso de la api. Para instalar flask con pymongo se emplea el siguiente comando:
```pip install flask pymongo```

## Script utilizado
