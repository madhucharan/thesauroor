# Thesauroor

A simple Streamlit-based chat app built to explore and understand various
prompting techniques.

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (a fast Python package manager)

Note: You do not need to pre-install Python. uv will install and manage the
required Python version automatically if needed

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/thesauroor.git
   cd thesauroor
   ```

2. **Install dependencies using uv:**

   ```bash
   uv sync
   ```

3. **(Optional) Create a virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

   _Note: This step is optional if you use uv run to execute commands_

## Running the Project

To start the project, use:

```bash
uv run streamlit run main.py
```
