import os
import commands

rootdir = "/Users/yi/Developer/source"

def main():
    for f in os.listdir(rootdir):
        path = os.path.join(rootdir, f)
        if os.path.isdir(path):
            print "deal path: " + path
            os.chdir(path)
            dealpath()

def dealpath():
    rst = os.system("git remote -v > /dev/null 2>&1")
    if rst == 0:
        output = commands.getstatusoutput("git status")[1]
        if not "nothing to commit" in output:
            print "\thas commit"
            output = commands.getstatusoutput("git remote -v")
            remote = output[1]
            # TODO: multiy thread
            if "https://github.com/huhuang03/" in remote or "git@gitlab.com:huhuang03" in remote:
                os.system("git add .")
                os.system("git commit -a -m 'auto commit'")
                os.system("git push")
            else:
                print "\tremote: " + remote
        else:
            print "nothing to commit"

if __name__ == "__main__":
    main()
