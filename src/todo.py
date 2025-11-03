"""Simple todo CLI using argparse and JSON for storage.

Usage examples:
  python -m src.todo add "Buy milk"
  python -m src.todo list

This file provides a minimal, dependency-free skeleton suitable for extension.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import List, Dict, Any


DEFAULT_TASKS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tasks.json")


def load_tasks(path: str = DEFAULT_TASKS_FILE) -> List[Dict[str, Any]]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks: List[Dict[str, Any]], path: str = DEFAULT_TASKS_FILE) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(tasks, fh, indent=2, ensure_ascii=False)


def add_task(description: str, path: str = DEFAULT_TASKS_FILE) -> None:
    tasks = load_tasks(path)
    next_id = max((t.get("id", 0) for t in tasks), default=0) + 1
    task = {"id": next_id, "description": description, "done": False}
    tasks.append(task)
    save_tasks(tasks, path)
    print(f"Added task #{next_id}: {description}")


def list_tasks(path: str = DEFAULT_TASKS_FILE) -> None:
    tasks = load_tasks(path)
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "x" if t.get("done") else " "
        print(f"[{status}] {t.get('id')}: {t.get('description')}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="Simple todo CLI (add, list)")
    parser.add_argument("--file", "-f", default=DEFAULT_TASKS_FILE,
                        help="Path to tasks JSON file (default: repository tasks.json)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("description", nargs=argparse.REMAINDER, help="Task description")

    p_list = sub.add_parser("list", help="List tasks")
    # potential future args (filtering, show-done, etc.)

    return parser


def main(argv: List[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    tasks_file = args.file

    if args.command == "add":
        # description may be multiple tokens
        desc = " ".join(args.description).strip()
        if not desc:
            print("Error: empty task description.")
            return 2
        add_task(desc, path=tasks_file)
        return 0
    elif args.command == "list":
        list_tasks(path=tasks_file)
        return 0
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
