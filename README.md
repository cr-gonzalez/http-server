# http-server

This module runs an http server compatible with both python 2 and python 3.
It takes an argument from the command line using 'python3 client.py "message"',
sends it to the server, prints it on the server and sends it back with either
a 'HTTP/1.1 200 OK' message saying it was a success, or a 'HTTP/1.1 500 
Internal Server Error' message if something broke.