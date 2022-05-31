FROM python:3
RUN apt update -y  && apt upgrade -y  
RUN apt install wget apt-transport-https gnupg lsb-release -y && \
    wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | apt-key add - && \
    echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | tee -a /etc/apt/sources.list.d/trivy.list && \
    apt update && \
    apt install trivy -y 
WORKDIR /usr/src/app
RUN mkdir templates
COPY trivy.tlp ./templates
COPY trivy_api.py ./
COPY demo.py ./
RUN pip install flask
EXPOSE 4000
CMD ["python", "./trivy_api.py"]

