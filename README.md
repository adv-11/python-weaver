# 🧵 python-weaver

[![PyPI version](https://img.shields.io/pypi/v/python-weaver.svg)](https://pypi.org/project/python-weaver)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


> **Transform complex, multi-stage workflows into reliable, resumable AI orchestration**

hey! im a grad student building this framework for catering every type of user who work with LLMs. It all started, when LLMs were missing important pieces of context in long shot conversations, tasks like research writing, market analysis, code migration were stunted. to tackle this, i made this framework, to make LLMs take notes, plan in advance, maintain a tracker (blueprint). i hope to make this production ready one day :D 

this framework enables llms to execute sophisticated, long-duration projects through intelligent task orchestration. By combining built-in connectors, human oversight, and multi-provider llm support, weaver bridges the gap between simple ai interactions and complex, real-world automation.

## Architecture Diagram
![Architecture Diagram](docs/diagrams/architecture.png)


## ✨ Why Weaver?

**🔄 Never Lose Progress Again**
- Stateful execution with SQLite persistence
- Resume interrupted workflows from any point
- Comprehensive error handling and retry logic

**🤝 Human-AI Collaboration**
- Review and edit AI-generated task plans
- Approve results before proceeding to next steps
- Export/import workflows via intuitive CSV interface

**🛡️ Production-Ready Architecture**
- Local-first security - your data never leaves your machine
- Multi-provider LLM support through litellm integration
- Modular, extensible design for custom workflows

**📊 Intelligent Task Management**
- Automatic dependency resolution
- Cost tracking across all LLM providers
- Detailed execution logs and timestamps

---


## 🚀 Quick Start

### Installation

```bash
pip install python-weaver
```

### Basic Usage

```python
from weaver.project import Project

# Initialize a new project
project = Project(
    project_name="market_analysis",
    project_goal="Generate a comprehensive market analysis report for renewable energy trends"
)

# Ingest your data sources
project.ingest([
    "data/market_report.pdf",
    "data/competitor_analysis.txt",
    "https://example.com/industry-trends"
])

# Generate an AI-powered execution plan
project.plan()
# 📝 Review and edit the generated blueprint.csv

# Execute with human oversight
project.run(human_feedback=True)
```

### CLI Workflow

```bash
# Initialize project
weaver init my_project "Analyze customer feedback and generate improvement recommendations"

# Add data sources
weaver ingest my_project reports/*.pdf feedback_data.csv

# Generate execution plan
weaver plan my_project

# Execute with human feedback
weaver run my_project

# Or run fully automated
weaver run my_project --no-human-feedback --steps 5
```

---

## 🏗️ Workflow
![Architecture Diagram](docs/diagrams/workflow.png)



Weaver's architecture ensures reliability and transparency:

- **Blueprint Database**: SQLite-backed task tracking with complete state persistence
- **Agent System**: Intelligent task execution with automatic retry and error handling  
- **Connector Framework**: Extensible ingestion system for PDFs, URLs, and custom sources
- **Multi-Provider Support**: Seamless integration with 10+ LLM providers via litellm

---

## 🎯 Core Features

### 📋 Intelligent Task Planning
- **Automated Decomposition**: Break complex goals into manageable, sequential tasks
- **Dependency Management**: Automatic resolution of task dependencies and prerequisites
- **Resource Optimization**: Smart LLM selection and load balancing across providers

### 🔄 Stateful Execution
- **Persistent State**: All progress saved to local SQLite database
- **Resume Capability**: Pick up exactly where you left off after interruptions
- **Audit Trail**: Complete execution history with timestamps and cost tracking

### 👥 Human-in-the-Loop
- **Plan Review**: Edit AI-generated task plans before execution
- **Result Approval**: Review and modify outputs at each step
- **CSV Interface**: Intuitive spreadsheet-based workflow management

### 🔌 Multi-Provider Support
- **OpenAI**: GPT-4, GPT-4 Turbo, GPT-3.5
- **Anthropic**: Claude 3 Haiku, Sonnet, Opus
- **Google**: Gemini 1.5 Pro, Flash
- **Azure OpenAI**: Enterprise-grade OpenAI models
- **Local Models**: Ollama, LM Studio integration
- **Custom Providers**: Easy integration via litellm

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- At least one LLM provider API key

### Quick Setup

```bash
# Install from PyPI
pip install python-weaver

# Verify installation
weaver check
```

### Provider Configuration

Set your API keys as environment variables:

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."

# Google
export GOOGLE_API_KEY="AIza..."

# Azure OpenAI
export AZURE_API_KEY="..."
export AZURE_API_BASE="https://your-resource.openai.azure.com/"
```

### Advanced Configuration

Create a `weaver.toml` file for advanced settings:

```toml
[litellm]
set_verbose = true
drop_params = true

[api_bases]
openai = "https://api.openai.com/v1"
anthropic = "https://api.anthropic.com"

[models]
default_orchestrator = "gpt-4o-mini"
```



## 🔧 Advanced Usage

### Custom Connectors

Extend Weaver with custom data sources:

```python
from weaver.connectors.base_connector import BaseConnector

class DatabaseConnector(BaseConnector):
    def ingest(self, source: str) -> str:
        # Your custom ingestion logic
        return extracted_text

# Register and use
project.register_connector("db", DatabaseConnector())
project.ingest(["db://my_database/table"])
```

### Programmatic Workflow Management

```python
from weaver.blueprint import Blueprint
from weaver.agent import Agent

# Direct blueprint manipulation
blueprint = Blueprint("my_project.db")
task_id = blueprint.add_task(
    task_name="Data Analysis",
    llm_config_key="claude-3-sonnet",
    prompt_template="Analyze the following data: {data}",
    dependencies="1,2"
)

# Execute specific tasks
agent = Agent(blueprint, "My project goal")
agent.execute_task(task_id)
```

### Cost Optimization

```python
# Configure cost-aware execution
project = Project("cost_optimized", "Generate report")

# Use different models for different task types
project.blueprint.add_task(
    task_name="Quick Summary",
    llm_config_key="gpt-4o-mini",  # Cost-effective for simple tasks
    prompt_template="Summarize: {content}"
)

project.blueprint.add_task(
    task_name="Deep Analysis", 
    llm_config_key="gpt-4o",  # High-quality for complex analysis
    prompt_template="Provide detailed analysis: {content}"
)
```

---

## 📊 Real-World Examples

### 📈 Market Research Automation
```python
project = Project("market_research", "Comprehensive renewable energy market analysis")
project.ingest([
    "reports/iea_renewable_2024.pdf",
    "data/market_data.csv",
    "https://irena.org/statistics"
])
project.plan()
project.run()
```

### 📚 Academic Research Pipeline
```python
project = Project("literature_review", "Systematic review of AI ethics literature")
project.ingest([
    "papers/*.pdf",
    "abstracts.txt",
    "https://arxiv.org/search/cs.AI"
])
project.plan()
project.run(steps=3)  # Process in batches
```

### 🏢 Business Process Automation
```python
project = Project("quarterly_report", "Generate Q4 business performance report")
project.ingest([
    "financials/q4_data.xlsx",
    "metrics/kpi_dashboard.csv",
    "feedback/customer_surveys.txt"
])
project.plan()
project.run(human_feedback=True)
```

---

## 🛠️ Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/python-weaver/python-weaver.git
cd python-weaver

# Install in development mode
pip install -e .[dev]

# Run tests
pytest

# Run with coverage
pytest --cov=weaver --cov-report=html
```

### Project Structure

```
python-weaver/
├── weaver/
│   ├── __init__.py
│   ├── project.py          # Main user interface
│   ├── blueprint.py        # SQLite task management
│   ├── agent.py           # LLM task execution
│   ├── config.py          # Provider configurations
│   ├── cli.py             # Command-line interface
│   └── connectors/        # Data ingestion modules
├── tests/                 # Comprehensive test suite
├── examples/              # Usage examples
└── docs/                  # Documentation
```

### Contributing

could use all the help i can get. i'll make a contributing guide soon to help you easily navigate and develop! 

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📋 Roadmap

### 🚀 Upcoming Features

- **🔄 Async/Await Patterns**
- **📊 Entirely customizable connectors**
- **🌐 Web Interface**: Browser-based project management dashboard


### 🎯 Current Focus

- Documentation and Official Website
- DB Optimization
- Better Memory Management
- RAG For long contexts
- Security Concerns addressing
---

## 📚 Documentation

Coming Soon!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
