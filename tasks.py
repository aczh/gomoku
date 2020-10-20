from invoke import task

@task
def build(c, prod=False):
    env = 'production' if prod else 'development'
    c.run(f'docker build --tag gomoku:latest --build-arg "ENV=f{env}" .')

@task(build)
def run(c):
    c.run(f'docker run -p 80:80 gomoku:latest')
