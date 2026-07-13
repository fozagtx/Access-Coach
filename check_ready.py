#!/usr/bin/env python3
"""Fail loudly if the app cannot run for real."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    errors: list[str] = []

    env_path = ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

    key = os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY", "")
    if not key or "YOUR_" in key:
        errors.append("OPENROUTER_API_KEY missing — set it in .env")

    sys.path.insert(0, str(ROOT))
    try:
        # Delay agent import until key may be set
        if key and "YOUR_" not in key:
            from agent.agent import AGENT_TOOLS, SYSTEM_PROMPT

            if "Access Coach" not in SYSTEM_PROMPT:
                errors.append("SYSTEM_PROMPT is not Access Coach")
            if "fetch_thread" not in AGENT_TOOLS:
                errors.append("Access Coach tools not registered")
    except Exception as e:
        errors.append(f"import failed: {e}")

    if errors:
        print("NOT READY:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("READY: Access Coach + OpenRouter OK")
    print("Next: slack login (in your Developer sandbox) && slack run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
