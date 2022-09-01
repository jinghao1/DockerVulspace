import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from rasp.ext import const,scope
from rasp.ext.assess.patch import enable_patches
from rasp.log import logger


def get_policies():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'policy_api.json')
    with open(file_path, 'r') as f:
        policies = json.load(f)
    if policies.get("status", 0) != 201:
        return []
    return policies.get('data', [])


class BaseMiddleware(object):
    loaded = False
    container = "django"

    def __init__(self):
        if BaseMiddleware.loaded:
            return

        start_time = time.time()


        # middleware id
        self.id = id(self)
        self.executor = ThreadPoolExecutor()

        logger.debug("------begin hook-----")
        policies = get_policies()
        enable_patches(policies)


        logger.info("python agent hook open")

        scope.exit_scope()
        BaseMiddleware.loaded = True

        # exit("song end")
