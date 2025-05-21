## Vision

- [[Sovereign OS - "EU Linux"]] (Lots of historical and contextual information)
- www.eu-os.eu: main site for the project
- [[EU OS FAQ]]
- [EU OS Manifesto](https://gitlab.com/eu-os/eu-os.gitlab.io/-/issues/4) (draft)
- [[EU OS <-> Abilian|EU OS <-> Abilian]] (draft)

## WIP (2025)

- [[EU OS POC (2025)]]: summary of the discussions around the EU OS POC to be developed over S1 2025.
- Hackathon: 2-3 June, Paris.
    *   **Overall Goal:** Develop a Proof-of-Concept (PoC) for EU OS, specifically demonstrating the unattended setup of a bootc-based OS with device lifecycle and user management (including optional Active Directory integration).
    *   **Focus:** Integrating existing upstream software components, documenting the process thoroughly for reproducibility, fixing potential upstream issues, and demonstrating the working system.
    *   **Key Tasks (Prioritized):**
        1.  Documentation (horizontal task)
        2.  Create/update custom OCI OS images (Gitlab CI, blue-build)
        3.  Bare-metal OS installation (manual then unattended via PXE/Anaconda)
        4.  Setup fleet monitoring (Foreman, Katello)
        5.  Setup Full-Disk Encryption (FDE) (Password, TPM, FIDO2)
        6.  Setup SSO (SSSD, FreeIPA - AD compatible)
        7.  Setup OCI image scanning (SBOM/Vulnerabilities)
        8.  Outreach to local stakeholders (e.g., CNIL, Gendarmerie).
