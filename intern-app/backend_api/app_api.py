from flask import Flask, render_template , url_for , redirect
from authlib.integrations.flask_client import OAuth
#from flask_github import GitHub


app=Flask(__name__)
oauth=OAuth(app)

'''Global VAriable
app , oauth
'''
'''
client_id , client_secret are specified from the github for registering new OAuth App 
'''
app.config['SECRET_KEY'] = "THIS SECRET"
app.config['GITHUB_CLIENT_ID'] = "ed73e18c78079b56a467"
app.config['GITHUB_CLIENT_SECRET'] ="0d8481fb3591bb8db596e29b10ca04cc6d991f5b"
#gthub = GitHub(app)

github = oauth.register (
    name = 'github',
    client_id = app.config["GITHUB_CLIENT_ID"],
    client_secret = app.config["GITHUB_CLIENT_SECRET"],
    access_token_url = 'https://github.com/login/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://github.com/login/oauth/authorize',
    authorize_params = None,
    api_base_url = 'https://api.github.com/',
    client_kwargs = {'scope': 'user:email'},
)



'''
Definiton: Index Page 
Route: https:<localhost:5000> "doesn't require any extra syntax in url"
Return: render_template
'''
@app.route('/')
def index():
    return render_template('index.html')

'''
Definiton: Github_login uses oauth for signing in using github
Route: https://<localhost>:5000/login/github
Return: return the github authorize page if logged in successfully
'''
@app.route('/login/github')
def github_login():
    github=oauth.create_client('github')
    github_uri=url_for('github_authorize',_external=True)
    github_repo=url_for('repo',external=True)
    return github.authorize_redirect(github_uri)
    #return github.repo(github_repo)
'''
Definiton: Github Authorize page prompt after the login is successful
Route: https:/<localhost>:5000/login/github/authorize
Return: Return the User details in Dictionary Format
'''
@app.route('/login/github/authorize')
def github_authorize():
    github=oauth.create_client('github')
    token=github.authorize_access_token()
    resp=github.get('user').json()
    return resp

"""
Definiton: Github Repositiries shown after successful login and authorization
Route: https://<localhost>:5000/repo
Return : Return the user repositires info in dictionary format.
"""
@app.route('/repo')
def repo(resp):
    #resp=github_authorize()
    url = api_base_url + '/users/{username}/repos?per_page=500'.format(username=resp['login'])
    repo_info = []
    for each_repo in resp:
        repo_dict = {}
        repo_dict['repo_name'] = each_repo['full_name']
        repo_dict['repo_link'] = each_repo['html_url']
        repo_dict['description'] = each_repo['description']
        repo_dict['owner_fullname'] = each_repo['owner']['login']
        repo_dict['html_url'] = each_repo['html_url']
        repo_info.append(repo_dict)
    return repo_info


if __name__=='__main__':
    app.run(debug=True)