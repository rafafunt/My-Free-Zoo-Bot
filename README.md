# My-Free-Zoo-Bot

Automation script for the **My Free Zoo** browser game. The bot controls the game using image recognition and mouse automation to handle daily tasks such as feeding, cleaning and collecting in-game resources.

## Features

- Feed, clean and play with animals automatically.
- Collect money, trash and other items.
- Give stars to friends (supported in Polish and English versions).
- Works with the provided image templates in the `captures/` directory.

## Requirements

- Python 3.x
- [pyautogui](https://pyautogui.readthedocs.io/)
- [python_imagesearch](https://github.com/rafafunt/pythonimagesearch)
- [keyboard](https://github.com/boppreh/keyboard)

Install the required libraries using `pip`:

```bash
pip install pyautogui python_imagesearch keyboard
```

## Usage

1. Launch **My Free Zoo** in your browser and ensure the game window is in focus.
2. Run the script:

   ```bash
   python "Python Code.py"
   ```
3. The bot looks for patterns from the `captures/` folder and performs the corresponding actions. Press `x` while the script is running to exit.

Giving stars requires opening the in-game friends list while the bot is active.

## Disclaimer

The project is provided for educational purposes. Use at your own risk and respect the game's terms of service. The original author of the script is [rafafunt](https://github.com/rafafunt).
