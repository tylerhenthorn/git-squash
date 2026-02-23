import argparse
import sys
from .squash import squash_history, GitSquashError


def main():
    parser = argparse.ArgumentParser(
        description="Flatten entire git history to a single commit"
    )
    parser.add_argument(
        "repo_path",
        nargs="?",
        default=".",
        help="Path to git repository (default: current directory)"
    )
    parser.add_argument(
        "-m", "--message",
        default="Squashed",
        help="Commit message (default: Squashed)"
    )
    parser.add_argument(
        "-b", "--branch",
        help="Branch name (default: current branch)"
    )

    args = parser.parse_args()

    try:
        squash_history(
            repo_path=args.repo_path,
            message=args.message,
            branch=args.branch
        )
        print(f"Successfully squashed history: {args.message}")
    except GitSquashError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
