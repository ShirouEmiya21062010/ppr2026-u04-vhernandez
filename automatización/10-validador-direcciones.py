import ipaddress 
dispositivos=[
  {"nombre":"Router H121","ip":"192.168.1.1"},
    {"nombre":"Router M203","ip":"192.168.1.10"},
    {"nombre":"Servidor Edif B","ip":"192.168.3.1"},
    {"nombre":"PC RVILLEGAs","ip":"192.168.2.1"},
    {"nombre":"PC G21","ip":"192.168.1.300"},
    {"nombre":"Router Rectoría","ip":"192.168.1.10"},
    {"nombre":"Switch Piso 1","ip":"10.0.0.25"},
    {"nombre":"Impresora Adm","ip":"192.168.1.999"},
    {"nombre":"Laptop Lab 3","ip":"192.168.2.1"},
    {"nombre":"Servidor Backup","ip":"172.16.254.1"},
    {"nombre":"Camara IP 01","ip":"192.168.1.1"},
    {"nombre":"AP Biblioteca","ip":"192.168.5.50"},
    {"nombre":"Terminal POS","ip":"192.168.300.45"},
    {"nombre":"Smart TV Sala","ip":"10.0.0.25"},
    {"nombre":"PC Recepción","ip":"192.168.1.50"},
    {"nombre":"Router Bodega","ip":"192.168.4.256"},
    {"nombre":"Servidor Web","ip":"192.168.3.1"},
    {"nombre":"Firewall Edge","ip":"192.168.100.1"},
    {"nombre":"Tablet Auditorio","ip":"192.168.0.500"},
    {"nombre":"NAS Principal","ip":"192.168.1.50"},
]

ips_registradas=[]
ips_validas=0
ips_no_validas=0
ips_duplicadas=0
for dispositivo in dispositivos:
    ip=dispositivo["ip"]
    nombre=dispositivo["nombre"]

    #Mannejo de excepciones
    try: 
        ipaddress.ip_address(ip)

        if ip in ips_registradas:
            print(nombre, "-", ip, "DIRECCIÓN DUPLICADA")
            ips_duplicadas+=1
        else:
            print(nombre,"_", ip, "DIRECCIÓN VALIDA")
            ips_registradas.append(ip)
            ips_validas+=1
    except ValueError:
        print(nombre,"-",ip, "DIRECCIÓN IP NO VALIDA")
        ips_no_validas+=1

print("="*50)
print("Total de direcciones validas: ", ips_validas)
print("Total de direcciones no validas: ", ips_no_validas)
print("Total de direcciones duplicadas: ", ips_duplicadas)