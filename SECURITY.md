# Security Notes

## Secrets

Do not commit AWS access keys, `.env` files, Terraform state files, kubeconfig files, or real production values.

This repository is configured to ignore:

- `.env` and `.env.*`
- `*.tfstate` and `*.tfstate.backup`
- `.terraform/`
- `terraform.tfvars`
- kubeconfig files
- SARIF/SBOM/generated scanner output

## AWS authentication

GitHub Actions should use AWS OIDC role assumption through `AWS_ROLE_TO_ASSUME`. Avoid storing long-lived `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` secrets in GitHub.

## Supply-chain checks

Recommended checks included in this project:

- Trivy filesystem and image scanning
- CodeQL static analysis
- Dependency Review for pull requests
- SBOM generation using CycloneDX format
- Dependabot updates

## Terraform state

Terraform state can contain sensitive infrastructure metadata. Use a remote backend such as S3 with encryption and locking for team usage. Do not upload state files to GitHub.
