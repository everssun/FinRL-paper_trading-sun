from paper_trading_1 import AgentBase, AgentPPO, Config, get_gym_env_args
from unittest.mock import patch
import gym

agent_class = AgentPPO
env_class = gym.make
env_args = get_gym_env_args(env=gym.make('LunarLanderContinuous-v2'), if_print=True)

def test_hello():
    assert Config(agent_class, env_class, env_args) == '<__main__.Config at 0x7fd1b5a73bb0>'


@patch('builtins.print')
def test_print_hello(mock_print):
    Config(agent_class, env_class, env_args)
    assert mock_print.call_args.args == ('<__main__.Config at 0x7fd1b5a73bb0>',)