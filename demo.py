from datetime import datetime
import shlex, subprocess
def analisis_trivy(docker_image,version):
    #docker_image = input('Dime el nombre de la imagen de docker: ')
    #version = input('Dime la versión o tag de la imagen: ')
    resultado_fecha = (datetime.today().strftime('%Y-%m-%d-%H:%M'))
    print(resultado_fecha)
    archivo_cve = (docker_image + '_' + version + '_' + resultado_fecha + '.html ')
    print(archivo_cve)
    comando = 'trivy image --format template --template "@templates/trivy.tpl" -o /Users/javer/Documents/trivy/reportes/' + archivo_cve
    print(comando)
    command_line = ( comando + docker_image + ':' + version)
    print(command_line)
    args = shlex.split(command_line)
    resultado = subprocess.call(args)
    return archivo_cve