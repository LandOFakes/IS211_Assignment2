# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-2KV2yE_AXL08s-GwGqjpUbVXmAFLYh2
"""

#Assignment 2

import argparse
import urllib.request
import logging
from datetime import datetime

logging.basicConfig(filename="error.log", level=logging.ERROR,format="%(message)s")
def download_data(url):
  response = urllib.request.urlopen(url)
  return response.read() .decode('utf-8')

def process_data(csv_data):
  person_data = {}
  lines = csv_data.strip() .split ("\n")
  for line_num, line in enumerate(lines[1:], start=2):
    try:
      parts = line.split(",")
      if len(parts) != 3:
        raise ValueError("Incorrect number of fields")
        id_ = int(parts[0])
        name = parts[1].strip()
        birthday_str = parts[2].strip()
        birthday_str = birthday_str.replace("*","/").replace("-","/")
        birthday_date = datetime.strptime(birthday_str, "%d/%m/%y").date()
        person_data[id_] = (name, birthday_date)
    except Exception as e:
        logging. error(f"Error processing line #{line_num} for ID {parts[0] if 'parts' in locals() and parts else 'Unknown'}: {e}")
  return person_data
def display_person(id_,person_data):
    if id_ in person_data:
        name, birthday = person_data[id_]
        print(f"person #{id_} is {name} with a birthday of {birthday}")
    else:
      print("No user found with that ID")
def main() :
                  parser = argparse.ArgumentParser()
                  parser.add_argument("--url", required=True, help="URL to CSV file", default="https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv")
                  args = parser.parse_args(args=['--url','https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv']if get_ipython()else None)
                  try:
                      csv_data = download_data(args.url)
                  except Exception as e:
                        print (f"error downloading data: {e}")
                        return
                  person_data = process_data(csv_data)
                  while True:
                    try:
                      user_input = int(input("Enter an ID to lookup:"))
                      if user_input <= 0:
                          break
                          display_person(user_input, person_data)
                    except ValueError:
                          print("Please enter a valid integer ID.")
if __name__ == "__main__":
    main()



