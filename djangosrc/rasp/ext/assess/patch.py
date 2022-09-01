import copy
import sys
from rasp.log import logger
from rasp.ext.assess import common_hook
from rasp.ext.assess import ctypes_hook
from rasp.ext.policy import policy
from rasp.ext import const,scope


class Namespace(object):
    def __new__(cls, *args, **kwargs):
        raise TypeError("Namespace derivatives may not be instantiated")


class Module(Namespace):
    hook = None


@scope.with_scope(scope.SCOPE_AGENT)
def enable_patches(policies):
    if len(policies) == 0:
        return

    has_patched = {}
    num = 1
    for rules in policies:

        if rules['enable'] != 1 or not rules['details']:
            continue

        for item in rules['details']:
            signature = item['value']

            if signature in has_patched:
                continue

            policy_rule = policy.new_policy_rule(rules['type'], item)
            if policy_rule is None:
                continue

            policy_arr = signature.split(".")

            if signature in const.C_API_PATCHES:
                continue
            print(num)
            num = num + 1
            try:
                imp_arr = copy.deepcopy(policy_arr)
                method_name = imp_arr[-1]
                del imp_arr[-1]
                policy_str = ".".join(imp_arr)
                new_module = LazyImportHook(policy_str, [method_name])
                origin_method = getattr(new_module, method_name)
                origin_cls = new_module.origin_module()
                if origin_cls is None:
                    imp_arr = copy.deepcopy(policy_arr)
                    method_name = imp_arr[-1]
                    class_name = imp_arr[-2]
                    del imp_arr[-1]
                    del imp_arr[-1]
                    policy_str = ".".join(imp_arr)
                    new_module = LazyImportHook(policy_str, [class_name])
                    origin_cls = getattr(new_module, class_name)
            except Exception as e:
                imp_arr = copy.deepcopy(policy_arr)
                if imp_arr[0] not in sys.modules:
                    # print(imp_arr[0])
                    continue

                method_name = imp_arr[-1]
                class_name = imp_arr[-2]
                del imp_arr[-1]
                del imp_arr[-1]
                policy_str = ".".join(imp_arr)

                try:
                    new_module = LazyImportHook(policy_str, [class_name])
                    origin_cls = getattr(new_module, class_name)
                except Exception as e:
                    continue

            after_cls = ctypes_hook.magic_get_dict(origin_cls)

            if isinstance(origin_cls, type):
                hooked = ctypes_hook.build_method_patch(origin_cls, policy_rule)
                if hooked is None:
                    continue
                logger.debug("------origin_cls_property------ " + "[" + str(rules['type']) + "]" + signature)
                after_cls[method_name] = hooked
            else:
                logger.debug("------origin_cls_function------ " + "[" + str(rules['type']) + "]" + signature)
                after_cls[method_name] = common_hook.BuildFuncPatch(origin_method, policy_rule)

            has_patched[signature] = True

    ctypes_hook.magic_flush_mro_cache()


class LazyImportHook:
    def __init__(self, module_name, fromlist=None):
        self.module_name = module_name
        self.module = None
        if fromlist:
            self.fromlist = fromlist
        else:
            self.fromlist = []

    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name, globals(), locals(), self.fromlist, 0)

        return getattr(self.module, name)

    def origin_module(self):
        return self.module
