# cbd-sample-rest-app
Cyberbullying Detection sample app using ML model from - https://github.com/Mpak1996/CBDA/tree/main

# Steps to run the app
1. Have Python, Pip installed in local machine
2. Go to the project directory
3. Run `pip install -r requirements.txt`. This installs all project dependencies
4. Start the app using `python cbd.py`
5. Use any Rest client like Postman or Insomnia to test the API. Below is the CURL to import
   `curl --location 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data '{
    "message": "<some text to be replaced>"
}'`
