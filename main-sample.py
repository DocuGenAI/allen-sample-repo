import json
import requests
from openai import OpenAI
keys = json.load(open('C:/shared/content/config/api-keys/openai.json'))
my_key = keys['team-18']

def main(): 
    print("hello world")
    print(my_key)
    #callOpenAI()
    getGithubFile()

def getGithubFile():
    # https://raw.githubusercontent.com/{username}/{repo name}/{branch}/{path to file}
    username = "abh3hu"
    repo_name = 'awesome-interview-questions'
    branch = 'master'
    path_to_file = "README.md"

    # https://github.com/DopplerHQ/awesome-interview-questions/blob/master/README.md

    fileURL = f"https://raw.githubusercontent.com/{username}/{repo_name}/{branch}/{path_to_file}"
    print("fileURL")
    print(fileURL)


def callOpenAI():
    client = OpenAI(api_key=my_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user",
             "content": "give me the code to get a single file from a public github project repo in python using Request Library"
            }
        ]
    )

    print("### response")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()