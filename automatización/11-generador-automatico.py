from pathlib import Path 

dispositivos=[
    {
        "nombre":"Router-01",
        "interfaz":"G0/0",
        "ip":"192.168.1.1",
        "mask":"255.255.255.0",
        "line console 0": "pass cisco" ,
        "line vty 0 4": "pass cisco"

    },
    {
        "nombre":"Router-02",
        "interfaz":"G0/0",
        "ip":"192.168.1.1",
        "mask":"255.255.255.0",
        "line console 0": "pass cisco" ,
        "line vty 0 4": "pass cisco",
        "no ip domain-lookup": "no ip domain-lookup",
        "acl": "access-list 1 permit 192.168.1.20"
        
    }
]

#CREAR LA CARPETA CON LOS ARCHIVOS DE CONFIG

carpeta=Path("Configuraciones")
carpeta.mkdir(exist_ok=True)

#generar las config

for dispositivo in dispositivos:
    configuraciones=f'''
    hostname {dispositivo["nombre"]}

    interface {dispositivo["interfaz"]}
    ip address {dispositivo["ip"]} {dispositivo["mask"]}
    no shut

    end

    copy r st

    '''
    archivo=carpeta/f'{dispositivo["nombre"]}.txt'
    archivo.write_text(configuraciones)
