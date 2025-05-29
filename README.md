# DevOps-Task-Hy


# we are going to containerise the python based application with the helm of tool like docker, k8s, helm. 
# we are using terraform for provison of infrastucture and argo cd for continuous delivery tool designed for Kubernetes.
# we are using Promethus & alertmanager for monitoring and observbility and sending alerts to email.

Kubernetes:
  - Deployments/service with resource limits, readiness/liveness probes
  - Ingress for external access
  - NetworkPolicy + RBAC + security  for security
  - Monit

Required toll

- AWS CLI configured or IAM user/Role
- kubectl and helm installed
- Terraform (≥ 1.3)
- Docker

Step to ci/cd

1. git clone https://github.com/<your-username>/<repo-name>.git
2. cd terraform/
terraform init
terraform apply

3. docker build -t flask-app . & docker push <ecr-url>:latest
4. kubectl apply -k k8s/
5.  Access the app using the host name provided in ingress file
6.  Monitoring and Alerting
   Prometheus scrapes /metrics using prometheus_flask_exporter
   Alerts routed to email using Alertmanager
   View logs via kubectl logs



