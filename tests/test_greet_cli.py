import noodle
import os


def test_output():
    assert noodle.output("sdf") is None


def test_greet():
    os.chdir(os.getcwd() + "/examples")
    stream = os.popen("python greet.py -v")
    assert stream.read() == "Noodle 0.1.2\n"
