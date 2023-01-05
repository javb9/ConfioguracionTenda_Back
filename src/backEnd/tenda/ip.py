import subprocess

def obtenerPuertaEnlace():
    ip=("netsh interface ipv4 show address Wi-Fi")
    p = subprocess.run('netsh interface ipv4 show address Wi-Fi',
                    stdout=subprocess.PIPE,
                    shell = True,
                    universal_newlines = True,
                    encoding = "cp850")
    out = p.stdout
    array = out.split()
    puetaEnlace=array[21]
    prefijo=array[14].split('/')[1]
    return puetaEnlace
    