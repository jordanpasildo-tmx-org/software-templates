# ${{ values.component_id }}

> ${{ values.description }}

**Owner:** ${{ values.owner }}  
**Runtime:** Python 3.11 (FastAPI on Red Hat UBI 9 Minimal)  
**Governance:** TMX Golden Path Pilot

---

## 🚀 Automated Security & CI/CD Pipeline

Whenever changes are pushed to `main`, the automated GitHub Actions pipeline performs:
1. **Automated Unit Tests:** Validates application routes, liveness (`/healthz`), and readiness (`/ready`).
2. **Rootless OCI Build:** Compiles the container on Red Hat UBI 9 Minimal running under `USER 1001`.
3. **SBOM Generation (Syft):** Emits a machine-readable CycloneDX Software Bill of Materials (`sbom.cdx.json`).
4. **Vulnerability Scanning (Trivy):** Scans the built container for CVEs across OS and Python packages.
5. **Image Publish:** Pushes the verified image to GitHub Container Registry (`ghcr.io`).

---

## ☸️ Deploying to OpenShift Developer Sandbox

To deploy this application to your OpenShift Developer Sandbox namespace, run:

```bash
oc apply -f k8s/
```

This creates:
- **Deployment:** Runs the hardened UBI 9 container as `USER 1001` with zero root privileges and read-only rootfs.
- **Service:** Exposes internal port `8080`.
- **Route:** Generates a public HTTPS endpoint for the application.

Verify status in OpenShift:
```bash
oc get pods -l app=${{ values.component_id }}
oc get route ${{ values.component_id }}
```
