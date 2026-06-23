#!/usr/bin/env python3
"""Generate an offline release summary for the retail-store GitOps pipeline.

This script is intentionally offline-safe. It can be extended later to call
Amazon Bedrock or another approved internal AI platform from CI.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

SERVICES = ["ui", "catalog", "cart", "checkout", "orders"]


def main() -> None:
    changed = os.getenv("CHANGED_SERVICES", "").split()
    changed = [svc for svc in changed if svc in SERVICES]
    commit = os.getenv("GITHUB_SHA", "local")[:7]
    actor = os.getenv("GITHUB_ACTOR", "local-user")
    run_id = os.getenv("GITHUB_RUN_ID", "local-run")

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "release_type": "retail-store-gitops",
        "commit": commit,
        "triggered_by": actor,
        "run_id": run_id,
        "changed_services": changed or SERVICES,
        "risk_summary": "Review service-specific logs, Trivy scan results, and ArgoCD sync status before production rollout.",
        "recommended_checks": [
            "Confirm each changed service image exists in Amazon ECR.",
            "Verify ArgoCD application health is Synced and Healthy.",
            "Review Trivy SARIF and SBOM artifacts.",
            "Smoke test the retail UI and checkout flow.",
        ],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
