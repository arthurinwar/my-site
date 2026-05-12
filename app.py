from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg2

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            conn = psycopg2.connect(
                host="db",
                database="mydb",
                user="admin",
                password="secret"
            )
            cur = conn.cursor()
            cur.execute("SELECT username, email FROM users;")
            rows = cur.fetchall()
            
            html = "<html><body><h1>Users from DB:</h1><ul>"
            for row in rows:
                html += f"<li>{row[0]} - {row[1]}</li>"
            html += "</ul></body></html>"
            
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
            
            cur.close()
            conn.close()
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), MyHandler)
    print("Starting server on port 5000...")
    server.serve_forever()
