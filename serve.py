import http.server
import socketserver
import os
import mimetypes

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        # Cache textures for 7 days (they don't change)
        if self.path.startswith('/textures/') or self.path.startswith('/js/'):
            self.send_header('Cache-Control', 'public, max-age=604800')
        else:
            self.send_header('Cache-Control', 'no-cache')
        # Ensure correct MIME types
        ct = mimetypes.guess_type(self.path)[0]
        if ct:
            self.send_header('Content-Type', ct)
        super().end_headers()

    protocol_version = 'HTTP/1.1'

PORT = 8092
socketserver.TCPServer.allow_reuse_address = True
print(f"Serving on http://localhost:{PORT}")
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.serve_forever()
