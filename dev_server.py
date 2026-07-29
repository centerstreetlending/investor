import http.server
import socketserver
import os

PORT = 8018

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If the path doesn't have an extension and isn't root, append .html
        if self.path != '/' and not '.' in self.path.split('/')[-1]:
            # Check if the .html file exists before appending, just in case
            if os.path.exists(self.translate_path(self.path + '.html')):
                self.path += '.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Allow port reuse so it restarts cleanly
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT, "with clean URL support")
    httpd.serve_forever()
