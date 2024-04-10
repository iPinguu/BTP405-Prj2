from http.server import HTTPServer, BaseHTTPRequestHandler
from bson import json_util
import json
import requests

import services.authentication as authenLib 

PORTNUM = 8080

class RequestHandler(BaseHTTPRequestHandler):

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

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            form_userName = requests.inputForm[userName]
            form_userPwd = requests.inputForm[userPwd]
            
            
            if(authenLib.authenticateUser(form_userName, form_userPwd)):
                with open('./pages/reservation.html', 'rb') as file:
                    self.wfile.write(file.read())
    
    def do_POST(self):

        if self.path == "/register-user":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()


        
    

        


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