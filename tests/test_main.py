from my_opensource_project.main import MyProject

def test_say_hello():
    project = MyProject()
    assert project.say_hello() == "Hello from My Open Source Project!" 