import nox

@nox.session(python=["3.11"])
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("coverage", "run", "-m", "pytest", "tests/")
    session.run("coverage", "report")
