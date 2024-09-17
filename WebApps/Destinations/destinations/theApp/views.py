from django.shortcuts import render, redirect
from .middleware import session_middleware
from .models import User, Session, Destination
from django.http import HttpRequest, HttpResponse
import string
import secrets
from  django.contrib.auth.hashers import make_password, check_password

# Create your views here.
# make sure you cant acess destinations 
# acess them from the currently logged in users destination set instead of just the destination id
# ONLY do user.destination instead of destination.objects
# except on the homepage
# for redirect use the path, for render use the html file name
# the destination already comes with the ID

def home(req):
    #need to know if the user is signed in or not to know which links to display
    destinations = Destination.objects.filter(share_publicly=True).order_by("-id")[:5]

    isSignedIn = False
    if req.user:
        isSignedIn = True

    return render(req, "theApp/home.html", {"destinations": destinations, "signedIn": isSignedIn})

def new_user(req):
    if req.method == "POST":
        return POSTUser(req)
    #this just renders the form page for the new user
    return render(req, "theApp/new_user.html/")
    
@session_middleware    
def new_session(req):
    if req.method == "POST":
        return POSTSessions(req)
    return render(req, "theApp/new_session.html/")
     
def POSTUser(req):
    # this endpoint is called when you submit the form from the new user page and processes the data before redirencting to destinations page
    #check that the email is valid
    if not "@" in req.POST.get("email"):
        return HttpResponse("Email is not valid", status=404)
    #check that password is at least 8 characters and has a number
    password = req.POST.get("password")
    passwordLst = list(password)
    if len(passwordLst) < 8:
        return HttpResponse("Password must be at least 8 characters long", status=404)
    
    digit = False
    for i in passwordLst:
        if i.isdigit():
            digit = True
            break
    if not digit:    
        return HttpResponse("Password must contain a number", status=404)
    # create user and send 400 error if it fails
    if req.method == "POST":
        params = req.POST
        #create new user
        user = User(
            name = params.get("name"),
            email = params.get("email"),
            password_hash = make_password(params.get("password")),
        )
        print(user.email)
        user.save()
        # create session
        token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(70))
        sessionObj = Session(
            token = token,
            user = user
        )
        sessionObj.save()
        #write session token to cookie
        res = redirect(f"/destinations/")
        res.set_cookie("token", token)
        # redirect to /destinations page
        return res

     
def POSTSessions(req):
    if req.method == "POST":
        #find user by email or return 404

        userEmails = []
        for user in User.objects.all():
            userEmails.append(user.email)
        email = req.POST.get("email")
        if email not in userEmails:
            return HttpResponse("User not found", status=404)
        
        # create new user object
        userObj = User.objects.get(email=email)
        # validate password
        password = req.POST.get("password")
        if not check_password(password, userObj.password_hash):
            return HttpResponse("Incorrect password", status=404)
        #create session and generate session token
        # create a new session object
        if not Session.objects.filter(user = userObj):
            token = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(70))
            sessionObj = Session(
                token = token,
                user = userObj
            )
            sessionObj.save()
        #write session token to cookie
        res = redirect(f"/destinations/")
        res.set_cookie("token", userObj.session.token)
        # redirect to /destinations page
        return res

def destroySession(req):
    #Destroys the current user's session and redirects them to the / page.
    req.user.session.delete()
    return redirect(f"/")

def destinations(req):
    #Renders all list of the currently logged-in user's destinations
    destinations = req.user.destination_set.all()
    return render(req, "theApp/destinations.html", {"destinations": destinations})

def new_destination(req):
    if req.method == "POST":
        return POSTdestinations(req)
    return render(req, "theApp/new_destination.html")

def POSTdestinations(req):
    # Accepts form data for a new destination. 
    # Creates the destination in the database. 
    if req.method == 'POST':
        destination = Destination(
            name = req.POST.get("name"),
            review = req.POST.get("review"),
            rating = req.POST.get("rating"),
            user = req.user,
            share_publicly = req.POST.get("share_publicly") == "on"
        )
        destination.save()  # Save the destination to the database
        return redirect('/destinations/')  # Redirect to a list view

def destination(req, id):
    # Renders a page with a form that is prepopulated with information for that 
    # destination that allows them to edit the destination information
    # submit a post to /destinations/:id
    #if dstination does not belong to user, return 404
    #also displays another form that only has a "delete" button that when pressed submits a post to the /destinations/:id/destroy endpoint
    destination = req.user.destination_set.get(id=id)
    if destination.user != req.user:
        return HttpResponse("Private destination", status=404) 
    
    if req.method == "POST":
        print(id)
        return POSTdestination(req, id)

    return render(req, 'theApp/destination.html', {'destination': destination})

def POSTdestination(req, id):
    # Accepts form data to update a destination specified by :id. 
    # If the user owns the destination, then perform the update and redirect to /destinations. 
    # you already know the user owns the destination from the endpoint 
    #get the destination by its id
    destination = req.user.destination_set.get(id=id)
    if req.method == "POST":
        #the id is given to you with the url and then the router calls this function for you
        #update the destination parameters with each given parameter you get from the request
        destination.name = req.POST.get("name")
        destination.review = req.POST.get("review")
        destination.rating = req.POST.get("rating")
        destination.share_publicly = req.POST.get("share_publicly") == "on"

        destination.save()

        return redirect('/destinations/') 
    

def destroyDestination(req, id):   
    # Deletes the destination specified by :id 
    # if the current user owns it and redirects to /destinations. 
    # If not, then responds with 404.
    #to get all destinations for the user: destinations = req.user.destination_set.all()
    # this gets all the destinations that only the user has acess to
    #to get one:
    try:
        destination = req.user.destination_set.get(id=id)
        destination.delete()
        return redirect('/destinations/') 
    except:
        return HttpResponse("Private destination", status=404) 
     
    