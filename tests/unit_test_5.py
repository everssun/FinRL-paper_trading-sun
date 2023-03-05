from unittest.mock import patch
from paper_trading_1 import AgentPPO

def test_hello():
    assert AgentPPO.explore_env == "<function __main__.AgentPPO.explore_env(self, env, horizon_len: int) -> [<class 'torch.Tensor'>]>"


@patch('builtins.print')
def test_print_hello(mock_print):
    AgentPPO.explore_env
    assert mock_print.call_args.args == ("<function __main__.AgentPPO.explore_env(self, env, horizon_len: int) -> [<class 'torch.Tensor'>]>",)