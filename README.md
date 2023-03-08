# Windows duplex scanning

A simple and lightweight Python3 and tkinter GUI program for scanning double sided documents using Windows Fax and Scan.

When scanning big documents using a flatbed printer windows doesn't offer the option for duplex scanning, meaning that you have to use proprietary printer software OR rename the filenames yourself.


<p align="center">
  <img alt="Screenshot" src="https://user-images.githubusercontent.com/70406237/223801015-7aac8da3-be99-4c3e-a474-d4276ed3c37b.png">
</p>



## Installation

Use the Python package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

```bash
pip install -r requirements.txt
```


## Usage

After you scan both sides of the document, give the program the scanned images directory and the number of pages, the program will automatically reorder the images. You have the option to create PDF file or move the images to a new folder.

A simple way to use this program is to have the executable file (.pyw) in the scanned documents directory and just double clicking it to run, the current directory will be automatically used.


## Requirements
* Python 3.7.3 +
