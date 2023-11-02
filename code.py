import subprocess
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))

def execute_python_script():
    try:
        subprocess.run(['python', 'code/main.py'], check=True)
        print("python complete")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error executing main.py: {e}")

def execute_mail_script():
    try:
        subprocess.run(['node', 'code/main.js'], check=True)
        print("Message sent")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error executing main.js: {e}")

def main():
    try:
        execute_python_script()
        execute_mail_script()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        # Uncomment the lines below if you want to run initialization and installation
        # initialize_project()
        # install_nodemailer()

        while True:
            main()
            print("code running")  # Added this line to indicate code is running
            time.sleep(60 * 15)  # Send email every 15 minutes

            # Start the HTTP server
            server = HTTPServer(('localhost', 8000), handler)
            print('Started HTTP server')
            server.serve_forever()
    except Exception as e:
        print(e)
