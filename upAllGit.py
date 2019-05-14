import os
import datetime
import subprocess
import re

rootdir = ["/Users/th/source", "/Users/th"]

print("Begin at " + datetime.datetime.now().strftime('%G-%b-%d %I:%M:%p'))

def run_shell(shell):
    return subprocess.run(shell, stdout=subprocess.PIPE).stdout.decode('utf-8')

def is_git_directory(path = '.'):
    return subprocess.call(['git', '-C', path, 'status'], stderr=subprocess.STDOUT, stdout = open(os.devnull, 'w')) == 0

def syncMMDbAndMMXp():
    os.system("rsync -av --delete ~/source/mm-tools/mmdb ~/source/MMdb/")
    os.system("rsync -av --delete ~/source/mm-tools/mmxp ~/source/MMxp/")

def main():
    # syncMMDbAndMMXp()
    i = 1
    for rd in rootdir:
        for f in os.listdir(rd):
            path = os.path.join(rd, f)
            if os.path.isdir(path) and os.access(path, os.W_OK):
                i += 1
                os.chdir(path)
                dealpath(path)

def dealpath(path):
    reg1 = re.compile('origin\s*https://(github|gitlab).com/huhuang03/')
    reg2 = re.compile('origin\s*git@(github|gitlab).com:huhuang03')
    if is_git_directory(path):
        print(f"handel project: {path}")
        output = run_shell(['git', 'status'])
        rst = os.system("git remote -v > /dev/null 2>&1")
        if rst == 0:
            if not "nothing to commit" in output:
                print("has commit")
                remote = run_shell(["git", "remote", '-v'])
                if reg1.search(remote) or reg2.search(remote):
                    os.system("git add .")
                    os.system("git commit -a -m 'auto commit'")
                    os.system("git push")
                else:
                    index = remote.find("\n", 0, len(remote))
                    remote = remote[0: index]
                    print("remote is not mine, remote: " + remote)
            else:
                print("nothing to commit")
        print("Done\n")

if __name__ == "__main__":
    main()
