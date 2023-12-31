# Procesamiento y transferencia de datos
Ejercicios de prueba para NT, resumen de programas utilizados:
* IDE PyCharm 2023.1.1
* Python 3.11
* MySQL Community Edition

Estructura del proyecto:

<code>
├── data_prueba_tecnica.csv
├── main.py
├── README.md
├── requirements.txt
└── SCREENSHOTS
    ├── data_prueba_tecnica.csv
    ├── out.txt
    ├── pythonInterpreter.jpg
    ├── Untitled Diagram.drawio
    ├── Untitled Diagram.drawio.png
    └── Untitled Diagram.drawio.svg

</code>


## Descripción
El codigo toma datos del archivo "data_prueba_tecnica.csv" los limpia y crea un archivo nuevo "data_prueba_tecnica2.csv", ya con estos datos disponibles 
se conecta a MySQL, se crea una base de datos con el nombre "Test1", acto seguido se crean 2 tablas y se les insertan los datos limpios del archivo #2 CSV. Para finalizar
se crea una vista llamada "Transactions_Per_Day" la cual une las tablas "charges" y "companies". Por medio de un group by se juntan todas la fechas para poder crear
una tabla que nos muestre solo nombre de la compañia, el monto en un dia especifico y la fecha.

#### PyCharm
El codigo se escribio con IDE PyCharm, se instalaron algunas librerias las cuales se puden agregar desde la siguiente ventana 
![Screenshot](/Images/pythonInterpreter.jpg)

Accede a esta ventana desde File -> Settings -> Project (name) -> Python Interpreter.

Las librerias necesarias son:
* mysql-connector-python 8.0.33
* numpy 1.24.3
* pandas 2.0.2

###### Tambien se pueden instalar de manera manual con el archivo "Requirements.txt" si se requiere.

#### MySQL
Para instalar MySQL debes de ir a la url http://mysql.com/downloads
![Screenshot](/Images/mysqlComu.jpg)

Descargas "MySQL Community Edition" que es una versión gratuita, despues seleccionas "MySQL Installer for windows"
![Screenshot](/Images/mysqlComu2.jpg)

Das click y en la siguiente pagina seleccionas "Download" que es la primera opción que diga Windows(x86 x32bit), en la siguiente pagina selecciona 
"No thanks, just start my download"
![Screenshot](/Images/mysqlComu3.jpg)

Esperas la descarga.
Ya en el instalador la mayoria de los pasos es solo dar click en "Next", cuando llegues a esta ventana....
![Screenshot](/Images/mysqlComu4.jpg)

Debes de colocar un usuario y contraseña, guardalos porque los necesitaremos, y continua con next cuando llegues a la siguiente ventana ingresa tu contraseña
de nuevo y da click en check, despues execute y finish.
![Screenshot](/Images/mysqlComu5.jpg)

Ya terminada la instalación continuaremos con MySQLWorkbench, al abrir selecciona el icono de +(mas) y se abrira una ventana, si utilizaras el programa de 
manera local, solo agrega un nombre a la conexion que estas creando y presiona el boton "Store in Vault" te pedira tu contraseña, despues presiona el boton "ok" seguido
de  "Test Connection".
![Screenshot](/Images/mysqlComu6.jpg)

Aparecera una ventana que dice "Successfully made the MySQL connection" anota los datos que aparecen porque los necesitaras para poder editarlos dentro del programa, los
datos probablemente sean parecidos a los siguientes (tu contraseña es la que guardaste en los pasos anteriores).
host="192.168.0.201"
user="root"
password="Tu contraseña"
En el codigo del programa es aqui donde debes modificar tus datos:
![Screenshot](/Images/datosMySQL.jpg)

## Diagrama
Diagrama resultado de la separacion de los datos, se crearon 2 tablas (companies, charges). Tienen una relación one to many, como se muestra en el diagrama.

![Screenshot](/Images/Diagram.jpg)

## Comentarios

La parte mas interesante de este ejercicio fue utilizar pandas para realizar la limpieza de los datos, por ejemplo algunos datos eran mas grandes que 24 
caracteres que se habian configurado, otros tenian letras en los costos lo cual impedia poder cargar los valores a las tablas ya que solo permite datos numericos.
Un reto interesante fue darme cuenta que al crear la tabla "companies" las FK (Foreign Keys) que eran las "company_id" para una misma empresa variaban (por ejemplo no
la contenian estaba vacia ó tenian caracteres incorrectos) lo que llevo a que las limpiara con pandas, fue un interesante ver como pequeños detalles cuentan y mucho.
Otra experiencia importante fue crear la conexion a la base de datos y darme cuenta que se debia de crear una base de datos nueva, seleccionarla para su uso
y despues ahí crear y cargar los datos de las tablas, ademas que utilice varios conceptos de bases de datos, SQL y python todo en un solo ejercicio. El principal motivo
por el cual utilice MySQL es poque lo he utilizado en el pasado y tengo una idea de las herramientas que utiliza (MySQLWorkbench), ademas que los puedo utilizar tanto en
windows como en sistemas Unix.
La base de datos que utilice no estaba en mi "localhost", era una computadora en la red local de mi casa por lo que tuve que configurar la ip a estatica y alguna que otra
configuracion de red relacionada.

## Para finalizar
El codigo se probo, se llego a cargar los 9996 registros en la base de datos
![Screenshot](/Images/FIN1.jpg)
Se verificaron las tablas con MySQLWorkbench

Tabla "companies"
![Screenshot](/Images/FIN2.jpg)
Tabla "charges"
![Screenshot](/Images/FIN3.jpg)
Finalmente la vista "Transactions_Per_Day"
![Screenshot](/Images/FIN4.jpg)
