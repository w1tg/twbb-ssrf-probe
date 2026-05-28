import http.server, socketserver, os
PORT=int(os.environ.get("PORT","8080"))
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try: data=open("/resp.txt","rb").read()[:3000]
        except Exception as e: data=b"no resp file "+str(e).encode()
        self.send_response(200); self.send_header("Content-Type","text/plain"); self.end_headers(); self.wfile.write(data)
    def log_message(self,*a): pass
socketserver.TCPServer(("",PORT),H).serve_forever()
