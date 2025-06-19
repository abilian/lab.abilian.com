## Automated install

This is not fully working yet.

Prerequisites:
- Python3
- `uv` (install via <https://docs.astral.sh/uv/getting-started/installation/>)

Here's how to run the installation scripts:

```
# Clone the H3NI Deployment repo
git clone https://gitlab.eclipse.org/eclipse-research-labs/nephele-project/opencall-2/h3ni/smo-deploy
cd smo-deploy
# Install dependencies (main one: Pyinfra)
uv sync
# Install
uv run make install
```

## Notes on Karmada

Documentation:

- https://karmada.io/docs/installation/
- https://karmada.io/docs/installation/install-cli-tools#install-kubectl-karmada
