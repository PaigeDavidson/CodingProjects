from response import Response
import datetime

def logging_middleware_factory(next):
    def logging_middleware(req):
        print(f"{req.method} {req.uri}")
        response = next(req)
        print(f"{req.uri} {response.code} {response.reason}")
        return response

    return logging_middleware

def headers_middleware_factory(next):
    def headers_middleware(req):
        response = next(req)
        response.headers["Content-Length"] = len(response.text)
        response.headers["Server"] = "My Mock Server"
        response.headers["Connection"] = "close"
        return response

    return headers_middleware

def static_files_factory(next):
    def static_files(req):
        if not "." in req.uri:
            return next(req)
        else:
            uri = req.uri.split(".")
            fileType = uri.pop(1)
            f = open("static/" + req.uri)
            static_files = f.read()
            f.close()
            #make a dictionary so even though you have different file types in the static folder the content-type is still correct
            contentTypes = {"js": "text/javascript", "css": "text/css"}
            return Response("HTTP/1.1", 200, "ok", {
                "Content-Type": contentTypes[fileType],
                "Content-Length": len(static_files),
                "Server": "MyServer",
                "Date": datetime.datetime.now(),
                "Connection": "close",
                "Cache-Control": "no-cache"
        }, static_files)
        
    return static_files


