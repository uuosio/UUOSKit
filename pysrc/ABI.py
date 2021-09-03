import json
import logging
from uuoskit import _uuoskit

logger=logging.getLogger(__name__)

def set_contract_abi(account, abi):
    ret = _uuoskit.abiserializer_set_contract_abi(account, abi)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return True

def pack_action_args(contractName, actionName, args):
    ret = _uuoskit.abiserializer_pack_action_args(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def unpack_action_args(contractName, actionName, args):
    ret = _uuoskit.abiserializer_unpack_action_args(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def pack_abi_type(contractName, actionName, args):
    ret = _uuoskit.abiserializer_pack_abi_type(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def unpack_abi_type(contractName, actionName, args):
    ret = _uuoskit.abiserializer_unpack_abi_type(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']