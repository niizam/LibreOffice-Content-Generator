# LibreOffice AI Content Generator

This is simple python macro script for LibreOffice to help you generate content from selected words/sentences with AI for free.  
## Demo
![loai](https://github.com/niizam/LibreOffice-Content-Generator/assets/45286708/34f1b848-f1fa-4508-aecf-28776dad9062)

## Requirements
- [APSO (Alternative Python Script Organizer)](https://extensions.libreoffice.org/en/extensions/show/apso-alternative-script-organizer-for-python), download [APSO here](https://extensions.libreoffice.org/assets/downloads/508/1663087602/apso.oxt)
- Python Modules;
    - asyncio
    - baichat-py (0.2.2)
```bash
sudo pip install asyncio baichat-py==0.2.2
```
- Little knowledge of LibreOffice macros and python

## Usage
- Open LibreOffice Writer
    - Select Tools → Extension Manager from the menu bar.
    - In the Extension Manager dialog (Figure 2)
    - click Add and select [apso.oxt](https://extensions.libreoffice.org/assets/downloads/508/1663087602/apso.oxt)
- Copy and paste `LibreOffice_AI.py` to `$HOME/.config/libreoffice/4/user/Scripts/python`.
- Write a sentences, select it, then run macro.

## Need Help to Improve 
- [ ] Add loading dialog or progressbar while macro waiting respons
- [ ] Convert this script as extension(?)

## Disclaimers
- Do with your own risk, i give no any warranty with this script, ('-_-').
- I just test this macros on Ubuntu Linux (22.04) with latest LibreOffice (7.5.3.2), i can't sure this macro can run every where. Please ping me on ticket issue if you can run this macro on your operating system.
