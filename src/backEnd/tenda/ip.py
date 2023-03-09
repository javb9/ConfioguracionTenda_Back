import subprocess
def obtenerPuertaEnlace():
    p = subprocess.run('netsh interface ipv4 show address Wi-Fi',
                    stdout=subprocess.PIPE,
                    shell = True,
                    universal_newlines = True,
                    encoding = "cp850")
    out = p.stdout
    array = out.split()
    puetaEnlace=array[21]
    
    return puetaEnlace
    