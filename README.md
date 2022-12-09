# Kwikpic

## How to build:

1. Install python 3.10.x, Make sure it's added to the path.
2. open terminal, type:
   ```bash
   pip install pyqt6 Pillow
   ```
3. Git clone or download this zip. Extract it. And CWD to the extracted folder.

   ```bash
   cd <extracted folder>
   ```

4. (Mac Only):
   if you don't have Xcode installed, Download and install **_Command Line tools_** for xcode. You have to download the specific version that matches your os version and you need to have an apple developer account to download this.

   Download **Command Line Tools for Xcode** from [Here](https://developer.apple.com/download/more/)

   If you have Xcode installed, you can skip this.

5. In terminal type:

   1. (Mac)
      ```bash
      pyinstaller --noconsole --name Kwikpic --windowed --clean --onedir --add-data "LOGO/logo.png:." --icon app.ico main.py
      ```
   2. (Windows) if you are on Windows:
      ```bash
      pyinstaller --onefile --name Kwikpic --noconsole --clean --icon=app.ico --add-data "LOGO/logo.png;."  main.py
      ```

6. Open to the **dist** folder and:
   1. Open **Kwikpic.exe** if you are on Windows.
   2. Open **Kwikpic.app** if you are on Mac.
      (If you are on mac, you have to whitelist this app to verify certification by going to **Settings > Security and Privacy > Allow Kwikpic**)
   3. Don't delete the Logo folder and the logo.png file inside it.
