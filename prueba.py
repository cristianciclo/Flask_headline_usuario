from flask import Flask ,session, json ,request
from flask import render_template
from flask import request
from flask.ext.mysql import MySQL
import feedparser
app = Flask(__name__)

mysql = MySQL()
# Configuración de MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'prueba'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

#feeds de las noticias
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
CNN_FEED = "http://rss.cnn.com/rss/edition.rss"
FOX_FEED = "http://feeds.foxnews.com/foxnews/latest"
IOL_FEED = "http://www.iol.co.za/cmlink/1.640"


app.secret_key = 'clave'


#------------------REGISTRO-------------------------

@app.route('/')
def iniciar():
	return render_template('iniciar_secion.html')

@app.route('/crear_usuario')
def registrar():
	return render_template('registro.html')

@app.route("/inicio_secion", methods=['POST'])
def enter():
	# Leemos los parametros recibidos
	_email = request.form['email']
	_password = request.form['password']
	# Los validamos
	

	conn = mysql.connect()
	cursor = conn.cursor()

	#Creamos el query para insertar los datos
	insert = "select name from alumnos where email ='"+_email+"';"
	cursor.execute(insert)
	data=cursor.fetchone()
	if data is None:
		return "Usuario incorrecto"
	else:
		insert = "select name from alumnos where password ='"+_password+"';"
		cursor.execute(insert)
		data=cursor.fetchone()
		if data is None:
			return "Contraseña incorrecta" 
		else:
			insert = "select name from alumnos where email ='"+_email+"';"
			cursor.execute(insert)
			nombre=cursor.fetchone()


			session['nombre'] = nombre
			session['email'] = _email
			feed = feedparser.parse(BBC_FEED)
			feedn = feedparser.parse(CNN_FEED)
			feedf = feedparser.parse(FOX_FEED)
			feedi = feedparser.parse(IOL_FEED)
			return render_template("home.html", bbc=feed['entries'], cnn=feedn['entries'], fox=feedf['entries'], iol=feedi['entries'])
		
	#conn.commit()



@app.route("/registers", methods=['POST'])
def register():
	# Leemos los parametros recibidos
	_name = request.form['name']
	_email = request.form['email']
	_password = request.form['password']
	# Los validamos
	

	conn = mysql.connect()
	cursor = conn.cursor()

	#Creamos el query para insertar los datos
	insert = "insert into alumnos (name, email, password) values ('"+_name+"', '"+_email+"', '"+_password+"');"
	cursor.execute(insert)
	conn.commit()
	return render_template('iniciar_secion.html')

	

#Noticias
@app.route("/info")
def info():
  nombre = session['nombre']
  email = session['email']
  return render_template("info.html", nombre=nombre, email=email)

@app.route("/news")
def get_news():
	feed = feedparser.parse(BBC_FEED)
	feedn = feedparser.parse(CNN_FEED)
	feedf = feedparser.parse(FOX_FEED)
	feedi = feedparser.parse(IOL_FEED)
	return render_template("home.html", bbc=feed['entries'], cnn=feedn['entries'], fox=feedf['entries'], iol=feedi['entries'])

@app.route("/set_info")
def set_info():
  return render_template("set_info.html", nombre=session['nombre'], email=session['email'])

@app.route("/modificar")
def set():
  return render_template("set_name.html")

@app.route("/modificar/set_name" ,methods=['POST'])
def set_info_nombre():
  conn = mysql.connect()
  cursor = conn.cursor()
  name = request.form['name']
  old_name=request.form["old_name"]
  update = "update alumnos set name='"+name+"' where name='"+old_name+"';" 
  cursor.execute(update)
  conn.commit()
  session["nombre"] = name
  return render_template("set_info.html", nombre=session['nombre'], email=session['email'])

@app.route("/delete")
def delete():
  conn = mysql.connect()
  cursor = conn.cursor()
  delete = "delete from alumnos where email='"+session["email"]+"';" 
  cursor.execute(delete)
  conn.commit()
  return render_template("iniciar_secion.html")