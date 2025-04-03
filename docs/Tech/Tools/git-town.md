Home/docs: https://www.git-town.com/

"Git Town adds a layer of high-level commands to Git. They perform typical development workflow operations like creating or shipping feature branches, similar to how an expert Git user would do it."

## Intro

[Git Town](https://www.git-town.com/) is an open-source command-line tool that enhances your Git experience by providing high-level workflow commands. It doesn't replace Git; instead, it builds *on top* of it, automating common, multi-step processes involved in popular branching strategies.

By understanding your repository structure (through simple configuration of your main and perennial branches), Git Town offers commands like:

*   `git town hack <branch-name>`: Creates a new feature branch correctly based off your main branch.
*   `git town sync`: Updates your current branch and all parent branches (including main/perennial) from their remotes, handling potential rebases or merges.
*   `git town ship`: Merges your completed feature branch, updates relevant parent branches, optionally creates a pull request, and cleans up the local and remote feature branch.

Essentially, Git Town aims to make sophisticated Git workflows feel effortless, consistent, and less error-prone.

## "main branch" vs. "perennial branch" 

"Main branch" and "perennial branch" are **roles** you assign to certain branches via Git Town's configuration.

1.  **Main Branch (`main-branch`)**

    *   **Concept:** This is the primary, central branch of your repository. It typically represents the most stable, production-ready code or the main line of development from which releases are cut.
    *   **Common Names:** `main`, `master`.
    *   **Role in Git Town:**
        *   **Base for Features:** By default, new feature branches (`git town hack <feature-name>`) are created branching off the main branch.
        *   **Target for Shipping:** When you finish a feature branch, `git town ship` merges it *into* the main branch (and potentially perennial branches).
        *   **Syncing:** `git town sync` updates the main branch from its remote counterpart and prunes local feature branches that have been merged *into* it.
        *   **Configuration:** Git Town *requires* you to designate exactly **one** branch as the main branch during setup (`git town config setup` or `git town config main-branch <branch-name>`). This is crucial for its core logic.
    *   **Analogy:** Think of it as the trunk of your development tree.

2.  **Perennial Branches (`perennial-branches`)**

    *   **Concept:** These are long-lived branches that exist alongside the main branch indefinitely. They are *not* feature branches that get merged and deleted. They often represent different environments, ongoing development lines, or specific release versions that need continuous maintenance.
    *   **Common Examples:** `develop`, `staging`, `qa`, `production`, `release-v1.x`, `dev`.
    *   **Role in Git Town:**
        *   **Protected from Pruning:** `git town sync` and `git town kill` will *not* delete perennial branches. Git Town knows they are meant to stick around.
        *   **Kept Up-to-Date:** `git town sync` will update perennial branches from their remote counterparts, just like the main branch.
        *   **Optional Shipping Target:** When using `git town ship`, you can configure it (or it might be the default depending on your setup, e.g., with a `develop` branch) to *also* merge the completed feature branch into specified perennial branches. This is common for workflows where features go to `develop` before `main`, or need to be deployed to `staging`.
        *   **Configuration:** You can configure **zero or more** branches as perennial (`git town config perennial-branches <branch1> <branch2> ...`). Git Town needs to know which branches have this special status.
    *   **Analogy:** Think of them as major, long-lasting limbs growing alongside the main trunk, representing different stages or versions.

**Key Differences Summarized (Git Town Context):**

| Feature           | Main Branch                      | Perennial Branch(es)                | Feature Branch (Implicit)      |
| :---------------- | :------------------------------- | :---------------------------------- | :----------------------------- |
| **Purpose**       | Primary integration/release line | Long-lived parallel lines (envs, etc.) | Short-lived task/feature dev   |
| **Quantity**      | Exactly **One**                  | **Zero or More**                    | Many, temporary                |
| **Configured?**   | Yes (Required)                   | Yes (Optional, but recommended if used) | No (Implicitly detected)       |
| **`git town sync`** | Updates; Deletes *merged feature branches* based on it | Updates; **Never** deleted by sync | Deleted if merged into main |
| **`git town ship`** | Primary merge target             | **Optional** additional merge target | The branch being shipped        |
| **Lifespan**      | Perpetual                        | Long-lived / Perpetual              | Temporary                      |

**Why does Git Town care about this distinction?**

Git Town uses this configuration to automate common workflow steps safely and correctly:

*   It knows which branch is the stable base (`main`).
*   It knows which branches *not* to delete accidentally (`perennial`).
*   It knows where features typically start from and end up (`main`, potentially `perennial`).
*   It can intelligently sync all relevant long-lived branches (`main` + `perennial`).

<!-- Keywords -->
#git
<!-- /Keywords -->
