# git-squash

Flatten entire git history to a single commit.

## Install

```
pip install git-squash
```

## Usage

```
git-squash                          # squash current repo
git-squash /path/to/repo            # squash specific repo
git-squash -m "Initial commit"      # custom message
git-squash -b main                  # target branch
git-squash -B e5f1a3b               # squash commits since e5f1a3b
git-squash -B e5f1a3b -m "cleanup"  # squash since a commit with custom message
```

**Warning:** Rewrites git history. Don't use this tool unless you like it for some reason.
