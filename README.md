# VSC configuration & Python standards

Nebbo believes in writing readable, safe and PEP-compliant Python code.
This repository guides the user how to set up both VSC and a development
environment (a sample DevContainer) to achieve the former. While the Python
version used in this guide is 3.11, this should be extended to any other Python version
you may use (adjusting the libraries' versions accordingly)

## Recommendation

[Cursor](https://www.cursor.com) is built on top of VSC and provides a better development experience because of its greatly improved AI completions and interactions (compared to Copilot). Once VSC code has been set up (and synced with your GitHub user), `cursor` is definitely worth trying since it will be able to automatically import all your extensions and settings from VSC. It can be quickly installed with the executable in Windows or MAC, or in Ubuntu by [downloading the `cursor-*.appImage` binary](https://www.cursor.com/) and:

```bash
sudo apt install libfuse2t64  # for Ubuntu 24.04, in 22.04 is: libfuse2
chmod +x ./cursor-<version>.AppImage
mv cursor-<version>.AppImage /opt/cursor.appimage
```
Then do `sudo vim /usr/share/applications/app.desktop` & add:
```bash
[Desktop Entry]
Name=Cursor
Exec=/opt/cursor.appimage --no-sandbox &
Icon=<PATH-OF-CURSOR-ICON>
Type=Application
Categories=Development;
```
Where `<PATH-OF-CURSOR-ICON>` is the path of the app's `.jpg` icon you have to download from Internet. 

### Important note

It **is important to remind** NOT to [install `fuse` or it may break your system if you have `gnome` installed](https://askubuntu.com/questions/1409496/how-to-safely-install-fuse-on-ubuntu-22-04).

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

### Ruff formatter

![`Ruff` formatter](.assets/formatter.gif)

### PyLance linter

![`PyLance` linter](.assets/linter.gif)

### mypy type checker

![`mypy` type checker](.assets/type-checker.gif)