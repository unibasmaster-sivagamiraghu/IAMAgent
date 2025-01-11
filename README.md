# IAM Agent Project

## Overview
This project implements an AI-powered Identity and Access Management (IAM) agent using CrewAI. The agent helps automate the classification of AD groups, mapping them to IT roles, and creating business roles.

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your configuration:
   ```
   API_BASE_URL=your_api_base_url
   API_KEY=your_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage
Run the main script:
```bash
python src/main.py
```

## Testing
Run the tests:
```bash
python -m unittest discover tests
```

## Project Structure
- `config/`: Configuration files
- `src/`: Source code
  - `agents/`: Agent definitions
  - `tools/`: Tool implementations
  - `tasks/`: Task definitions
- `tests/`: Unit tests