# ImagesToPDF
A small and simple script to convert a set of images to a pdf file

# Examples
You can find the attached python script `img2pdf.py`

Let's say you have a bunch of images in `/home/user/Pictures/lecture-slides/` and you want to generate a pdf out of these files say `/home/user/Documents/lecture-slides/slides.pdf` then you can run the script as follows:

```python3 img2pdf.py /home/user/Pictures/lecture-slides/ /home/user/Documents/lecture-slides/slides.pdf```

# Dependencies
The script depends on the following packages/modules: "fpdf, PIL, os, sys, glob, threading"  
All the modules are self-bundled with python3 except fpdf which you can install as follows:  
```sudo apt install python3-pip```
```pip3 install fpdf```


# Advanced Options
In case if you want to restrict only some of the images to be a part of pdf e.g. `*.jpg` and `.*png` only then you can edit the script to just keep those extensions

# Contact
Feel free to contact `shubhampanchal9773@gmail.com` for any suggestions or help you need. 
