# Audiobook Creator - Agent Configuration

## Build/Lint/Test Commands
- Install dependencies: `uv pip install -r requirements_cpu.txt` or `uv pip install -r requirements_gpu.txt`
- Run linting: `ruff check .`
- Run formatting: `ruff format .`
- Run specific test: `python -m pytest tests/test_specific.py::test_function_name -v`

## Code Style Guidelines
- Use Python 3.12 with uv for dependency management
- Follow PEP 8 style guide with ruff for linting/formatting
- Use type hints for all function parameters and return values
- Use descriptive variable names with snake_case convention
- Handle errors with specific exception types, not generic except clauses
- Use f-strings for string formatting
- Keep functions focused and small (< 50 lines ideally)
- Use async/await for I/O bound operations
- Import organization: standard library, third-party, local imports (each section sorted alphabetically)

## Environment Setup
- Configure .env file with LLM and TTS endpoints before running
- Set TTS_MODEL to either "kokoro" or "orpheus" in .env
- Ensure required services (LLM API, TTS API) are running before starting the app

## Key Components
- app.py: Gradio UI and FastAPI endpoints
- book_to_txt.py: Text extraction and cleaning
- identify_characters_and_output_book_to_jsonl.py: Character identification with GLiNER
- add_emotion_tags.py: Emotion tag enhancement (Orpheus only)
- generate_audiobook.py: Audiobook generation with TTS engines
- utils/: Helper modules for file operations, LLM calls, voice mapping, etc.

## Testing
- Run all tests: `python -m pytest`
- Run with coverage: `python -m pytest --cov=.`

## Docker
- CPU version: `cd docker/cpu && docker compose up --build`
- GPU version: `cd docker/gpu && docker compose up --build`