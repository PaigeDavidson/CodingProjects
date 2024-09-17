from django.http import HttpRequest
from .models import Session
from django.shortcuts import render, redirect

def session_middleware(next):

    def middleware(req: HttpRequest):
        # Read the session_token out of the cookie
        session_token = req.COOKIES.get("token", 0)
        # Find the session by its token
        acessibleEndpoints = ["/users/new/", "/", "/sessions/new/"]
        try:
            session = Session.objects.get(token=session_token)
            req.user = session.user
        except:
            req.user = None
            if req.path not in acessibleEndpoints:
                return redirect(f"/sessions/new/")
        # If no session is found then skip to step 4
        # Get the user from the session and attach it to the request.
        # If URI maps to an endpoint requires a user to be logged in and there is no session, redirect them to the /sessions/new page
        # Otherwise, call the next middleware and return the result.

        #now you dont have to worry about the user being logged in in any of your endpoints
        # if the user tries to go to any of the not acessible endpoints, they will be directed to the login page
        #so you know if the user is on a destintions page it should belong to them

        res = next(req)
        return res

    return middleware
