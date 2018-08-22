from __future__ import unicode_literals
# from dateutil.relativedelta import relativedelta
from models import *
from datetime import datetime
from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
	def registration_validator(self, postData):
		print "CHECKPOINT: registration_validator - MODELS.PY"

		NAME_REGEX  = re.compile(r'^[A-Za-z ]*$')
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
		results = {
			'status' : True
		}
		errors = []

		# Name
		if len(postData['firstname']) < 2:
			errors.append("Name must be at least 3 characters in length.")
		if not re.match(NAME_REGEX, postData['firstname']):
			errors.append("Name may only only contain alphabtical characters.")	

		if len(postData['lastname']) < 2:
			errors.append("Name must be at least 3 characters in length.")
		if not re.match(NAME_REGEX, postData['lastname']):
			errors.append("Name may only only contain alphabtical characters.")	

		if len(postData['alias']) < 3:
			errors.append("alias must be at least 3 characters in length.")


		# password validation
		if len(postData["password"]) < 8:
			errors.append("password must be at least 8 characters long")

		if postData['password'] != postData['confirmpw']:
			errors.append("passwords must match!")

		#if datetime.strptime(postData["birthday"], '%Y-%m-%d') > datetime.now() - relativedelta(years=13):
			#errors.append("Sorry, you must be at least 13 years of age to register.")	

		if len(errors) > 0:
			results['status'] = False
			results['errors'] = errors
		else:
			hashedpw = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))
			user = User.objects.create(firstname=postData['firstname'], lastname=postData['lastname'], email=postData['email'], alias = postData['alias'],password = hashedpw)
			results['user'] = user


		return results

	def login_validator(self, postData):
		results = {
			'status' : True
		}
		errors = []
		hashedpw = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))

		user = User.objects.filter(email = postData['email'])

		if len(user) > 0:
			# Check this user's password
			user = user[0]
			if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
				errors.append("Sorry, your alias/password incorrect")
		else:
			errors.append('Sorry pal, please register.')

		if len(errors) > 0:
			results['status'] = False
			results['errors'] = errors
		else:
			results['user'] = user
		return results				

class ActivityManager(models.Manager):
	def Activity_Validator(self, postData):
		pass
		# '''		results = {
		# 	'status':True
		# }
		# errors = []
		# if len(postData['destination']) < 2:
		# 	errors.append("You have entered an invalid destination")
		# if len(postData['description']) < 2:
		# 	errors.append("Your description is invalid.")		

		# current_date = datetime.now()
		# formatted_date = current_date.strftime('%Y-%m-%d')

		# if postData['startdatetime'] < formatted_date:
		# 	errors.append('You cant be departing from the past, that is impoossible')

		# if postData['departure_end_date'] < postData['departure_start_date']:
		# 	errors.append("Your departure end dat cant come before your departure start date.")

		# if len(errors) > 0:
		# 	results['status'] = False
		# 	results['errors'] = errors
		# 	print "Sorry there were errors"
		# else:
		# 	print "CHECKPOINT: Congradulations, You have successfully created a new Activity"
		# 	this_member = Member.objects.get(id=postData['member_id'])
		# 	print "this_member name", this_member.name	'''	

# Models
class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=222)
    alias = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Activity(models.Model):
	title = models.CharField(max_length=222)
	description = models.CharField(max_length=1000)
	participant = models.ManyToManyField(User, related_name="participant")
	coordinator = models.ForeignKey(User, related_name="coordinator") 
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True) 
	startdatetime = models.DateTimeField()
	enddatetime = models.DateTimeField()  
	objects = ActivityManager()

