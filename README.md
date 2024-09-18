# AutoClicker for Ubuntu on Xorg

Just an automatic clicker for the left button of a mouse.

You can change the toggle key(currently "p") in line 6 of the `autoclicker.py` script.

To run this script you need to install the pynput module :
```bash
sudo apt install python3-pynput
# or
pip install pynput
```

You need to install xdotool if it is not installed :
```bash
sudo apt-get install xdotool
```

Once the script is running, press the toggle key and the auto click will begin.
