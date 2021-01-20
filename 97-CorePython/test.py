import subprocess

s = subprocess.Popen("python", stdout=subprocess.PIPE, stderr= subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
with s.stdin:
    s.stdin.write(b"import os\n")
    s.stdin.write(b"print(os.environ)")

with s.stdout:
    out = s.stdout.read().decode("GBK")

with s.stderr:
    error = s.stderr.read().decode("GBK")

print(f'out={out}')
print(f'error={error}')
