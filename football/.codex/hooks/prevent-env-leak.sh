#!/usr/bin/env bash
set -euo pipefail

payload="$(cat)"

HOOK_PAYLOAD="$payload" python3 - <<'PY'
import json
import os
import sys
from pathlib import Path


def extract_command(obj):
    if isinstance(obj, dict):
        for path in [
            ("tool_input", "command"),
            ("toolInput", "command"),
            ("input", "command"),
            ("command",),
        ]:
            cur = obj
            ok = True
            for key in path:
                if isinstance(cur, dict) and key in cur:
                    cur = cur[key]
                else:
                    ok = False
                    break
            if ok and isinstance(cur, str):
                return cur

        for value in obj.values():
            found = extract_command(value)
            if found:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = extract_command(value)
            if found:
                return found
    return ""


def parse_env_values(env_path: Path):
    values = []
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        _, value = line.split("=", 1)
        value = value.strip().strip('"').strip("'")
        if not value:
            continue
        if len(value) < 4:
            continue
        values.append(value)
    return values


try:
    payload_text = os.environ.get("HOOK_PAYLOAD", "").strip()
    event = json.loads(payload_text) if payload_text else {}
except json.JSONDecodeError:
    sys.exit(0)

cmd = extract_command(event)
if not cmd:
    sys.exit(0)

env_values = parse_env_values(Path(".env"))
leaked = [v for v in env_values if v in cmd]

if leaked:
    print(
        "Bloqueado: el comando contiene un valor secreto de .env. "
        "Usa variables de entorno sin exponer el valor literal.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
PY
