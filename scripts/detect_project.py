#!/usr/bin/env python3
"""Read-only heuristic detector for project stack/domain signals."""
from pathlib import Path
import json
import sys

SIGNALS = {
    "react-nextjs": ["next.config.js", "next.config.mjs", "next.config.ts", "vite.config.js", "vite.config.ts"],
    "laravel-php": ["artisan", "composer.json", "phpunit.xml", "pest.php"],
    "shopify": ["shopify.theme.toml", "config/settings_schema.json", "sections", "snippets"],
    "mobile": ["app.json", "app.config.js", "app.config.ts", "ios", "android"],
    "data-engineering": ["dbt_project.yml", "great_expectations.yml"],
    "infrastructure": ["Dockerfile", "docker-compose.yml", "compose.yaml", "terraform", ".github/workflows"],
    "ai-applications": ["promptfooconfig.yaml", "langgraph.json"],
}
MANIFESTS = [
    "package.json", "pnpm-lock.yaml", "yarn.lock", "package-lock.json",
    "composer.json", "pyproject.toml", "requirements.txt", "Cargo.toml",
    "go.mod", "Gemfile", "pubspec.yaml", "pom.xml", "build.gradle",
]

def exists(root: Path, item: str) -> bool:
    p = root / item
    return p.exists()

def main():
    target = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not target.exists() or not target.is_dir():
        print(json.dumps({"error": f"Not a directory: {target}"}, indent=2))
        return 2

    found = []
    for pack, signals in SIGNALS.items():
        hits = [s for s in signals if exists(target, s)]
        if hits:
            found.append({"pack": pack, "evidence": hits})

    manifests = [m for m in MANIFESTS if exists(target, m)]
    result = {
        "project_path": str(target),
        "manifests": manifests,
        "suggested_packs": found,
        "notes": [
            "Heuristic detection only; verify against actual project files.",
            "No files were changed.",
            "Shopify themes may be detected by directory names even without a config file; inspect manually.",
            "Multiple packs may apply to a monorepo."
        ],
    }
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
