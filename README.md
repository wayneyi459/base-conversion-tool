# Arbitrary Base Conversion Tool

A Python tool for converting numbers between arbitrary bases (up to base 16) using a recursive algorithm.

## Overview
This project implements a base conversion program that converts a number from any given base into another target base.
The conversion is performed by first converting the input number to decimal, then recursively converting it to the target base.

## Features
- Supports arbitrary base conversion up to base 16
- Converts input numbers from any base to decimal
- Converts decimal numbers to a target base using recursion
- Handles numeric and alphabetic digits (0–9, A–F)

## Technologies
- Python
- Recursion
- Mathematical positional notation

## How It Works
1. Convert the input number from its original base to decimal
2. Recursively divide the decimal number by the target base
3. Map remainders to digits or letters using a predefined symbol sequence

## How to Run
1. Make sure Python is installed
2. Run the program:
   ```bash
   python main.py
