from http.server import BaseHTTPRequestHandler, HTTPServer
import json
# import helper

hostName = "localhost"
serverPort = 3000

sessions = {}

class MyServer(BaseHTTPRequestHandler):
    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.send_headers()
        
    def do_GET(self):
        # data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        if self.path == '/get_companies':
            # companies = helper.get_companies()
            data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
            print(data, "what the hell")
            self.send_response(200)
            self.send_headers()
            self.wfile.write(json.dumps({'companies': "Hello"}).encode('utf-8'))
        else:
            self.handle_error('request not recognised')
    
    def do_POST(self):
        # data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        print(self.rfile.read(int(self.headers['Content-Length'])))
        if self.path == '/retrieve_documents_from_query':
            self.send_response(200)
            self.send_headers()
            self.wfile.write(json.dumps({'companies': "Hello"}).encode('utf-8'))
            # number_of_records = 10
            # if data['number_of_records']:
            #     number_of_records = data['number_of_records']
            # page_no = 1
            # if data['page_no']:
            #     page_no = data['page_no']
            # documents = helper.retrieve_documents_from_query(data['query'], number_of_records, page_no)
            # self.send_response(200)
            # self.send_headers()
            # self.wfile.write(json.dumps({'query': data['query'], 'documents': documents}).encode('utf-8'))
        elif self.path == '/get_summary':
            summary = helper.get_summary(data['doc_id'], data['item_no'])
            self.send_response(200)
            self.send_headers()
            self.wfile.write(json.dumps({'doc_id': data['doc_id'], 'item_no': data['item_no'], 'summary': summary}).encode('utf-8'))
        else:
            handle_error('request not recognised')
            

    def handle_error(self, error):
            self.send_response(400)
            self.send_headers()
            self.wfile.write(('Error: ' + error).encode('utf-8'))  

    def send_headers(self):
            print('sending headers')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.send_header('Access-Control-Allow-Methods', '*')
            self.send_header("Content-Type", "application/json")
            self.end_headers()



if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")