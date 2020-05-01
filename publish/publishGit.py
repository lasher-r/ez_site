from datetime import datetime
import sh

class GitPublish:

    def __init__(self, path, remote):
        self.remote = remote
        self.git = sh.git.bake(_cwd=path)
        self._init_git()
        self.set_remote()

    def _init_git(self):
        try:
            status = self.git.status()
            return status
        except sh.ErrorReturnCode_128 as e:
            init = self.git.init()
            self._init_git()

    def add_all(self):
        return self.git.add('.')

    def add_and_commit(self):
        self.add_all()
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        try:
            self.git.commit(m=dt_string)
        except sh.ErrorReturnCode_1:
            return 'nothing to commit'

    def set_remote(self):
        try:
            self.git.remote.add.origin(self.remote)
        except sh.ErrorReturnCode_128 as e:
            set_url = self.git.remote.bake('set-url')
            cmd = set_url.origin(self.remote)
            print(cmd)
        
        return self.git.remote('-v')

    def push(self):
        cmd = self.git.push.bake('-u').bake('--force')
        print(cmd)
        return cmd.origin('master')

    def publish(self):
        self.add_and_commit()
        self.push()

if __name__ == "__main__":
    remote = 'git@github.com:lasher-r/lasher-r.github.io.git'
    publisher = GitPublish('/tmp/pn', remote)
    publisher.publish()