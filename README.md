# openmog
Autonomous AI agent swarm orchestrator

# Bootstrap

# Initialize source code project

Initialize this source code project with the artifacts to direct an AI coding agent to contribute. Ensure that these artifacts are maximally portable across AI coding agents including Cline, Claude Code, Codex, and kilocode. Expect that skills will be added. Choose the programming language and supply chain ecosystem that is most well suited to this project. Provide a document for contributor on-boarding that provides steps to initialize a freshly installed VS Code with the necessary extensions to be productive in that programming language and ecosystem.

# Initialize specifications of intent for openmog

openmog will be directed by configuration files that control:
- **purpose**: specifies what this openmog instance is intended to accomplish as its on-going concern
- **authorizations**: specifies authorizations (access that requires review and approval (and by whom), or access that is auto-approved) and access control
- **contacts**: specifies addresses for collaborators to communicate for delegating tasks for review, approval, and requesting assistance
- **settings**: controls settings, options, integrations, and the selection of which AI model to use

openmog will bootstrap this source code project to implement a complete autonomous AI agent that can use the chosen LLM (model) for reasoning, planning, and formulating actions. Begin by writing specifications for this automous AI agent swarm orchestrator.

The initial set of requirements are as follows.

- This agent will need to understand the purpose that is configured. In the abstract, this agent will serve to perform work as a colleague on a team.
- This agent will do planning strategically and heirarchically to decompose the work and incrementally to sequence tasks with dependencies.
- This agent will have durable memory of plans accomplished, current tasks, and planned tasks not yet started.
- This agent will perform incrementally replanning as as the outcome of tasks reveal work or rework that must be done.
- This agent will act to perform tasks.
- This agent will collaborate with humans for review and approval, according to the authorizations specified by the team.
- This agent will orchestrate subagents to accomplish parallizable work in the plan.
- This agent will act by applying skills, invoking tools, calling MCP servers, and retrieving information from data sources.
- This agent will be capable of self-improvement. This includes learning new skills, integrating additional tools, MCP servers, and data sources, as authorized by the owner of the deployment.
- This agent will communicate with other agents and collaborators using each participant's preferred channels, including options for JIRA, Slack, and email.

# Initialize the self-improving development of openmog

openmog will be used to instantiate at least one deployment of itself for the purpose of developing improvements to its own capabilities through code changes to this source code project working in collaboration with other deployment instances of openmog or with human contributors.
