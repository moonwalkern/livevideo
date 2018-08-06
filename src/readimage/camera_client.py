import socket, time, argparse, sys
import picamera

# connect a client to a server (e.g. TNJ10038LKVTLSO.local:8000)

class CameraStreamer(object):

    def __init__(self, server, port):
        self.cli_socket = socket.socket()
        self.camera = picamera.PiCamera()
        self.server = server
        self.port = port

    def setup_camera(self, resolution = (1920,1080), fps = 30):
        self.camera.resolution = resolution
        self.camera.framerate = fps

    def connect_server(self):
        self.cli_socket.connect((self.server, self.port))
    
    def stream_video(self, length, format='h264', quality=100):
        connection = self.cli_socket.makefile('wb')
        try:
            self.camera.start_preview()
            time.sleep(3)
            self.camera.start_recording(connection, format=format)
            self.camera.wait_recording(length)
            self.camera.stop_recording()
        finally:
            self.camera.close()
            connection.close()
    
    def close_connection(self):
        self.cli_socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--server',type=str)
    parser.add_argument('-p', '--port', type=int)
    parser.add_argument('-l', '--length', type=int)
    args = parser.parse_args()
    server_name = 'TNJ10038LKVTLSO.local' \
                    if args.server == None \
                    else args.server
    port = 8080 if args.port == None \
            else args.port
    length = 3000 if args.length == None \
            else args.length
    print('Server: {}, Port: {}'.format(server_name, port))
    streamer = CameraStreamer(server_name, port)
    streamer.setup_camera()
    streamer.connect_server()
    streamer.stream_video(length=length)
    print('Finished Streaming After {0} Seconds'.format(length))
    

