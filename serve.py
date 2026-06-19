import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        # NO CACHING - force browser to always reload
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    protocol_version = 'HTTP/1.1'

PORT = 8092
socketserver.TCPServer.allow_reuse_address = True
print(f"Serving on {PORT}")
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as h:
    h.serve_forever()
