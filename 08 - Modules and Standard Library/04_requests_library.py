# Requests library allows users to make HTTP requests, to access information from websites.
# Even though it is a third party software component, requests library has been recommended in the python's documentation.
# The package is installed via the command prompt using pip.
# Within the terminal users just need to type in 'pip install requests'.


# Has the functionality to get information from websites, post information to websites, download images, follow redirects etc...
# So it's basically great for accessing the information, but not so great for parsing that information...
# Other libraries like 'requests-html' could be useful when the goal is to parse the data.


# Accessing the contents of a website:
import requests


r = requests.get(
    "https://xkcd.com/353/"
)  # URL address of the antigravity python webcomic.


print(r)  # Returns the response of the web page of the URL.


print(dir(r))  # Returns the attributes and methods for the object.
print(help(r))  # More detailed explanations of the attributes and methods.


print(r.text)  # Returns the html. (Content of the response in unicode)


# Downloading a picture:
r = requests.get(
    "https://imgs.xkcd.com/comics/python.png"
)  # URL address of the image specifically.
print(r.content)  # Returns in the form of bytes. (Content of the response in bytes)


# Grabbing the bytes and saving them to a file in the operating system:
with open("comic.png", "wb") as f:
    f.write(
        r.content
    )  # Creating the picture within local files, using content of the response in bytes.


print(r.status_code)
"""
http status codes:
200 - success
300 - redirects
400 - client errors (example: no permission)
500 - server errors (example: crashed website)
"""


print(r.ok)  # Response returns True in cases below 400, False in cases above 400.
print(r.headers)  # Prompts out the headers that has more in-depth response information.


# Advanced features of 'requests' library:
# https://httpbin.org allows users to test different http methods, redirects and authentication etc...


# 'get' parameters:
import requests


# It is possible to add parameters manually to the URL:
# r = requests.get("https://httpbin.org/get?page=2&count=25")


# But the requests library allows users to add parameters in as a dictionary, and leaves no room for simple mistakes.
payload = {"page": 2, "count": 25}  # Dictionary of those parameters.
r = requests.get(
    "https://httpbin.org/get", params=payload
)  # Passing in the parameters as an additional argument.


print(r.text)  # Returns the response from httpbin website.
print(r.url)  # Returns the URL.


# 'post' parameters:
import requests


# Posting username and password informations to the website as a dictionary:
payload = {"username": "Dorry", "password": "ElbaffablE"}
r = requests.post("https://httpbin.org/post", data=payload)


print(r.text)  # Returns a json response from the website.


# Users may save the json response as a dictionary within a variable, via the 'json()' function:
r_dict = r.json()  # Creating a python dictionary from that json response.
print(r_dict["form"])  # Accessing the 'form' key of the dictionary.


# Basic authentication & delays, timeouts:
import requests


# Passing credentials for basic authentication:
r = requests.get(
    "https://httpbin.org/basic-auth/Dorry/ElbaffablE", auth=("Dorry", "ElbaffablE")
)  # 'auth' is set to be a tuple that has username and password values.
print(r.text)


# Requests will wait indefinitely, in cases where no response comes from the page that it's trying to access.
# Setting a timeout with an additional parameter:
r = requests.get(
    "https://httpbin.org/delay/1", timeout=3
)  # Adding in one second delay and waiting three seconds before timing out.
print(r)
