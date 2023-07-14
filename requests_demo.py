# Requests Library:
import requests


r = requests.get("https://xkcd.com/353/")


print(dir(r))
print(help(r))
print(r.text)  ##returns html
# -------------------------------------------------------------------------------------
# Downloading a picture
r = requests.get("https://imgs.xkcd.com/comics/python.png")
print(r.content)


with open("comic.png", "wb") as f:
    f.write(r.content)
# -------------------------------------------------------------------------------------
# Checking back if the response from website
print(r.status_code)
# http status codes:
# 200 - success
# 300 - redirects
# 400 - client errors (example: no permission)
# 500 - server errors (example: crashed website)
# returns True in cases below 400, False in cases above 400
print(r.ok)


# prints out the headers
print(r.headers)
# -------------------------------------------------------------------------------------
# Advanced features of 'requests' library
#'get' parameters
import requests


# we could have added our parameters manually to the url if we wanted to but,
#'requests' library allows users to add parameters in as a dictionary, hence it leaves no rooms for simple mistakes
payload = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params=payload)


print(r.text)
print(r.url)
# -------------------------------------------------------------------------------------
#'post' parameters ('put' request works same)
import requests


payload = {"username": "Dorry", "password": "ElbaffablE"}
r = requests.post("https://httpbin.org/post", data=payload)


# Returns a json response from the website
print(r.text)
# We can save the response as a dictionary within a variable, via the 'json()' function
r_dict = r.json()
print(r_dict["form"])
# -------------------------------------------------------------------------------------
# Basic authentication & delays, timeouts
import requests


r = requests.get(
    "https://httpbin.org/basic-auth/Dorry/ElbaffablE", auth=("Dorry", "ElbaffablE")
)
print(r.text)


r = requests.get("https://httpbin.org/delay/1", timeout=3)
print(r)
