#!/usr/bin/env python3
"""mindmap server — serve the mind map app with optional auto-load data."""

import http.server
import os
import sys
import shutil

PORT = 8765
DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    import socketserver

    # If a JSON file is provided, copy it as auto-load.json
    if len(sys.argv) > 1:
        src = sys.argv[1]
        dst = os.path.join(DIR, 'auto-load.json')
        shutil.copy(src, dst)
        print(f'[mindmap] Data: {src} -> auto-load.json')
    else:
        auto = os.path.join(DIR, 'auto-load.json')
        if os.path.exists(auto):
            os.remove(auto)

    os.chdir(DIR)

    # Try to bind, with SO_REUSEADDR
    class ReusableServer(socketserver.TCPServer):
        allow_reuse_address = True

    port = PORT
    while port < PORT + 100:
        try:
            server = ReusableServer(('localhost', port), http.server.SimpleHTTPRequestHandler)
            break
        except OSError:
            port += 1
    else:
        port = PORT

    url = f'http://localhost:{port}'
    print(f'[mindmap] {url}')
    sys.stdout.flush()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n[mindmap] Done.')
        server.shutdown()


if __name__ == '__main__':
    main()
