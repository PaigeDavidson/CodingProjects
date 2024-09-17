import socket
from request import Request
from response import Response
from encoder import encode, decode
from router import router
import middleware

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                connection.close()
                continue
            print(str(data, "utf-8"))
            #send data from server to encoder to turn from bytes to string request object
            request = decode(data)
            # put request though middleware here - you pass in your router object not the request
            middleware_chain = middleware.static_files_factory(router)
            middleware_chain = middleware.headers_middleware_factory(middleware_chain)
            middleware_chain = middleware.logging_middleware_factory(middleware_chain)

            #send request from middleware to router
            #in the router, it will send request to correct endoint and get a response
            response = middleware_chain(request)
            #the middleware_chain is your router now!
            #encode the reponse object back into a string so the server can send the bytes 
            responseText = encode(response)
            
            

            connection.send(bytes(responseText, "UTF-8"))

# to run server.py in terminal be in the SimpleHTTPServer folder and run python3 server.py 
# then go to a web browser like chrome and type in localhost:port# where the port# is typically 8000 
# but you can find it in the terminal if its different
