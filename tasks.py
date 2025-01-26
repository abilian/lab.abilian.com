from invoke import task

USER = "web"
HOST = "lab.abilian.com"
PATH = "/srv/web/lab.abilian.com"


# HOST = "trunks3.abilian.com"
# PATH = "/home/web/lab.abilian.com/"

@task
def deploy(c):
    c.run(f"rsync -e ssh --delete-after -avz site/ {USER}@{HOST}:{PATH}/")
