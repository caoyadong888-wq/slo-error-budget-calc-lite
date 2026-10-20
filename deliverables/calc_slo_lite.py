#!/usr/bin/env python3
"""Downtime only, for 30-day and 90-day windows.

The full calculator also scores request budgets, burn rate, a multi-window
policy stub, and an xlsx workbook. This file does not.
"""

from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal
from pathlib import Path


def dec_str(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text if text else "0"


def parse_percent(value: object) -> Decimal:
    if isinstance(value, bool) or isinstance(value, float) or value is None:
        raise ValueError("availability percent must be an integer or a decimal string")
    percent = Decimal(str(value).strip().rstrip("%"))
    if percent <= 0 or percent > 100:
        raise ValueError("availability percent must be in (0, 100]")
    return percent


def downtime(percent: Decimal, days: int) -> tuple[str, str, str]:
    allowed = Decimal(days) * Decimal(86400) * (Decimal(100) - percent) / Decimal(100)
    return dec_str(allowed), dec_str(allowed / Decimal(60)), dec_str(allowed / Decimal(3600))


def render(percent: Decimal) -> str:
    lines = [
        f"availability_percent: {dec_str(percent)}",
        f"budget_ratio: {dec_str((Decimal(100) - percent) / Decimal(100))}",
        "window_days  seconds  minutes  hours",
    ]
    for days in (30, 90):
        seconds, minutes, hours = downtime(percent, days)
        lines.append(f"{days}  {seconds}  {minutes}  {hours}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="30-day and 90-day SLO downtime only")
    parser.add_argument("--availability-percent")
    parser.add_argument("--scenario", help="JSON object with availability_percent")
    args = parser.parse_args(argv)
    try:
        if args.scenario:
            data = json.loads(Path(args.scenario).read_text(encoding="utf-8"))
            percent = parse_percent(data["availability_percent"])
        elif args.availability_percent:
            percent = parse_percent(args.availability_percent)
        else:
            raise ValueError("pass --availability-percent or --scenario")
    except (ValueError, KeyError, json.JSONDecodeError, OSError) as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 2
    sys.stdout.write(render(percent))
    return 0


if __name__ == "__main__":
    sys.exit(main())
