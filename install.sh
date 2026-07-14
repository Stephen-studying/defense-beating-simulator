#!/usr/bin/env sh
set -eu

agent="codex"
destination=""
force=0
skill_name="defense-beating-simulator"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --agent)
      [ "$#" -ge 2 ] || { echo "--agent requires a value" >&2; exit 2; }
      agent="$2"
      shift 2
      ;;
    --dest)
      [ "$#" -ge 2 ] || { echo "--dest requires a value" >&2; exit 2; }
      destination="$2"
      shift 2
      ;;
    --force)
      force=1
      shift
      ;;
    -h|--help)
      echo "Usage: sh install.sh [--agent codex|agents|generic|claude|gemini|copilot|project] [--dest PATH] [--force]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

case "$agent" in
  codex|agents|generic|claude|gemini|copilot|project)
    ;;
  *)
    echo "Unknown agent: $agent" >&2
    exit 2
    ;;
esac

if [ -z "$destination" ]; then
  case "$agent" in
    codex) destination="${CODEX_HOME:-$HOME/.codex}/skills" ;;
    agents|generic) destination="${AGENT_SKILLS_HOME:-$HOME/.agents/skills}" ;;
    claude) destination="$HOME/.claude/skills" ;;
    gemini) destination="$HOME/.gemini/skills" ;;
    copilot) destination="$HOME/.copilot/skills" ;;
    project)
      echo "Project mode requires --dest, for example: --dest \"\$HOME/your-project/.agents/skills\"" >&2
      exit 2
      ;;
  esac
fi

source_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
if [ ! -f "$source_dir/SKILL.md" ]; then
  echo "Cannot find SKILL.md at $source_dir/SKILL.md. Run this script from the repository root." >&2
  exit 1
fi

mkdir -p "$destination"
destination_abs="$(CDPATH= cd -- "$destination" && pwd)"
case "$destination_abs" in
  "$source_dir"|"$source_dir"/*)
    echo "Destination must not be inside the source repository. Choose another project directory or a user-level skills directory." >&2
    exit 2
    ;;
esac

target="$destination_abs/$skill_name"
if [ -e "$target" ]; then
  if [ "$force" -ne 1 ]; then
    echo "Target already exists: $target. Re-run with --force to replace it." >&2
    exit 1
  fi
  case "$target" in
    "$destination_abs/$skill_name") rm -rf "$target" ;;
    *)
      echo "Refusing to remove target outside destination: $target" >&2
      exit 1
      ;;
  esac
fi

mkdir -p "$target"
for name in SKILL.md AGENTS.md CLAUDE.md GEMINI.md LICENSE agents references assets; do
  item="$source_dir/$name"
  if [ ! -e "$item" ]; then
    echo "Required runtime entry is missing: $name" >&2
    exit 1
  fi
  cp -R "$item" "$target/"
done

if [ ! -f "$target/SKILL.md" ]; then
  echo "Installation failed: SKILL.md was not copied to $target" >&2
  exit 1
fi

echo "Installed $skill_name for '$agent' to:"
echo "$target"
echo ""
if [ "$agent" = "codex" ]; then
  echo 'Restart Codex, then invoke $defense-beating-simulator.'
else
  echo "Ask the agent to discover the installed skill or read:"
  echo "  - $target/SKILL.md"
  echo "  - $target/AGENTS.md when explicit routing is needed"
fi
