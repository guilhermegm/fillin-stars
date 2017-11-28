# Fillin Stars

### Requirements

* Python 3.6

### Running

Edit the **env.py** file with your configuration

```
FILE_PATH *input README path*
FILE_OUTPUT_PATH *output the new README path*
GITHUB_TOKEN *https://developer.github.com/v3/auth/#basic-authentication*
REPO_LINE_STARTSWITH *used to help the script finds the repository line (tuple, opcional)*
FILL_REPO_STAR *repository's line modifier, it's a function*
REMOVE_REPO_STAR *before fill the repository details it will to remove if exists (function, opcional)*
FILL_FOOTER_INFO *footer message*
```

Run

```
GITHUB_TOKEN=YOUR_TOKEN python3 fillin-stars.py
```
