#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import random
import re

class RandomImageHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # If requesting root, show random image page
        if self.path == '/':
            images = [f for f in os.listdir('.')
                      if re.match(r'.*\.(jpe?g|png|gif|webp)$', f, re.I)]

            if not images:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"No images found")
                return

            img = random.choice(images)

            html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>UwU</title>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }}
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            background: #000;
        }}
        img {{
            max-width: 100vw;
            max-height: 100vh;
            object-fit: contain;
        }}
    </style>
</head>
<body>
    <img src="/{img}" alt="Boykisser">
</body>
</html>'''
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Cache-Control', 'public, max-age=604800')
            self.end_headers()
            self.wfile.write(html.encode())
        else:
            # For all other paths, serve files normally (images, etc.)
            super().do_GET()

os.chdir('/srv/images')
HTTPServer(('0.0.0.0', 6969), RandomImageHandler).serve_forever()
