# Simple local deployment: copies the app to a deploy folder and checks
# that the deployed copy works.
import importlib.util
import os
import shutil
import sys

DEFAULT_DIR = os.path.join(os.path.expanduser("~"), "deployments",
                           "jenkins_project")
FILES = ["app.py", "requirements.txt"]


def deploy(deploy_dir):
    os.makedirs(deploy_dir, exist_ok=True)
    for name in FILES:
        shutil.copy(name, deploy_dir)
        print(f"Copied {name} to {deploy_dir}")


def check(deploy_dir):
    path = os.path.join(deploy_dir, "app.py")
    spec = importlib.util.spec_from_file_location("deployed_app", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.greet("World")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR
    deploy(target)
    print("Deployed app output:", check(target))
    print("Deployment finished")
