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
```

**Warning:** Rewrites git history. Don't use this tool unless you like it for some reason.
