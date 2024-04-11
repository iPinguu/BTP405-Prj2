from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

import services.authentication as authenLib 

PORTNUM = 8080

class RequestHandler(BaseHTTPRequestHandler):

    def reqData(reqData):
        content_length = int(reqData.headers['Content-Length'])
        body = reqData.rfile.read(content_length)
        data = json.loads(body.decode('utf-8'))
        
        reqData.name = data.get('name')
        reqData.email = data.get('email')
        reqData.password = data.get('password')
    
    
    def do_GET(self):
        
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('./pages/index.html', 'rb') as file:
                self.wfile.write(file.read())

        if self.path == "/register-user":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('./pages/register-user.html', 'rb') as file:
                self.wfile.write(file.read())
    
    def do_POST(self):
        if self.path == "/login-user":

            content_length = int(self.headers['Content-Length'])
            postData = self.rfile.read(content_length)
            formData = parse_qs(postData)

            name = formData.get('userName', [''])[0]
            passWord = formData.get('userPwd', [''])[0]

            try:
                
                if(authenLib.authenticateUser(name, passWord)):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    with open('./pages/reservation.html', 'rb') as file:
                        self.wfile.write(file.read())
                else:
                    print("not registered")
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    with open('./pages/index.html', 'rb') as file:
                        self.wfile.write(file.read())
            
            except Exception as e:
                print(e)



        
    

        


def run(serverClass=HTTPServer, handlerClass=RequestHandler, port = PORTNUM):
    serverAddress = ('localhost', port)
    httpd = HTTPServer(serverAddress, RequestHandler)
    print(f'[DEBUGGING]: Starting Server, running on Port: [{PORTNUM}]\n')
    httpd.serve_forever()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass 
    httpd.server_close()
    print('[DEBUGGING]: Server Has Stopped!')

if __name__ == '__main__':
    run()