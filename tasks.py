from invoke import task

@task
def build(c, prod=False, tag="gomoku:latest"):
    env = 'production' if prod else 'development'
    c.run(f'docker build --tag {tag} --build-arg "ENV=f{env}" .')

@task(build)
def run(c, tag='gomoku:latest'):
    c.run(f'docker run -p 80:80 {tag})
