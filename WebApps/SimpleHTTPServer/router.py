from response import Response
from datetime import datetime

#router - calls one of the endpoints down below based on the request
# returns a file not found error if the request doesnt match any endpoints
def router(req):
    if req.uri == "/":
        return home(req)
    elif req.uri == "/about":
        return about(req)
    elif req.uri == "/projects":
        return projects(req)
    elif req.uri == "/expirience":
        return expirience(req) 
    elif req.uri == "/info":
        return info(req)
    else:
        return Response("HTTP/1.1", 404, "not found", {
            "Content-Type": "text/html",
            "Content-Length": 14,
            "Server": "MyServer",
            "Date": datetime.now(),
            "Connection": "close",
            "Cache-Control": "no-cache"
        }, "file not found")

#endpoints - each endpoint is its own function
# make sure to close all files
def home(req):
   f = open("templates/index.html") 
   text = f.read()
   f.close()
   return Response("HTTP/1.1", 200, "ok", {
        "Content-Type": "text/html",
        "Content-Length": len(text),
        "Server": "MyServer",
        "Date": datetime.now(),
        "Connection": "close",
        "Cache-Control": "no-cache"
   }, text) #each response needs a comma text at the end even if it is an empty string

def about(req):
   f = open("templates/about.html") 
   text = f.read()
   f.close()
   return Response("HTTP/1.1", 200, "ok", {
        "Content-Type": "text/html",
        "Content-Length": len(text),
        "Server": "MyServer",
        "Date": datetime.now(),
        "Connection": "close",
        "Cache-Control": "no-cache"
   }, text)

def projects(req):
   f = open("templates/projects.html") 
   text = f.read()
   f.close()
   return Response("HTTP/1.1", 200, "ok", {
        "Content-Type": "text/html",
        "Content-Length": len(text),
        "Server": "MyServer",
        "Date": datetime.now(),
        "Connection": "close",
        "Cache-Control": "no-cache"
   }, text)

def expirience(req):
   f = open("templates/expirience.html") 
   text = f.read()
   f.close()
   return Response("HTTP/1.1", 200, "ok", {
        "Content-Type": "text/html",
        "Content-Length": len(text),
        "Server": "MyServer",
        "Date": datetime.now(),
        "Connection": "close",
        "Cache-Control": "no-cache"
   }, text)

# the /info endpoint is different where it uses the 301 location and other stuff, everything else is the same
# get to this endpoint by just typing it into the browser search bar ex: localhost:\\8000\info

def info(req):
   return Response("HTTP/1.1", 301, "Moved Permanetly", {
        "Server": "MyServer",
        "Date": datetime.now(),
        "Connection": "close",
        "Cache-Control": "no-cache",
        "Location": "/about"
   }, "")

    