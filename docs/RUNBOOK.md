# Operations Runbook

## Check cluster access

```bash
aws eks update-kubeconfig --region us-west-2 --name <cluster-name>
kubectl get nodes
kubectl get pods -A
```

## Check ArgoCD

```bash
kubectl get applications -n argocd
kubectl describe application retail-store-ui -n argocd
kubectl logs -n argocd deployment/argocd-application-controller
```

## Check retail services

```bash
kubectl get pods -n retail-store
kubectl get svc -n retail-store
kubectl get ingress -n retail-store
kubectl logs -n retail-store deployment/ui --tail=100
```

## Roll back a service

1. Find the last known good image tag in Git history.
2. Revert the Helm `values.yaml` image tag for the affected service.
3. Commit the change to `main`.
4. Let ArgoCD reconcile, or run a manual sync.

```bash
git revert <bad-commit-sha>
git push origin main
```

## Common issues

### ArgoCD application is OutOfSync

```bash
kubectl describe application <app-name> -n argocd
```

Check chart values, image tag, namespace creation, and service account permissions.

### Pods are CrashLoopBackOff

```bash
kubectl logs -n retail-store <pod-name> --previous
kubectl describe pod -n retail-store <pod-name>
```

Review environment variables, config maps, database pods, and service DNS.

### Load balancer is not reachable

```bash
kubectl get svc -n ingress-nginx
kubectl describe svc -n ingress-nginx ingress-nginx-controller
```

Validate NLB provisioning, security group rules, and ingress annotations.
