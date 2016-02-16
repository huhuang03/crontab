import os
import commands

rootdir = "/Users/yi/Developer/source"

for f in os.listdir(rootdir):
    path = os.path.join(rootdir, f)
    if os.path.isdir(path):
        os.chdir(path)
        rst = os.system("git remote -v > /dev/null 2>&1")
        if rst == 0:
            output = commands.getstatusoutput("git remote -v")
            remote = output[1]
            # TODO: judge should upload
            # TODO: multiy thread
            if "https://github.com/huhuang03/" in remote or "git@gitlab.com:huhuang03" in remote:
                os.system("git add .")
                os.system("git commit -a -m 'auto commit'")
                os.system("git push")

