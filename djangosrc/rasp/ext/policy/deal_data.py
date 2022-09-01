from rasp.ext.tracker import ContextTracker
from rasp.log import logger
from rasp.ext import const,scope,utils
CONTEXT_TRACKER = ContextTracker()


@scope.with_scope(scope.SCOPE_AGENT)
def wrap_data(policy_rule, self_obj=None, result=None, come_args=None, come_kwargs=None):

    context = CONTEXT_TRACKER.current()

    if not utils.needs_propagation(context, policy_rule.node_type):
        return

    if not filter_result(result, policy_rule.node_type):
        return

    if policy_rule.node_type == const.NODE_TYPE_SOURCE:
        context.has_source = True
    print(policy_rule.signature)
    print(come_args)
    # tracking = Tracking(policy_rule)
    # tracking.apply(self_obj, result, come_args, come_kwargs)


def filter_result(result, node_type=None):
    if node_type != const.NODE_TYPE_SINK:
        if utils.is_empty(result) or utils.is_not_allowed_type(result):
            return False

    return True
