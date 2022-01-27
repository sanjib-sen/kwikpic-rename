# Kwikpic

## How to build:

1. Install python 3.9.x, Make sure it's added to the path.
2. open terminal, type:
```bash
pip install opencv-python, pyqt5, pyqt5-tools
```
3. Git clone or download this zip. Extract it. And CWD to the extracted folder.
(Open Terminal and type cd <extracted folder>)
```bash
cd <extracted folder>
```
4. In terminal type:
    1. (Mac) If you are on mac:
    ```bash
    pyinstaller --noconsole --name Kwikpic --windowed --clean --onefile --add-data "LOGO/logo.png:LOGO" --icon app.ico mac.py
    ```
    2. (Windows) if you are on Windows:
    ```bash
    pyinstaller --onefile --name Kwikpic --noconsole --clean --icon=app.ico --add-data "LOGO/logo.png;LOGO"  windows.py
    ```
5. Open to the **dist** folder and:
    1. Open **Kwikpic.exe** if you are on Windows. 
    2. Open **Kwikpic.app** if you are on Mac. 
    (If you are on mac, you have to whitelist this app to verify certification by going to **Settings > Security and Privacy > Allow Kwikpic**)
    3. Don't delete the Logo folder and the logo.png file inside it. 