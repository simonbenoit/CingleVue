import bottle
import pymongo
import schoolDAO

#This is the default route
@bottle.route('/')
def school_index():
	schools_list = school.find_names()
	return bottle.template('index', dict(schools = schools_list))

#This is the route for insertion
@bottle.route('/newschool', method='POST')
def insert_newschool():
	name = bottle.request.forms.get("name")
	email = bottle.request.forms.get("email")
	telephone = bottle.request.forms.get("telephone")
	school.insert_school(name,email,telephone)
	bottle.redirect('/')

#This is the route for deletion
@bottle.route('/deleteschool', method='delete')
def delete_school():
	school.delete_school()
	bottle.redirect('/')

#This is the route for updating
@bottle.route('/editschool', method='PUT')
def edit_school():
	name = bottle.request.forms.get("name")
	uemail = bottle.request.forms.get("uemail")
	utelephone = bottle.request.forms.get("utelephone")
	school.edit_school(name, uemail, utelephone)
	bottle.redirect('/')

#This is to setup the connection

#First, setup a connection string. My server is running on this computer so localhost is OK
connection_string = "mongodb://localhost"
#Next, let PyMongo know about the MongoDB connection we want to use.  PyMongo will manage the connection pool
connection = pymongo.MongoClient(connection_string)
#Now we want to set a context to the names database we created using the mongo interactive shell
database = connection.schools
#Finally, let out data access object class we built which acts as our data layer know about this
school = schoolDAO.SchoolDAO(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082) 