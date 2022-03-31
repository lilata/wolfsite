import subprocess
def get_output(cmd):
    cmdl = cmd.strip().split(' ')
    child = subprocess.Popen(cmdl,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    return str(child.stdout.read(), encoding='utf-8')
