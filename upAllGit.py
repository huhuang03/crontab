import os
import commands
import datetime

rootdir = "/Users/th/source"

print "Begin at " + datetime.datetime.now().strftime('%G-%b-%d %I:%M:%p')

def main():
    i = 1
    for f in os.listdir(rootdir):
        path = os.path.join(rootdir, f)
        if os.path.isdir(path):
            print str(i) + ". deal path: " + path
            i += 1
            os.chdir(path)
            dealpath()
        print "Done!"

def dealpath():
    rst = os.system("git remote -v > /dev/null 2>&1")
    if rst == 0:
        output = commands.getstatusoutput("git status")[1]
        if not "nothing to commit" in output:
            print "\thas commit"
            output = commands.getstatusoutput("git remote -v")
            remote = output[1]
            if "https://github.com/huhuang03/" in remote or "git@gitlab.com:huhuang03" in remote:
                os.system("git add .")
                os.system("git commit -a -m 'auto commit'")
                os.system("git push")
            else:
                index = remote.find("\n", 0, len(remote))
                remote = remote[0: index]
                print "\tremote is not mine, remote: " + remote
        else:
            print "\tnothing to commit"

if __name__ == "__main__":
    main()
