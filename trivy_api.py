from crypt import methods

from flask import Flask, jsonify, request

app_trivy = Flask(__name__)

from demo import analisis_trivy

@app_trivy.route('/ping')
def ping():
  return jsonify({"message": "pong!"})

@app_trivy.route('/trivy' , methods=['POST'])
def trivy():
  new_analisis = {
      "docker_image": request.json['docker_image'],
      "version": request.json['version']
  }
  docker = request.json['docker_image']
  version = request.json['version']
  archivo_cve = analisis_trivy(docker, version)
  return jsonify({"message": "Analisis lanzado se vera el resultado en el archivo " + archivo_cve } )


if __name__ == '__main__':
    app_trivy.run(debug=True, host='0.0.0.0', port=4000)