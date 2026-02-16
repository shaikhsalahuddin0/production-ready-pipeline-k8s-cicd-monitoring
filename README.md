# Production-Ready DevOps Pipeline with Kubernetes, CI/CD & Monitoring

This project demonstrates how a simple web application can be built, containerized, deployed on Kubernetes, and monitored in a production-style setup. The focus of this project is to showcase practical DevOps skills such as CI/CD automation, container orchestration, health checks, monitoring, and logging.

The goal was not just to run an application, but to build an end-to-end workflow similar to what DevOps teams follow in real-world environments.

---

## Project Overview

This project covers the complete lifecycle of an application:

- Code pushed to GitHub  
- Automated build and containerization using CI/CD  
- Deployment on Kubernetes with multiple replicas  
- Health checks and service exposure  
- Metrics collection using Prometheus  
- Visualization and monitoring using Grafana  
- Centralized logging for troubleshooting  

It reflects how modern DevOps pipelines are designed and operated.

---

## Architecture & Flow

The flow of this project is as follows:

1. Developer pushes code to GitHub  
2. CI/CD pipeline builds a Docker image  
3. The image is deployed to Kubernetes  
4. Kubernetes runs the application in pods and exposes it via a service  
5. Prometheus scrapes metrics from the application  
6. Grafana visualizes traffic, latency, CPU, and memory usage  
7. Logs are collected for debugging and monitoring  


---

## Tech Stack

- Application: Python (Flask)  
- Containerization: Docker  
- Orchestration: Kubernetes (Minikube for local setup)  
- CI/CD: Jenkins  
- Monitoring: Prometheus, Grafana  
- Logging: Loki, Promtail  
- Local Cluster: Minikube  

---

## Why This Stack

This stack was chosen to match tools commonly used in real DevOps environments:

- Docker helps package the application in a consistent and portable way.  
- Kubernetes manages deployment, scaling, and service networking.  
- CI/CD automates build and deployment, reducing manual effort and mistakes.  
- Prometheus and Grafana provide visibility into application performance and system health.  
- Centralized logging makes debugging easier when multiple pods are running.

---

## Key Features

- Containerized application deployed on Kubernetes  
- Rolling updates and multiple replicas for availability  
- Automated build and deployment pipeline  
- Health check and metrics endpoints exposed by the app  
- Real-time monitoring dashboards in Grafana  
- Logs collected for troubleshooting  

---

## Live Outputs & Monitoring

Below are real outputs captured from the running system. These screenshots show that the application is live on Kubernetes and is being monitored properly.

### Application Running (Home Endpoint)
This confirms that the service is accessible.

<img width="1920" height="1020" alt="localhost_8080 - Google Chrome 16-02-2026 11_01_55" src="https://github.com/user-attachments/assets/8c598174-a380-42c1-9740-420a6ef38817" />

---

### Health Check Endpoint
Used by Kubernetes readiness and liveness probes.

<img width="1920" height="1020" alt="localhost_8080_health - Google Chrome 16-02-2026 11_11_44" src="https://github.com/user-attachments/assets/f937e4c6-d16d-4610-8e1b-618db52f6656" />


---

### Metrics Endpoint (Prometheus)
Exposes application and process metrics.

<img width="1920" height="967" alt="localhost_8080_metrics - Google Chrome 16-02-2026 11_13_01" src="https://github.com/user-attachments/assets/30e5fb59-25af-4d04-8ef0-8d4a53b2601e" />



---

### Monitoring Dashboard (Grafana)
Shows request rate, latency, pod CPU usage, memory usage, and running replicas.

<img width="1536" height="1024" alt="ChatGPT Image Feb 16, 2026, 05_58_33 PM" src="https://github.com/user-attachments/assets/8b95bcb1-4a9f-45b8-9a9c-b34106f08e95" />


---

## How to Run Locally (Minikube)

```bash
minikube start
eval $(minikube docker-env)

docker build -t sample-flask:latest ./app

kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

kubectl -n devops-demo port-forward svc/sample-flask 8080:80
