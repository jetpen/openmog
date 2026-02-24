OpenMog Documentation
=====================

**OpenMog** is an autonomous AI agent swarm orchestrator that coordinates multiple AI agents to accomplish complex tasks through intelligent planning, execution, and collaboration.

Overview
--------

OpenMog provides a framework for building and deploying autonomous AI agents that can:

- Understand and execute complex, multi-step tasks
- Coordinate with other agents in a swarm
- Learn and adapt through continuous improvement
- Maintain durable memory of plans and progress
- Collaborate with human operators when needed

Key Features
------------

- **Multi-Agent Orchestration**: Coordinate multiple AI agents working together
- **Intelligent Planning**: Strategic and tactical planning with dependency management
- **Memory Management**: Persistent storage of agent state, plans, and history
- **Skill System**: Extensible skill architecture for agent capabilities
- **Configuration-Driven**: Purpose, authorizations, and settings via config files
- **Human Collaboration**: Seamless integration with human oversight and input

Getting Started
---------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   configuration
   usage
   development
   api

Installation
------------

Install OpenMog using pip:

.. code-block:: bash

   pip install openmog

For development:

.. code-block:: bash

   git clone https://github.com/jetpen/openmog.git
   cd openmog
   pip install -e ".[dev]"

Quick Start
-----------

1. Configure your agent:

   .. code-block:: yaml

      # config.yaml
      purpose: "Assist with software development tasks"
      authorizations:
        auto_approve: ["read_files", "run_tests"]
        require_review: ["deploy_code"]
      settings:
        model: "gpt-4"
        max_subagents: 5

2. Run the agent:

   .. code-block:: bash

      openmog run --config config.yaml

Contributing
------------

We welcome contributions! Please see our :doc:`contributing` guide for details.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`