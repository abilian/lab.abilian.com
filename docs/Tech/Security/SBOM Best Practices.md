Open source projects often lack clarity on the benefits of generating SBOMs, and the time and knowledge required to generate them are substantial. These projects typically operate with limited resources, and both short-term and long-term SBOM generation efforts are not cost-free. The direct benefits of SBOM generation for these projects remain unclear.

While the advantages of SBOMs for software consumers are more apparent, these benefits alone may not justify the additional effort required from open source projects without some form of assistance or incentive.

Moreover, there is limited guidance available for open source projects that want to generate and distribute SBOMs. Key questions include:

1. What tooling should be used to generate SBOMs?
2. What SBOM formats should be produced?
3. Should dependencies be documented, and if so, to what depth in the dependency tree?
4. How should these documents be distributed?
5. How should duplicate entries of dependencies be resolved across SBOMs?
6. How can the adoption of SBOMs be measured (e.g., through Scorecards)?
7. What tooling gaps exist, and how can they be addressed?

Additionally, collaboration with upstream projects is crucial to ensure proper tooling integration, and these efforts should be clearly outlined in a playbook. There should also be a focus on creating a Minimum Viable SBOM Report (MVSR) tied to the larger OpenSSF initiative.

## The Answers

The answers to these questions will vary depending on the ecosystem, programming language, and developer preferences.

## Proposed Plan

Rather than providing prescriptive guidance to open source projects on generating and distributing SBOMs, the SBOM Everywhere group proposes a hands-on approach. Currently, there are too many unknowns to offer concrete advice without practical experience in SBOM generation. By directly assisting projects in generating and distributing SBOMs, we can identify and address these unknowns. The goal is to help projects willing to engage with our team and to be flexible and patient as we work together to uncover best practices.

We propose creating an SBOM Strike Team that will work alongside open source projects to set up SBOM tooling. The team will document the lessons learned and make these resources available publicly for future use. This documentation should include not only the technical aspects of generating and distributing SBOMs but also the tangible benefits realized by participating projects.

### Plan Goals

The primary goal is to create a playbook based on the Strike Team’s experience that outlines best practices and lessons learned in SBOM generation and distribution.

### Action Items

1. **Create the SBOM Strike Team:**
   - The team will be responsible for carrying out the tasks outlined below.
   - Members will need to commit several hours per week to this effort.
   - Members should be able to communicate and collaborate effectively with open source projects.

2. **Engage Open Source Projects:**
   - Identify open source projects willing to participate. The goal is for these projects to review and approve pull requests (PRs), rather than implement tools or code.
   - Some level of project support will be necessary for Strike Team members to understand the development environment and workflow.

3. **Document Expectations:**
   - The target projects should generate SBOMs, sign them, and provide attestation using tools such as Rekor and in-toto.
   - Clear expectations and success criteria should be defined, such as whether the project’s SBOMs adhere to naming conventions and are properly signed and attested.

4. **Track Progress:**
   - Progress should be measured, and success should be defined by the adoption of SBOMs and the quality of these documents.
   - The Scorecards project can be extended to include checks that ensure SBOMs are in place and of high quality.

5. **Capture Best Practices:**
   - Leverage existing SBOM use cases from SBOM Everywhere, and capture lessons learned while working with open source communities.
   - Create a best practices document that outlines how to generate SBOMs for various languages and ecosystems, and update it as new lessons are learned.

6. **Create Documentation:**
   - Develop an open source SBOM use case document and an SBOM creation playbook that details how to generate SBOMs in specific formats.
   - These documents should be regularly updated as new insights emerge.

7. **Extend Tooling:**
   - Extend SBOM Scorecards and other tools to provide clear evaluations of SBOMs’ quality and completeness.

8. **Align with Broader Security Goals:**
   - Ensure alignment with the OpenSSF Software Security Mobilization Plan’s Goal 1, Workstream 3: developing a digital, risk-based metrics dashboard.
   - The Strike Team’s work will contribute to this dashboard by providing data on SBOM quality for open source projects.

### Plan Needs

- **SBOM Strike Team Staffing:**
   - A minimum of 2-4 team members will be required, with a commitment of at least 4 hours per week per member.
   - The team should have input and final say over which projects they collaborate with.

### New Guidance

- **Bidirectional Communication:**
   - Incentivize developers to generate SBOMs through education, best practices, and potentially financial incentives.
   - Establish clear channels of communication between end-users, developers, and third-party vendors regarding SBOM expectations across the supply chain.

<!-- Keywords -->
#developers #dependencies
<!-- /Keywords -->
