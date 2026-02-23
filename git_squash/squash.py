import os
import subprocess
from pathlib import Path


class GitSquashError(Exception):
    pass


def _run(*cmd, cwd=None):
    return subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=cwd)


def squash_history(repo_path=".", message="Squashed", branch=None):
    repo_path = Path(repo_path).resolve()

    try:
        _run("git", "rev-parse", "--git-dir", cwd=repo_path)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise GitSquashError(f"Not a git repository: {repo_path}")

    try:
        if branch is None:
            result = _run("git", "rev-parse", "--abbrev-ref", "HEAD", cwd=repo_path)
            branch = result.stdout.strip()

        temp_branch = f"temp-squash-{os.getpid()}"
        _run("git", "checkout", "--orphan", temp_branch, cwd=repo_path)
        _run("git", "add", "-A", cwd=repo_path)
        _run("git", "commit", "-m", message, cwd=repo_path)
        _run("git", "branch", "-D", branch, cwd=repo_path)
        _run("git", "branch", "-m", branch, cwd=repo_path)

    except subprocess.CalledProcessError as e:
        # Best-effort cleanup: restore original branch, remove temp
        try:
            _run("git", "checkout", branch, cwd=repo_path)
        except Exception:
            pass
        try:
            _run("git", "branch", "-D", temp_branch, cwd=repo_path)
        except Exception:
            pass
        raise GitSquashError(f"Git operation failed: {e.stderr or e}")
