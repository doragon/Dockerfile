import docker
import logging
import logging.config
import sys
from string import Template


class DockerClient:

    def __init__(self):
        logconfigpath = '/var/workspace/logger_config.ini'
        base_url = 'tcp://xxx.xxx.xxx.xxx:4243'
        version = '1.12'

        logging.config.fileConfig(logconfigpath)
        self.logger = logging.getLogger(__name__)
        self.logger.info('[DockerClient.__init__]')
        try:
            self.dockerc = docker.Client(
                base_url=base_url,
                version=version,
                timeout=10
            )
        except Exception as e:
            self.logger.error('=== output error ===')
            self.logger.error('type:' + str(type(e)))
            self.logger.error('args:' + str(e.args))
            self.logger.error('message:' + str(e.message))
            self.logger.error('Exception as e:' + str(e))


    def build(self, workpath, tag):
        self.logger.info('[DockerClient.build]')
        result = self.dockerc.build(path=workpath, tag=tag, rm=True)
        result = list(result)[-1]
        self.logger.info(result)
        imageid = None
        if 'Successfully built' in result:
            imageid = result.replace('{"stream":"Successfully built', '').replace('\\n"}', '')
        else:
            self.logger.error('Failed to build')
        return {'Id': imageid, 'Repository': tag}


    def images(self, name=None, quiet=False, all=False):
        self.logger.info('[DockerClient.images]')
        images = self.dockerc.images()
        res = []
        if name:
            for img in [imgs for imgs in images if name in imgs['RepoTags'][0].split('/')[0]]:
                res.append(img['RepoTags'])
        return res


    def push(self, repository):
        self.logger.info('[DockerClient.push]')
        res = [line for line in self.dockerc.push(repository=repository, stream=True, insecure_registry=True)]
        self.logger.info(res)
        if 'error' in list(res)[-1]:
            self.logger.error('Failed to push')
            res = None
        return res


if __name__ == '__main__':
    dockerc = DockerClient()
    argvs = sys.argv
    if len(argvs) != 4:
        dockerc.logger.error('Usage: # python %s filename' % argvs[0])
        exit()

    dockerc.logger.info('workpath = ' + argvs[1])
    dockerc.logger.info('tag = '      + argvs[2])
    dockerc.logger.info('registry = ' + argvs[3])

    repository = argvs[3] + '/' + argvs[2]
    res = dockerc.build(workpath=argvs[1], tag=repository)
    if res['Id'] is None:
        raise Exception, 'Build failure!'
    res = dockerc.push(repository)
    if res is None:
        raise Exception, 'Push failure!'
