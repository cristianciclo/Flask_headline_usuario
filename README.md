# Flask_headline_usuario
Primera estancia del proyecto Pythonn_Flask_Headline al cual he añadido una interfaz de usuario en la cual puedes registrarte, iniciar sección y modificar tu cuenta para poder acceder a las ultimas noticias de algunos periódicos-

## Requisitos:
Lo primero que necesitamos es tener un entorno virtual, en el caso de que no lo tengamos, lo instalaremos con 
<code>$ sudo apt-get install python3-venv</code>

Ahora nos crearemos un entorno virtual para trabajar con pip e instalar lo necesario
<code>$ python3 -m venv env</code>

Ya tenemos el entorno virtual, ahora lo iniciaremos con
<code>$ source env/bin/activate</code>

Y empezaremos a instalar:
<code>$ pip install flask</code> ---> Para el uso de Flask
<code>$ pip install feedparser</code> --->  Necesario para leer los RSS de las noticias

## Base de Datos MySql
Tendremos que crear una base de datos MySql donde almacenaremos los datos, asi que accedemos a nuestro MySql con
<code>mysql -u root -p</code>
Ahora creamos la base de datos prueba, en el caso de que cambiemos el nombre de la base de datos, tendremos que cambiarlo en el     codigo del proyecto
<code>create database prueba</code>
Nos cambiamos a la base de datos creada y creamos la tabla
<code>use prueba</code>
<code>CREATE TABLE alumnos (name VARCHAR(30), email VARCHAR(30), password VARCHAR(30));</code>

## Iniciar
Cuando lo tengamos todo, entraremos en la carpeta del proyecto y ejecutaremos 
<code>export FLASK_APP=prueba.py </code> --> para exportar la app de flask
<code>flask run</code> --> Para iniciar la aplicación


IMPORTATNTE
Comprobar vuestro usuario y contraseña y cambiarlo en el código del programa.

## Funcinamiento
Ya lo tenemos todo, ahora solo tendremos que entrar en el navegador a localhost:5000 y tendremos nuestra aplicación funcionando
Este programa hace uso de las sessiones para mantener los datos del usuario que ha iniciado session, base de datos para su almacenamiento, feedparser para los RSS
   Desde nuestra aplicacion, podremos crearnos un usuario e iniciar seccion con el.
   Cuando estemos dentro, podremos ver las ultimas noticias de los periodicos, acceder a nuestro perfil, modificar nuestro nombre, eliminar nuestra cuenta y cerrar seccion
   
   Para proximas versiones, se controlaras errores y la seguridad del programa, asi como a la hora de crear tu cuenta, te de la opción de elegir tu periodico de noticias preferidas para que sea lo primero que te aparezca al iniciar seccion.
   Tambien se añadira la posibilidad de guardar las noticias que te hayan llamado la atención.
