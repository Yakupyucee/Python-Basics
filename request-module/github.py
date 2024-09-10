import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = 'TOKEN'#Write a github token
    
    def getUser(self,userName):
        response = requests.get(self.api_url + '/users/' + userName)
        return response.json()

    def getRepositories(self,userName):
        response = requests.get(self.api_url + '/users/' + userName + '/repos')
        return response.json()

    def createRepositories(self,repoName):
        response = requests.post(self.api_url+'/user/repos?access_token='+self.token,json = {
            "name": repoName,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        print(response.status_code)
        return response.json()

github = Github()

while True:
    choice = input('1- Get user \n2- Get repositories \n3- Create repositories \n4- Exit \nChoice : ')
    
    if choice == '4':
        break

    else :
        if choice == '1':
            userName = input('Username : ')
            response = github.getUser(userName=userName)
            print(f'User Name : {response['login']} \nFollowers : {response['followers']} \nFollowing : {response['following']}')


        elif choice == '2':
            userName = input('Username : ')
            response = github.getRepositories(userName=userName)
            for repo in response: 
                print (repo['name'])

        elif choice == '3':
            repoName = input('Enter repositories name : ')
            response = github.createRepositories(repoName = repoName)
            print(response)
        else:
            print('Wrong choice. Try again.')