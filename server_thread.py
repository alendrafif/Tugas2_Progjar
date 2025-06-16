from socket import socket, AF_INET, SOCK_STREAM
import threading
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.keep_running = True

    def run(self):
        logging.info(f"Client connected from {self.address}")
        try:
            while self.keep_running:
                data = self.connection.recv(1024)
                if not data:
                    break

                request = data.decode('utf-8').strip()

                if request == "TIME":
                    now = datetime.now().strftime("%H:%M:%S")
                    response = f"JAM {now}\r\n"
                    self.connection.sendall(response.encode('utf-8'))

                elif request == "QUIT":
                    logging.info(f"Client {self.address} sent QUIT")
                    break

                else:
                    response = "UNKNOWN COMMAND\r\n"
                    self.connection.sendall(response.encode('utf-8'))

        except Exception as e:
            logging.error(f"Error with client {self.address}: {e}")
        finally:
            self.connection.close()
            logging.info(f"Connection closed for {self.address}")


class TimeServer(threading.Thread):
    def __init__(self, host='0.0.0.0', port=45000):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.clients = []

    def run(self):
        with socket(AF_INET, SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            logging.info(f"Time server running on {self.host}:{self.port}")

            while True:
                conn, addr = server_socket.accept()
                client_thread = ProcessTheClient(conn, addr)
                client_thread.start()
                self.clients.append(client_thread)


if __name__ == "__main__":
    server = TimeServer()
    server.start()
