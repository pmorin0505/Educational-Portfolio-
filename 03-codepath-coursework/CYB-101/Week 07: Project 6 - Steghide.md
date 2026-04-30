# Week 7 - Project 6: Steghide and Seek

## Overview
This project used steganography to hide and extract data inside image files using Steghide.

## Tools Used
- steghide
- Linux terminal
- nano
- cat

## Process

### Create Message File
nano message.txt

cat message.txt

### Embed Message into Image
steghide embed -ef message.txt -cf image.jpg

A passphrase was used to secure the hidden data.

### Check Image for Hidden Data
steghide info image.jpg

### Extract Hidden Message
steghide extract -sf image.jpg -xf extracted.txt

cat extracted.txt

## Key Concepts

Steganography: hiding data inside files
Extraction: recovering hidden data using Steghide
File analysis: detecting hidden content inside images

## Cybersecurity Relevance
Steganography is used to:
- Hide data inside files
- Investigate hidden communications
- Analyze malicious payload concealment
- Understand data exfiltration methods

## Reflection
This project demonstrated how data can be hidden inside image files without changing their visible appearance. It reinforced the importance of analyzing file structures in cybersecurity.
