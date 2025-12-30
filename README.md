# Auto Typer

A simple Python-based auto-typing application with a GUI, built using `tkinter`, `pyautogui`, and `keyboard`.

## Features
- **Auto Typing**: Type out long text snippets automatically.
- **Adjustable Speed**: (Implied by code structure, currently fixed interval in `pyautogui.typewrite`).
- **Special Keys Support**: Supports tags like `{ENTER}`, `{TAB}`, `{BACKSPACE}`, etc.
- **Simulate Paste**: Option to simulate pasting text instead of typing it character-by-character.
- **Hotkey Trigger**: Start/Stop typing with a configurable hotkey (Default: F6).

## Requirements
- Python 3.x
- `pyautogui`
- `keyboard`

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pyautogui keyboard
   ```
3. Run the application:
   ```bash
   python autotype.py
   ```

## Usage
1. Enter the text you want to auto-type in the "Text" box.
2. Set your desired Hotkey (Default F6).
3. Click "OK" to arm the typist.
4. Switch to your target application and press the Hotkey.

## Building
To build a standalone executable:
```bash
pyinstaller autotype.spec
```
