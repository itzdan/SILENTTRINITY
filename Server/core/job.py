import json
from core.utils import gen_random_string


class Job:
    def __init__(self, command=None, module=None):
        self.id = gen_random_string()
        self.status = 'initialized'
        self.command = command
        self.module = module

    def payload(self):
        payload = {'id': self.id}

        if self.command:
            payload['cmd'], payload['args'] = self.command

        elif self.module:
            payload['cmd'] = 'run_ipy_script' if self.module.language == 'ipy' else 'run_boo_script'
            payload['args'] = self.module.payload()

        return json.dumps(payload).encode()
