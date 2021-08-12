# Windows duplex scanning

A simple and lightweight Python3 and tkinter GUI program for scanning double sided documents using Windows Fax and Scan.

When scanning big documents using a flatbed printer windows doesn't offer the option for duplex scanning, meaning that you have to use proprietary printer software OR rename the filenames yourself.

<p align="center">
  <img width="396" alt="Screenshot" src="https://user-images.githubusercontent.com/70406237/129221562-eb0475bb-18d7-440f-9606-7bf57be857d4.png">
</p>


## Installation

Use the Python package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

```bash
pip install -r requirements.txt
```


## Usage

After you scan both sides of the document, give the program the scanned images directory and the number of pages, the program will automatically reorder the images. You have the option to create a new file and move the images there.

A simple way to use this program is to have the executable file (.pyw) in the scanned documents directory and just double clicking it to run, the current directory will be automatically used.


## Requirements
* Python 3.7.3 +
