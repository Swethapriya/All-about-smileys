import twitter

api = twitter.Api(consumer_key='ixSJS9ZdWg557X61nCo3LBI0X',
consumer_secret='W7qOlh1OBqd7kA4bZFRM5ZlgWTYV2gTDDuJWQdGNhO1nrDbO2r',
access_token_key='2354690352-tEK26HCzhIutNTc88m2QZ2PIFkylIxxhvi7oEDi',
access_token_secret='Dubgmq88BUj0yhmRhirOChG0hY5qgNR8YMcxBaWnXi9TY')

print(api.VerifyCredentials())
help(api)