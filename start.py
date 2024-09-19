from roboflow import Roboflow
rf = Roboflow(api_key="500UQUX3Vfwfou3TwO7q")
project = rf.workspace("workspace-nyrap").project("dogdetectiontutorial")
version = project.version(1)
dataset = version.download("yolov8")
