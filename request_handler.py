import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from moods import get_all_moods, get_mood_by_id
from entries import get_all_entries, get_single_entry, delete_entry, get_entries_by_search, create_entry, update_entry
from tags import get_all_tags

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:
            # GIVEN: /entries?q=search_term

            param = resource.split("?")[1] # q=search_term
            resource = resource.split("?")[0] # 'entries
            pair = param.split("=") # [ 'q', 'search_term' ]
            key = pair[0] # 'q'
            value = pair[1] # 'search_term'

            return ( resource, key, value )

        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  
            except ValueError:
                pass  

            return (resource, id)  

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        response = {}

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            (resource, id) = parsed

            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"
                else:
                    response = f"{get_all_entries()}"
            
            elif resource == "moods":
                if id is not None:
                    response = get_mood_by_id(id)
                else:
                    response = get_all_moods()
            
            elif resource == "tags":
                response = get_all_tags()
        
        elif len(parsed) ==3:
            ( resource, key, value ) = parsed

            if key == "q" and resource == "entries":
                response = get_entries_by_search(value)

        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_item = None

        if resource == "entries":
            new_item = create_entry(post_body)

        self.wfile.write(f"{new_item}".encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        # Delete a single animal from the list
        if resource == "entries":
            success = update_entry(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
            
        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            delete_entry(id)

        self.wfile.write("".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()