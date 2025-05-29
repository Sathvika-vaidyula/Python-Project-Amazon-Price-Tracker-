# Python-Project-Amazon-Price-Tracker-

#
# Welcome to Amazon Price Tracker — a Python bot that tracks the price of an Amazon product
# and alerts you via email or SMS when the price drops below your target.
# Perfect for anyone who shops online and wants to never miss a deal!
#
# -------------------------------------------------------------------------------
#
# Project Overview
#
# Online shopping is convenient, but prices fluctuate a lot, sometimes daily.
# This project automates monitoring the price of a product on Amazon so you don’t have to check manually every day.
#
# For example, I've been eyeing an Instant Pot Duo Plus 9-in-1 — a versatile pressure cooker
# that can do everything from slow cooking to baking cakes. Its price varies frequently,
# and I want to buy it when it drops below $100.
#
# This bot:
# - Scrapes the product page to get the current price.
# - Compares it to your target buy price.
# - Sends you an alert via email or SMS when the price is right.
#
# -------------------------------------------------------------------------------
#
# How It Works
#
# 1. You provide the URL of the Amazon product you want to track.
# 2. The script scrapes the webpage to extract the current price.
# 3. It converts the price to a float and compares it with your target price.
# 4. If the current price is lower, the bot sends you a notification email or SMS.
# 5. You get the alert and can buy the product immediately without constantly checking manually.
#
# -------------------------------------------------------------------------------
#
# Features
#
# - Web scraping with BeautifulSoup to parse Amazon product pages.
# - Price extraction and float conversion.
# - Email or SMS notifications using SMTP or Twilio.
# - Can be scheduled to run daily (e.g., using cron or Windows Task Scheduler).
#
# -------------------------------------------------------------------------------
#
# Requirements
#
# - Python 3.x
# - requests library
# - beautifulsoup4 library
# - smtplib (built-in) for email alerts OR twilio for SMS alerts
# - python-dotenv (optional, for managing sensitive credentials)
#
# -------------------------------------------------------------------------------
#
# Installation
#
# 1. Clone this repository:
#    git clone https://github.com/yourusername/amazon-price-tracker.git
#    cd amazon-price-tracker
#
# 2. Install dependencies:
#    pip install -r requirements.txt
#
# 3. Set up environment variables for your email or Twilio credentials securely:
#
#    Create a `.env` file in the root folder with your secrets (do NOT commit this file):
#    SMTP_ADDRESS=smtp.gmail.com
#    EMAIL_ADDRESS=your_email@gmail.com
#    EMAIL_PASSWORD=your_email_password_or_app_password
#    TWILIO_ACCOUNT_SID=your_twilio_sid
#    TWILIO_AUTH_TOKEN=your_twilio_auth_token
#    TWILIO_NUMBER=+1XXXXXXXXXX
#    YOUR_PHONE_NUMBER=+91XXXXXXXXXX
#
# -------------------------------------------------------------------------------
#
# Usage
#
# Edit the script main.py to update:
# - The product URL you want to track.
# - Your target buy price.
# - Notification method (email or SMS).
#
# Run the script:
#    python main.py
#
# -------------------------------------------------------------------------------
#
# Scheduling
#
# To automate daily checks, schedule the script using:
# - Cron (Linux/macOS)
# - Task Scheduler (Windows)
#
# -------------------------------------------------------------------------------
#
# Notes
#
# - For Gmail SMTP, use an App Password if you have two-factor authentication enabled.
# - Amazon may block scrapers; consider rotating user agents or adding delays.
# - Keep your credentials secure, never upload `.env` files or secrets to public repos.
#
# -------------------------------------------------------------------------------
#
# License
#
# This project is open-source and free to use.
#
