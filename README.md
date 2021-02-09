# RedmondXP

Windows XP inspired theme for GTK3 developed for XFCE4
![Image Screenshot](https://github.com/matthewmx86/RedmondXP/blob/main/Screenshots/0.png)

## About
The RedmondXP project aims to recreate the nostalgic look of Windows XP for the XFCE4 desktop environment. 

## Extras
Included with the main theme package are the GTK theme, the Xfce4WM theme and the Firefox IE theme.

## Requirements
#### Main theme
The following packages are recommended for full functionality:
```
firefox, xfce4, xfce4-goodies, xfce4-whiskermenu-plugin (included with xfce4-goodies)
```
The theme has been designed for XFCE4 but it is not not required
for the use of the GTK and Firefox themes.  

## Installation

### Downloading theme sources
You can download a copy of the repository by the following command:
```
git clone https://github.com/matthewmx86/RedmondXP.git
```

### Main theme
Make a .themes directory in your home directory if one doesn't exist and extract the RedmondXP.tar.gz archive into 
the ~/.themes directory.
```
mkdir ~/.themes
tar -xvzf RedmondXP.tar.gz -C ~/.themes/
```
The GTK3, Xfce4WM and Metacity-1 themes will now be installed.
It is also recommended to disable GTK overlay scrollbars (autohiding scrollbars in GTK3). The following command
will disable the overlay scrollbars for the current user:
```
export GTK_OVERLAY_SCROLLING=0
```
You may have to log out and back in for the setting to take effect.

### Application menu
Both the XFCE4 application menu button and Whisker Menu buttons are styled and either one can be used. The theme styles
the Whisker Menu window and supports most user configurations, no particular settings are required. 

#### Firefox theme
You will first need to find your firefox user profile directory. It is usually the one that ends with ".default".
To find the correct directory, open a terminal and go to the hidden Firefox directory. Using grep you can view the directories
ending with ".default".
```
cd ~/.mozilla/firefox
ls | grep default
```
In this exmaple I have two directories: one .default and the other .default-release. 
![Image Screenshot](https://github.com/matthewmx86/Redmond97/blob/master/Screenshots/console.png)
If you only have one directory ending with .default that one is the correct profile directory and you can skip
this next step. Otherwise, you can run the following to see which profile is the default.
```
firefox -P
```
You will then see the following window:

![Image Screenshot](https://github.com/matthewmx86/Redmond97/blob/master/Screenshots/firefox.png)

The selected profile is your default profile, in my case it is the default-release profile.

Once you have found the correct profile directory, you will then need to make a directory inside of it called "chrome".
Following my example above you would run the command:
```
mkdir ~/.mozilla/firefox/vugvl4ul.default-release/chrome
```
Now that the chrome directory has been created, you can install the IE theme by copying the Firefox userchrome files into your chrome folder.
The Firefox theme should now be installed and will be activated once you close all Firefox sessions and restart Firefox.

Note: Be sure to enable user stylesheets if you have not enabled this option before:
1. Enable the option "toolkit.legacyUserProfileCustomizations.stylesheets" in the about:config page.

## Known issues
-As of right now GTK3 Libre-Office does not display 100% correctly. Some widgets are off in the preferences 
window and the scrollbar buttons don't use the default theme arrows. There has however, been many additions to the theme for LibreOffice compatibility
and I no longer recommend using the GTK2 workaround for this theme.
-Menus currently are drawn using the same border as the main windows.
-No support for MATE desktop yet, work will begin shortly.
-Untested in Gnome desktop.

## TODO
1. Design or find suitable GTK2 theme to match. (My Win9x theme is currently included for GTK2)
2. Fix issue with menus having the same border as main windows.

## Screenshots
![Image Screenshot](https://github.com/matthewmx86/RedmondXP/blob/main/Screenshots/Screenshot2.png)
![Image Screenshot](https://github.com/matthewmx86/RedmondXP/blob/main/Screenshots/Screenshot1.png)
![Image Screenshot](https://github.com/matthewmx86/RedmondXP/blob/main/Screenshots/Screenshot3.png)
![Image Screenshot](https://github.com/matthewmx86/RedmondXP/blob/main/Screenshots/Screenshot4.png)
