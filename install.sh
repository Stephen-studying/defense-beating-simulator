#!/usr/bin/env sh
set -eu

agent="codex"
destination=""
force=0
skill_name="defense-beating-simulator"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --agent)
      agent="$2"
      shift 2
      ;;
    --dest)
      destination="$2"
      shift 2
      ;;
    --force)
      force=1
      shift
      ;;
    -h|--help)
      echo "Usage: sh install.sh [--agent codex|generic] [--dest PATH] [--force]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

case "$agent" in
  codex|generic)
    ;;
  *)
    echo "Unknown agent: $agent. Expected codex or generic." >&2
    exit 2
    ;;
esac

if [ -z "$destination" ]; then
  if [ "$agent" = "codex" ]; then
    destination="${CODEX_HOME:-$HOME/.codex}/skills"
  else
    destination="${AGENT_SKILLS_HOME:-$HOME/.agent-skills}"
  fi
fi

source_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

if [ ! -f "$source_dir/SKILL.md" ]; then
  echo "Cannot find SKILL.md at $source_dir/SKILL.md. Run this script from the repository root." >&2
  exit 1
fi

mkdir -p "$destination"
destination_abs="$(CDPATH= cd -- "$destination" && pwd)"
target="$destination_abs/$skill_name"

if [ -e "$target" ]; then
  if [ "$force" -ne 1 ]; then
    echo "Target already exists: $target. Re-run with --force to replace it." >&2
    exit 1
  fi
  case "$target" in
    "$destination_abs/$skill_name")
      rm -rf "$target"
      ;;
    *)
      echo "Refusing to remove target outside destination: $target" >&2
      exit 1
      ;;
  esac
fi

cp -R "$source_dir" "$target"

echo "Installed $skill_name for '$agent' to:"
echo "$target"
echo ""
if [ "$agent" = "codex" ]; then
  echo 'Restart Codex, then use: Use $defense-beating-simulator to analyze my project defense materials.'
else
  echo "Point your agent at one of these entrypoints:"
  echo "  - $target/AGENTS.md"
  echo "  - $target/SKILL.md"
fi
