from invoke import task

@task
def build(c):
    c.run('docker build --tag gomoku:latest .')

@task
def run(c):
    c.run('docker run -p 80:80 gomoku:latest')
