# Project 4 — OCR System 🔎

## Overview

This project was developed as part of my DecodeLabs Artificial Intelligence Internship.

The project is an Optical Character Recognition (OCR) system that extracts text from an image and evaluates the confidence of the recognized text.

## How It Works

```text
Input Image
    ↓
Load Image
    ↓
Image Preprocessing
    ↓
OCR Recognition
    ↓
Calculate Confidence
    ↓
Display Recognized Text
    ↓
PASS / FAIL Evaluation
```
## Features
-> Image loading
-> Image preprocessing
-> Text extraction using OCR
-> Individual word confidence
-> Average confidence calculation
-> Confidence threshold checking
-> Processed image output
-> PASS / FAIL result

## Technologies Used
-> Python
-> OpenCV
-> Pytesseract
-> Pillow
-> NumPy

## OCR Confidence
- The system uses a confidence threshold of 80%.

- If the average OCR confidence is at least 80%, the result is marked as:
 STATUS: PASS ✓

## Example Result

The test image successfully produced:

Recognized Text:
Artificial Intelligence Project 4 OCR Test

Average Confidence:
95.83%

Confidence Threshold:
80.00%

STATUS: PASS ✓

## What I Learned

This project helped me understand the basic workflow of Optical Character Recognition.

I learned how images can be loaded and preprocessed before sending them to an OCR engine. I also learned how OCR confidence scores can be used to evaluate the quality of recognized text.

The project gave me practical experience working with computer vision libraries and integrating different Python libraries into one application.

## Project Files
File — Project files
Images — Input and related images

## Internship
DecodeLabs Artificial Intelligence Internship — Project 4
