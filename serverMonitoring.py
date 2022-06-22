import socket
import ssl
from datetime import datetime
import pickle
import subprocess
import platform


class Server():
    def __init__(self,name,port,connection,priority):
        self.name = name
        self.port = port
        self.connection = connection.lower()
        self.priority = priority.lower()

        self.history = []
        self.alert = False

    def check_connection(self):
        msg = ""
        sucess = False
        now = datetime.now()
        try:
            if self.connection == "plain":
                socket.create_connection((self.name,self.port), timeout=10)
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                sucess = True
                self.alert = False
            elif self.connection == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name,self.port), timeout=10))
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                sucess = True
                self.alert = False
            else:
                if self.ping():
                    msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                    sucess = True
                    self.alert = False
        except socket.timeout:
            msg = f"server {self.name} timeout. On port {self.port}"
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = f"server:{self.name} {e}"
        except Exception as e:
            msg = f"No Clue??: {e}"

        self.create_history(msg,sucess,now) 
    
    def create_history(self,msg,sucess,now):
        history_max = 100
        self.history.append((msg,sucess,now))

        while len(self.history) > history_max:
            self.history.pop(0)
    def ping(self):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "Windows" 
            else 'c', self.name), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
            return False


def check_server():
    servers = pickle.load( open( "servers.pickle", "rb" ) )

    print("Example to add server")
    domain_name = "staging.purpledove.net"

    servername = domain_name
    port = 80
    connection = ("plain")
    priority = ("high")


    new_server = Server(servername, port, connection, priority)
    servers.append(new_server)

    pickle.dump(servers, open("servers.pickle", "wb" ))

if __name__ == "__main__":
    server_name = "purpledove.net"
    for server_names in server_name:
        if server_names:
            server_names.check_connection()
            print(len(server_names.history))
    # try:
    #     servers = pickle.load(open("servers.pickle", "rb"))
    # except:
    #     servers = [ 
    #         Server("purpledove.net", 80, "plain", "high")
    #     ]

    # for server in servers:
    #     server.check_connection()
    #     print(len(server.history))
    #     print(server.history[-1])

    pickle.dump(server_names, open("servers.pickle", "wb"))