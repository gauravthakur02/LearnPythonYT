# Using Variables to Store and Manipulate Configuration Data in a DevOps Context

'''
In a DevOps context, you often need to manage configuration data for various services or environments. Variables are essential for this purpose. Let's consider a scenario where we need to store and manipulate configuration data for a web server.
'''

# server details
server_name = "web-server"
port = 80
http_enabled = False
max_connections = 1000

# Print server details
print(f"Server Name: {server_name}")
print(f"Server Port: {port}")
print(f"HTTPS Enabled: {http_enabled}")
print(f"Max Connections: {max_connections}")

# update server configs
port = 443
http_enabled = True

# Print updated server details
print(f"Server Port: {port}")
print(f"HTTPS Enabled: {http_enabled}")
