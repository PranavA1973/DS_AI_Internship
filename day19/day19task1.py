import subprocess

def run_git(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Success: {command}")
        if result.stdout: print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Note/Error on '{command}': {e.stderr.strip()}")

run_git("git checkout feature-viz || git checkout -b feature-viz")


run_git('echo # New Plot File > plots.py')


run_git("git add plots.py")

run_git('git commit -m "Add experimental visualization script"')

run_git("git checkout main")

run_git("git checkout feature-viz")