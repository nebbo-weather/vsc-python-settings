# VSC configuration & Python standards

Nebbo believes in writing readable, safe and PEP-compliant Python code.
This repository guides the user how to set up both VSC and a development
environment (a sample DevContainer) to achieve the former. While the Python
version used in this guide is 3.11, this should be extended to any other Python version
you may use (adjusting the libraries' versions accordingly)

## Guide

The main tools & extensions to use can be distinguised amongst:
- Formatting: `Ruff`
- Linting: `Pylance` (& `Ruff`)
- Type hinting: `mypy` (& `Pylance`)

Let's set them up:
- [ ] Configure your Python environment throught the `pyproject.toml`
    - At you will see, not only the `mypy` & `ruff` servers are installed, but also some libraries' stubs (necessary for mypy) such as: `pandas-stubs`, `types-tqdm`, `scipy-stubs`
    - Note that `ruff` can be applied to the entire package from CLI by runnning:
    ```bash
    ruff check --fix src/testapp/
    ```
    Some more "unsafe" fix can be automatically performed with: `ruff check --fix --unsafe-fixes src/testapp/`
- [ ] Create a `.mypy.ini` to adjust some `mypy` settings:
    - Some libraries' stubs are not available or incomplete and `mypy` will complain. This can be avoided with:
    ```.mypy.ini
    [mypy-xskillscore.*]
    ignore_missing_imports = True
    ```
    - Also it is advisable to enable untyped defs.' checks with:
    ```.mypy.ini
    [mypy]
    check_untyped_defs = True
    ```   
    - **Note** you can locally disable the type checker for in a specific line commenting `# type: ignore`
- [ ] Install the corresponding VSC extensions in the `.devcontainer/devcontainer.json` file
    - In general, you will want to have the same extensions as locally. You can run:
    ```bash
    code --list-extensions | sed -e 's/^/    "/' -e 's/$/",/' | sed '$ s/,$//' > extensions.txt
    ```
    to create an extesions' list.
- [ ] Finally, adjust your global VSC user's settings `.json`. In my case, I recommend:
    ```.json
    {
        // # Aesthetic & personal preferences
        "workbench.colorTheme": "Dracula Theme",
        "workbench.tree.indent": 20,
        "window.zoomLevel": 1,
        "editor.fontSize": 14,
        // "editor.rulers": [78, 120],
        "editor.minimap.renderCharacters": false,
        "editor.minimap.size": "fill",
        "editor.cursorStyle": "block-outline",
        "editor.cursorBlinking": "smooth",

        // # Auto-save feature
        "files.autoSave": "afterDelay", 
        "files.autoSaveDelay": 1000,  // after 1 second

        // # Python settings
        "[python]": {
            "editor.codeActionsOnSave": {
                "source.organizeImports": "always",
                "source.fixAll": "always",
            },
            "editor.defaultFormatter": "charliermarsh.ruff",
            "editor.formatOnSave": true,  
        },
        "python.analysis.typeCheckingMode": "basic",
        "python.languageServer": "Pylance",

        // # Other settings
        "git.confirmSync": false,
        "redhat.telemetry.enabled": false,
        "explorer.confirmDragAndDrop": false,
    }
    ```
    Even though those before the `# Auto-save feature` comment are purely personal preferences.

## Usage example

### `Ruff` formatter

![`Ruff` formatter](.assets/formatter.gif)

### `PyLance` linter

![`PyLance` linter](.assets/linter.gif)

### `mypy` type checker

![`mypy` type checker](.assets/type-checker.gif)