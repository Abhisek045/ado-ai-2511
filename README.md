# ado-ai-2511

This repository contains a minimal Python command-line todo application skeleton.

Files added in branch `add-todo-cli`:

- `src/todo.py` — a small CLI using `argparse` with `add` and `list` commands.
- `tasks.json` — JSON file used for storing tasks (initially empty).
- `requirements.txt` — lists project dependencies (none required by default).

Quick start
-----------

Run the CLI using the module form or directly with Python:

```bash
python -m src.todo add "Buy milk"
python -m src.todo list
```

The `tasks.json` file is stored at the repository root by default. You can override it using `-f /path/to/tasks.json`.

This is a lightweight starter intended to be expanded (edit, remove, mark-done, tests, packaging, etc.).
