import pickle
from serverMonitoring import Server

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