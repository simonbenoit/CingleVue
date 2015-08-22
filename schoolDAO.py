import string

class SchoolDAO(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.schools = database.schools

#This function find the details of the school
	def find_names(self):
		l = []
		for each_name in self.schools.find():
			l.append({'name':each_name['name'], 'email':each_name['email'], 'telephone':each_name['telephone']})

		return l

#This function will handle the insertion of school
	def insert_school(self,newname,newemail,newtelephone):
		newname = {'name':newname,'email':newemail, 'telephone':newtelephone}
		self.schools.insert(newname)

#This function will handle the deletion of school
	def delete_shool (self, name):
		name = {'name':name}
		self.schools.remove(name)

#This function will handle the editing of school
	def edit_school (self, name, uemail, utelephone):
		update = {'name':name, 'email':uemail, 'telephone':utelephone}
		self.schools.update(update)

