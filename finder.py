import socket

nombre_equipo = socket.gethostname()
print("El nombre del equipos es: ", nombre_equipo)

ip_equipo = socket.gethostbyname(nombre_equipo)
print("La direccion IP es: ", ip_equipo)
