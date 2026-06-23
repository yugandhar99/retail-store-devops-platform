# Portfolio Notes

## Project positioning

This project represents a more advanced DevOps/Platform Engineering portfolio project. It shows how to deploy a real multi-service retail application to AWS using Terraform, EKS Auto Mode, Helm, ArgoCD GitOps, Amazon ECR, and GitHub Actions.

## Best resume bullet

Built and modernized a retail microservices DevOps platform using AWS EKS Auto Mode, Terraform, Helm, ArgoCD GitOps, Amazon ECR, and GitHub Actions, adding changed-service deployments, OIDC-based AWS authentication, Trivy scanning, SBOM generation, CodeQL, dependency review, drift detection, and operational runbooks.

## Interview explanation

I worked on a retail store microservices project where each service was containerized and deployed to Amazon EKS using Helm charts. I used Terraform to provision the VPC, EKS cluster, and add-ons, then used ArgoCD to continuously reconcile the Kubernetes state from Git.

To make it closer to a production DevOps workflow, I improved the CI/CD process so GitHub Actions detects which service changed, builds only that service, scans the image with Trivy, generates an SBOM, pushes the image to Amazon ECR, updates the Helm values, and lets ArgoCD deploy the change. I also moved the pipeline toward OIDC-based AWS authentication instead of long-lived access keys.

## Career progression shown

- Basic containerization: Dockerized services
- Intermediate DevOps: Helm charts and GitHub Actions
- Advanced DevOps/Platform: EKS, Terraform, ArgoCD GitOps, ECR, OIDC, SBOM, security scanning, drift detection
- Modern operations: release summaries, runbooks, observability notes, and rollback process
