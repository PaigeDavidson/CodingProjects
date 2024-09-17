from request import Request

#turn the object into a string
def encode(responseObj):
    headerStr = ""
    for i in responseObj.headers:
        headerStr += f"{i}: {responseObj.headers[i]}\n"
    return f"{responseObj.version} {responseObj.code} {responseObj.reason}\n{headerStr}\n{responseObj.text}"

#bytes to string and request object - this is where you use your request class to make a request object
def decode(requestBytes):
    requestString = str(requestBytes, "utf-8")
    lines = requestString.split("\n")
    firstLine = lines.pop(0)
    method,uri,version = firstLine.split(" ")
    headDict = {} 
    for i in lines:
        if i == "\r":
            break
        headerName, headerValue = i.split(": ") 
        headDict[headerName] = headerValue

    #making the request object
    return Request(method, uri, version, headDict, "")