# Building a Retail Store DevOps Platform on AWS EKS with GitOps

This project demonstrates how a real microservices application can be deployed using modern DevOps practices. The application includes UI, catalog, cart, orders, and checkout services, each packaged with Docker and Helm.

The platform layer uses Terraform to provision AWS networking and Amazon EKS, while ArgoCD continuously syncs Kubernetes manifests from Git. GitHub Actions handles changed-service builds, image scanning, SBOM generation, image publishing to Amazon ECR, and Helm value updates.

## Why this project matters

Many enterprise teams are moving from basic CI/CD pipelines toward platform engineering and GitOps. This project shows that progression by combining infrastructure as code, Kubernetes packaging, secure CI/CD, container scanning, and operational documentation.

## Key learning areas

- Multi-service application deployment
- Amazon EKS Auto Mode
- Terraform infrastructure automation
- Helm-based Kubernetes packaging
- ArgoCD GitOps reconciliation
- Amazon ECR image publishing
- GitHub Actions with AWS OIDC
- Trivy vulnerability scanning
- SBOM generation
- Rollback and runbook process
