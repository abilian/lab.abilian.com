In software architecture, an Architectural Decision Records (or ADR) is a document that captures an important architectural decision made along with its context and consequences.

When developing software, teams need to make numerous decisions regarding the architecture, technologies, design patterns, and more. These decisions can significantly influence the course of the project and the software's final outcome. However, the reasoning behind these decisions can be lost or forgotten over time, especially in large teams or long-term projects.

ADRs help to prevent this loss of information. They provide a structured way to capture these decisions, making it easier for current and future team members to understand why a particular decision was made.

The whole document should be one or two pages long. Written as if it is a conversation with a future developer. This requires good writing style, with full sentences organized into paragraphs. Bullets are acceptable only for visual style, not as an excuse for writing sentence fragments.

## Structure

An ADR typically includes the following sections:

1.  **Title:** A brief, descriptive title for the decision.
2.  **Status:** The current status of the decision (e.g., proposed, accepted, rejected, deprecated, replaced).
3.  **Context:** A description of the situation and factors that led to the need for a decision.
4.  **Decision:** The decision that was made.
5.  **Consequences:** The expected outcomes, impacts, or changes that will result from the decision. This section should include both positive and negative consequences.

ADRs are particularly useful in projects that use agile methodologies, where decisions may need to be revisited as the project evolves. They also foster greater transparency and understanding within the team, making it easier to onboard new team members or transition responsibilities.

## Pros and cons

**Pros**:

-   We have a clear log of the different decisions taken, which can help newcomers to understand past decisions.
-   It can help in the discussion of such changes.
-   Architecture decisions recorded in small modular readable documents.

**Cons**:

-   More time is required for each change, as we need to document and discuss it.


## Relationship with patterns

[[Design Patterns]] provide general solutions to recurring problems, while ADRs record specific decisions made within the context of a particular project, which could include the use of certain patterns. Patterns are more about "how" to design and code, while ADRs are more about "why" certain decisions were made.

## ADR are not only about architecture

Architectural Decision Records (ADRs) can be used to record decisions that are not strictly architectural in nature. While the term "architectural" is in the name, it's become a bit of a misnomer as the practice has evolved.

ADRs can capture important decisions about design, technology choices, coding standards, and even process changes - essentially any decision that has a significant impact on the project and that future team members might need to understand.

The term "architectural" in ADR is a reflection of the original intent and context of these records: to capture high-level, system-wide decisions typically made by software architects. However, the utility of documenting significant decisions in a structured way has seen ADRs applied more broadly.

## ADRs vs. RFCs

While there is overlap in the purposes of ADRs and RFCs, they serve different functions in the software development process:

1.  **ADRs (Architectural Decision Records):**

    ADRs are documents that capture an important architectural decision made along with its context and consequences. **They are records of key decisions that help future team members understand the rationale behind decisions, and they promote transparency and knowledge sharing**.

    ADRs tend to be more localized to a specific project or product, and they typically address specific technical issues or decisions, like choosing a particular technology, framework, pattern, or method for implementing a feature. While they should be as long as needed, they should be generally quite short (1-2 pages).

2.  **RFCs (Request for Comments):**

    RFCs are broader in scope and are often used to propose new features, methodologies, or changes in a system. They are used for obtaining feedback and building consensus in the early stages of proposing a change or a new feature. RFCs often go through a period of review and discussion before being accepted or rejected.

    RFCs, originally used in the development of the Internet, are often used by open-source communities to propose changes and get community feedback. **They tend to be more about proposing ideas and getting feedback, rather than documenting decisions that have already been made.**

In this sense, Python's PEPs (Python Enhancement Proposals) a more akon to RFCs that to ADRs (though they serve as ADRs, *post-hoc*).

In summary, while both ADRs and RFCs are ways of documenting and communicating about design and architecture, they serve different purposes and are used at different stages of the decision-making process. ADRs are typically used to document a decision that has been made, while RFCs are used to propose a change and gather feedback.

## References

- https://lyz-code.github.io/blue-book/adr/
- https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- https://github.com/joelparkerhenderson/architecture-decision-record
- https://www.infoq.com/news/2020/04/architecture-decision-records/

## Examples in the wild

- https://github.com/thomvaill/log4brains/tree/master/docs/adr
- https://github.com/nats-io/nats-architecture-and-design
- https://github.com/arachne-framework/architecture
