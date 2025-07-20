# 🖥️ Tuix: Revolutionize Terminal Interfaces  

**Terminal UI/UX Toolkit for Python Developers**  

## 🚀 Vision  
Tuix is a cutting-edge Python library that transforms terminal applications with powerful UI/UX capabilities, enabling developers to create beautiful, interactive command-line interfaces with ease.  

## ✨ Why Choose Tuix?  
- Modern approach to terminal UI development  
- Comprehensive suite of styling and layout tools  
- Intuitive design for both beginners and experts  
- Lightweight and performance-optimized  

## Key Features  
- Advanced text formatting and styling  
- Precise cursor control and screen management  
- Interactive UI components  
- Smooth animations and visual feedback  
- Cross-platform compatibility  

## 📜 License  
MIT License

Copyright (c) 2025 ABOLFAZL MOHAMMADPOUR

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 🌍 Community & Support  
Join our growing [community](https://t.me/tuixcommunity) of developers contributing to the future of terminal interfaces. Your feedback and contributions help shape Tuix's development roadmap.  
You Can Join Our [Newsletter](https://t.me/tuixnewsletter) For Seeing The Newset News Such As (Changes/BugFixes And More)

And Finally, You Could Show Your Kindness By Supporting Us With One Or Many Of The Way That Are Linked In follwing. Thanks For Everythings😍

### International Peoples
<a href="https://www.buymeacoffee.com/abolfazlmohammadpour" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

<a href='https://ko-fi.com/E1E1EQH5Z' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi5.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

### Iranian Peoples
<a href="https://www.coffeebede.com/abolfazlmohammadpour"><img class="img-fluid" src="https://coffeebede.ir/DashboardTemplateV2/app-assets/images/banner/default-yellow.svg" /></a>

## How To Use Tuix?
**Tuix** Uses **Ansi Escape Sequence** For Changing Your Terminal From A Terrible Text To Looks Like Beautiful. So If You Wanna Use **Tuix**, You Must To Make Sure That Your Terminal Supports **Ansi Escape Sequence**.
Here Are Lists Of Some Famous Terminal Apps That Support **Ansi Escape Sequence**:

- Git Bash Terminal
- Gnome X Based Linux Terminals Like Ubuntu Linux Or RedHat Linux
- PowerShell 

### Insttalling Requirements
- You Should Know **Tuix** Completely Developed Under Python3 Programming Language. So For Using **Tuix** You Must To Install **Python Version 3.10** Or Newer On Your Device.  

- After Installing Your Python You Must To Install **pip** Module On Your Device For Installing **Tuix** From **PyPi**.  

**If You Are Using Debian Base Linux Distro Like Ubuntu Or Mint, You Can Enter The Following Command For Installing Python Version 3.10 And pip Module On Your Device**
```
sudo apt update -y && sudo apt install python3.10 -y && sudo apt install python3-pip -y && sudo apt upgrade -y
```
 Now Your System Is Ready For Intsalling **Tuix**
 For Doing This You Have To Enter The Following Command On Your Terminal
 ```
 sudo pip install tuix
 ```
 If The Above Command Doesn't Work You Can Enter The Following Command
 ```
 sudo python3 -m pip install tuix 
 ```
 Now Everything Is Ready For Using **Tuix** In Your Python Projects. You Can Use **Tuix** In Your Python Projects Like Following
 ```py
 from tuix import tuix
 ```
For Knowing How **Tuix** Works And How To Use **Tuix**'s Functionalities You Could Explore In **example** Directory Of The Projects.

### Tuix In Action
**Tuix** Has A Wide Range Features For Working On Terminal Environments, And We Will Show Some Of The Ability Of **Tuix** In The Following

### Changing ForeGround Color Of Terminal With **Tuix**
Here Is An Examples That Shows How To Change Foreground Color Of A Text In Terminal
```py
from tuix import tuix

def main() -> None:
    print("This Is Default Foreground Color Of Your Terminal")

    # Changing The Foreground Color To Black
    tuix.change_foreground_color(tuix.BLACK_FOREGROUND)
    print("This Is Black Foreground Color")

    # Changing The Foreground Color To Bright Black
    tuix.change_foreground_color(tuix.BRIGHT_BLACK_FOREGROUND)
    print("This Is Bright Black Foreground Color")

    # Changing The Foreground Color To Red
    tuix.change_foreground_color(tuix.RED_FOREGROUND)
    print("This Is Red Foreground Color")

    # Changing The Foreground Color To Bright Red
    tuix.change_foreground_color(tuix.BRIGHT_RED_FOREGROUND)
    print("This Is Bright Red Foreground Color")

    # Changing The Foreground Color To Green
    tuix.change_foreground_color(tuix.GREEN_FOREGROUND)
    print("This Is Green Foreground Color")

    # Changing The Foreground Color To Bright Green
    tuix.change_foreground_color(tuix.BRIGHT_GREEN_FOREGROUND)
    print("This Is Bright Green Foreground Color")

    # Changing The Foreground Color To Yellow
    tuix.change_foreground_color(tuix.YELLOW_FOREGROUND)
    print("This Is Yellow Foreground Color")

    # Changing The Foreground Color To Bright Yellow
    tuix.change_foreground_color(tuix.BRIGHT_YELLOW_FOREGROUND)
    print("This Is Bright Yellow Foreground Color")

    # Changing The Foreground Color To Blue
    tuix.change_foreground_color(tuix.BLUE_FOREGROUND)
    print("This Is Blue Foreground Color")

    # Changing The Foreground Color To Bright Blue
    tuix.change_foreground_color(tuix.BRIGHT_BLUE_FOREGROUND)
    print("This Is Bright Blue Foreground Color")

    # Changing The Foreground Color To Magenta
    tuix.change_foreground_color(tuix.MAGENTA_FOREGROUND)
    print("This Is Magenta Foreground Color")

    # Changing The Foreground Color To Bright Magenta
    tuix.change_foreground_color(tuix.BRIGHT_MAGENTA_FOREGROUND)
    print("This Is Bright Magenta Foreground Color")

    # Changing The Foreground Color To Cyan
    tuix.change_foreground_color(tuix.CYAN_FOREGROUND)
    print("This Is Cyan Foreground Color")

    # Changing The Foreground Color To Bright Cyan
    tuix.change_foreground_color(tuix.BRIGHT_CYAN_FOREGROUND)
    print("This Is Bright Cyan Foreground Color")

    # Changing The Foreground Color To White
    tuix.change_foreground_color(tuix.WHITE_FOREGROUND)
    print("This Is White Foreground Color")

    # Changing The Foreground Color To Bright White
    tuix.change_foreground_color(tuix.BRIGHT_WHITE_FOREGROUND)
    print("This Is Bright White Foreground Color")

    # Reset All Of The Appearance Themes
    tuix.reset_format()


if __name__ == "__main__":
    main()

```

### Changing BackGround Color Of Terminal With **Tuix**
Here Is An Examples That Shows How To Change Background Color Of A Text In Terminal
```py
from tuix import tuix

def main() -> None:
    print("This Is Default Background Color Of Your Terminal")

    # Changing The Background Color To Black
    tuix.change_background_color(tuix.BLACK_BACKGROUND)
    print("This Is Black Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright Black
    tuix.change_background_color(tuix.BRIGHT_BLACK_BACKGROUND)
    print("This Is Bright Black Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Red
    tuix.change_background_color(tuix.RED_BACKGROUND)
    print("This Is Red Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright Red
    tuix.change_background_color(tuix.BRIGHT_RED_BACKGROUND)
    print("This Is Bright Red Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Green
    tuix.change_background_color(tuix.GREEN_BACKGROUND)
    print("This Is Green Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright Green
    tuix.change_background_color(tuix.BRIGHT_GREEN_BACKGROUND)
    print("This Is Bright Green Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Yellow
    tuix.change_background_color(tuix.YELLOW_BACKGROUND)
    print("This Is Yellow Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright Yellow
    tuix.change_background_color(tuix.BRIGHT_YELLOW_BACKGROUND)
    print("This Is Bright Yellow Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Blue
    tuix.change_background_color(tuix.BLUE_BACKGROUND)
    print("This Is Blue Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright Blue
    tuix.change_background_color(tuix.BRIGHT_BLUE_BACKGROUND)
    print("This Is Bright Blue Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Magenta
    tuix.change_background_color(tuix.MAGENTA_BACKGROUND)
    print("This Is Magenta Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright Magenta
    tuix.change_background_color(tuix.BRIGHT_MAGENTA_BACKGROUND)
    print("This Is Bright Magenta Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Cyan
    tuix.change_background_color(tuix.CYAN_BACKGROUND)
    print("This Is Cyan Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright Cyan
    tuix.change_background_color(tuix.BRIGHT_CYAN_BACKGROUND)
    print("This Is Bright Cyan Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To White
    tuix.change_background_color(tuix.WHITE_BACKGROUND)
    print("This Is White Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

    # Changing The Background Color To Bright White
    tuix.change_background_color(tuix.BRIGHT_WHITE_BACKGROUND)
    print("This Is Bright White Background Color", end="")
    # Reset All Of The Applied Appearance Actions To The Default
    tuix.reset_format()
    print()

if __name__ == "__main__":
    main()
```

### Changing Syle Of A Text In Terminal With **Tuix**
Here Is An Examples That Shows How To Change Style Of A Text In Terminal
```py
from tuix import tuix


def main() -> None:
    # Resets All Applied Style From Your Terminal
    tuix.reset_format()
    print("This Is Default Style Of Your Terminal")

    # Will Set Style Of Terminal To Bold
    tuix.set_bold_format()
    print("This Is Bold Style Of Your Terminal", end="")
    # Will Reset Style Of Your From Bold Or Dim To Default
    tuix.reset_bold_format()
    print()

    # Will Set Style Of Your Terminal To Dim
    tuix.set_dim_format()
    print("This Is Dim Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Dim Or Bold To Default
    tuix.reset_dim_format()
    print()

    # Will Set Style Of Your Terminal To Italic
    tuix.set_italic_format()
    print("This Is Italic Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Italic To Default
    tuix.reset_italic_format()
    print()

    # Will Set Style Of Your Terminal To Under Line
    tuix.set_under_line_format()
    print("This Is Under Line Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Under Line To Default
    tuix.reset_under_line_format()
    print()

    # Will Set Style Of Your Terminal To Blink
    tuix.set_blink_format()
    print("This Is Blink Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Blink To Default
    tuix.reset_blink_format()
    print()

    # Will Set Style Of Your Terminal To Reverse
    tuix.set_reverse_format()
    print("This Is Reverse Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Reverse To Default
    tuix.reset_reverse_format()
    print()

    # Will Set Style Of Your Terminal To Hide
    tuix.set_hide_format()
    print("This Is Hide Style Of Your Terminal", end="")
    # Will Reset Style Of Your Terminal From Hide To Default
    tuix.reset_hide_format()
    print()

    # Will Set Style Of Your Terminal To Strike Line
    tuix.set_strike_line_format()
    print("This Is Strike Line Style Of Your Terminal", end="")
    # Will Rset Style Of Your Terminal From Strike Line To Default
    tuix.reset_strike_line_format()


if __name__ == "__main__":
    main()

```









