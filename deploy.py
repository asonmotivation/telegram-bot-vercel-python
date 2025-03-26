import os
import requests
import json

def deploy_to_vercel():
    # Vercel API endpoint
    url = "https://api.vercel.com/v1/deployments"
    
    # Headers for Vercel API
    headers = {
        "Authorization": f"Bearer {os.getenv('VERCEL_TOKEN')}",
        "Content-Type": "application/json"
    }
    
    # Project configuration
    data = {
        "name": "telegram-bot-vercel-python",
        "files": [
            {
                "name": "vercel.json",
                "content": open("vercel.json").read()
            },
            {
                "name": "requirements.txt",
                "content": open("requirements.txt").read()
            },
            {
                "name": "vercel_app/wsgi.py",
                "content": open("vercel_app/wsgi.py").read()
            }
        ],
        "env": {
            "TOKEN": "7970579536:AAHOWQDir-ule9h5WxP2UagXFAL3AlON9UY"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        deployment = response.json()
        print(f"Deployment successful! URL: {deployment['url']}")
        return deployment['url']
    except Exception as e:
        print(f"Deployment failed: {str(e)}")
        return None

if __name__ == "__main__":
    deploy_to_vercel() 