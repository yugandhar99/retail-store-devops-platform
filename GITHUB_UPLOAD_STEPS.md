# GitHub Upload Steps

Recommended repository name:

```text
retail-store-devops-platform
```

Recommended description:

```text
Retail store microservices DevOps platform using AWS EKS Auto Mode, Terraform, Helm, ArgoCD GitOps, ECR, GitHub Actions OIDC, Trivy, SBOM, CodeQL, and drift detection.
```

## Upload using GitHub website

This project has more than 100 files, so GitHub website upload may block one large drag-and-drop upload. Upload in batches:

1. Root files: `README.md`, `.gitignore`, `LICENSE`, `SECURITY.md`, `PORTFOLIO_NOTES.md`, `GITHUB_UPLOAD_STEPS.md`, `BRANCHING_STRATEGY.md`, `blog.md`
2. Folders: `.github`, `docs`, `infra`, `argocd`
3. Service folders one by one: `src/ui`, `src/catalog`, `src/cart`, `src/orders`, `src/checkout`, `src/app`

## Upload using Git commands

```bash
git init
git add .
git commit -m "Initial commit - Retail Store DevOps Platform"
git branch -M main
git remote add origin https://github.com/yugandhar99/retail-store-devops-platform.git
git push -u origin main
```

## Before deployment

Update these values if your repo name is different:

- `argocd/applications/*.yaml` repoURL
- `argocd/projects/retail-store-project.yaml` sourceRepos
- GitHub repository variables: `AWS_REGION`
- GitHub secret: `AWS_ROLE_TO_ASSUME`
