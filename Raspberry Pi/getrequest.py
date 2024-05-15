from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        
        
        if self.path == "/led?=on":
            GPIO.output(40, GPIO.LOW)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(u'LED allume'.encode('utf-8'))
        elif self.path == "/led?=off":
            GPIO.output(40, GPIO.HIGH)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(u'LED eteinte'.encode('utf-8'))
        elif self.path == "/fall?=1":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(u'Chute detecte'.encode('utf-8'))
                
                
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(u'page non trouvé'.encode('utf-8'))

def send(url):
    try:
        response = urllib.request.urlopen(url)
        print("Requete envoyé avec succès ! \nRequete : " + url)
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(e)



def run_serveur():
    print("Demarage du serveur...")
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Serveur demarré sur le port 8000')
    httpd.serve_forever()

#run_serveur()