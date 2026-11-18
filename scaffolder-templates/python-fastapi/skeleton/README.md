# ${{ values.component_id }}

> ${{ values.description }}

**Owner:** ${{ values.owner }}  
**Runtime:** Python 3.11 (FastAPI on Red Hat UBI 9 Minimal)  
**Governance:** TMX Golden Path Pilot

---

## 🚀 OpenShift Pipelines (Tekton) Security CI/CD

This application is managed natively by **OpenShift Pipelines (Tekton)**:
1. **`fetch-repository`:** Clones source code into a shared persistent workspace.
2. **`lint-dockerfile`:** Runs Hadolint static analysis for root execution (`USER 0`) and syntax rules.
3. **`unit-tests`:** Executes Pytest suite in `python:3.11-slim`, validating `/healthz` and `/ready` probes.
4. **`build-image`:** Compiles the OCI image rootlessly via `buildah` (`vfs` storage driver, `chroot` isolation).
5. **`generate-sbom`:** Extracts machine-readable CycloneDX SBOM (`sbom.cdx.json`) using Anchore Syft.
6. **`scan-vulnerabilities`:** Scans SBOM for CVE vulnerabilities with Aqua Security Trivy.
7. **`sign-image`:** Cryptographically validates and signs image provenance with Cosign.

### Running the Pipeline in OpenShift:
```bash
oc apply -f .tekton/pipeline.yaml
oc create -f .tekton/pipelinerun.yaml
```

View the live pipeline execution in the **Pipelines** tab of the OpenShift Web Console or directly inside **Red Hat Developer Hub** under the component's CI/CD tab!

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
