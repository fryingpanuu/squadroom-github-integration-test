#!/usr/bin/env python3
"""Lightweight, deterministic GitHub integration smoke test.

This script performs simple in-process checks and prints a clear success
message when all validations pass. It is intentionally side-effect free.
"""

from __future__ import annotations

import hashlib
import os
import sys


EXPECTED_MARKER = "8973ded1418b0b0ffdc0331c773f01c0e8177c539102af2849ec3d326cbf575a"


def build_marker() -> str:
    """Return a deterministic SHA-256 marker used as the test assertion."""

    return hashlib.sha256(
        "github_integration_disposable_test".encode("utf-8")
    ).hexdigest()


def assert_runtime_environment() -> None:
    """Validate assumptions that should always hold for this script."""

    if sys.version_info < (3, 8):
        raise RuntimeError("Python 3.8+ is required")

    if os.name not in {"posix", "nt"}:
        raise RuntimeError("Unsupported runtime platform")


def main() -> int:
    """Run deterministic checks and return an appropriate exit code."""

    try:
        assert_runtime_environment()

        marker = build_marker()
        if marker != EXPECTED_MARKER:
            print("ERROR: deterministic marker mismatch")
            return 1

        print("[ok] runtime check passed")
        print(f"[ok] deterministic marker: {marker}")
        print("SUCCESS: disposable GitHub integration test completed")
        return 0
    except Exception as exc:  # pragma: no cover - defensive path for smoke test
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
