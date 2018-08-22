from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def landing (request):
	return render(request, 'landing.html')

def register(request):
	print "CHECKPOINT: def register - views.py"
	results = User.objects.registration_validator(request.POST)

	if (results['status']):
		request.session['errors'] = []
		request.session['firstname'] = results['user'].firstname
		request.session['user_id'] = results["user"].id
		print 'CHECKPOINT: Successful register. You are now leaving your login app, and now entering your dashboard.'
		return redirect('/home')
	else:
		for error in results['errors']:
			messages.error(request, error)
		print "ERROR MESSAGE: Unsuccessful register attempt. Try again."	
		return render(request, "landing.html")

def login(request):
	print "CHECKPOINT: def login - views.py"
	results = User.objects.login_validator(request.POST)

	if (results['status']):
		request.session['errors'] = []
		request.session['firstname']    = results['user'].firstname
		request.session['user_id'] = results['user'].id
		print 'CHECKPOINT: Successful login.' 
		print 'Now leaving login and entering the dashboard.'
		return redirect('/home')
	else:
		for error in results['errors']:
			messages.error(request, error)
		print "ERROR MESSAGE: Unsuccessful login attempt. Try again."	
		return render(request, "landing.html")		


def dashboard (request):
	me = User.objects.get(id=request.session['user_id'])
	all_activities = Activity.objects.all().order_by('startdatetime')
	My_activities = Activity.objects.filter(participant=me)
	context = {
		'all_activities': all_activities,
		'My_activities': My_activities,
		'me': me

	}
	return render(request,'Dash.html', context)	

def logout(request):
	request.session.flush()
	return redirect('/')

def FestivalAdderPage(request):
	return render(request, 'FestivalAdderPage.html')	

'''def CreateActivityProcessor(request):
	#results = Activity.objects.registration_validator(request.POST)	
	activity = Activity.objects.create(
		title = request.POST['title'], 
		description =request.POST['description'], 
		startdatetime =request.POST['startdatetime'], 
		enddatetime = request.POST['enddatetime'], 
		coordinator = User.objects.get(id=request.session['user_id']))
	activity.save()

	return render(request, 'ActivityPage.html')	'''

def CreateActivityProcessor(request):	
	activity = Activity.objects.create(
		title = request.POST['title'], 
		description =request.POST['description'], 
		startdatetime =request.POST['startdatetime'], 
		enddatetime = request.POST['enddatetime'], 
		coordinator = User.objects.get(id=request.session['user_id']))
	activity.save()

	return render(request, 'ActivityPage.html')

def ActivityInfoPage(request, id):
	me = User.objects.get(id=request.session['user_id'])
	activity_info = Activity.objects.get(id=id)	
	#participants = Activity.objects.get(id=id)
	context = {
		'activity_info': activity_info
	}
	return render(request, 'ActivityPage.html', context)

def delete(request, id):
	u = User.objects.get(id=request.session['user_id'])	
	A = Activity.objects.get(id=id).delete()
	return redirect('/home')

def Join(request, id):
	u = User.objects.get(id=request.session['user_id'])
	A = Activity.objects.get(id=id)
	A.participant.add(u)
	return redirect('/home')

def Leave(request, id):
	u = User.objects.get(id=request.session['user_id'])
	A = Activity.objects.get(id=id)
	A.participant.remove(u)
	return redirect('/home')				
