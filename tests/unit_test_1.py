from paper_trading_1 import get_gym_env_args
from unittest.mock import patch
import gym

def test_hello():
    assert get_gym_env_args(gym.make("LunarLanderContinuous-v2"), if_print=False) == {'env_name': 'LunarLanderContinuous-v2',
 'num_envs': 1,
 'max_step': 1000,
 'state_dim': 8,
 'action_dim': 2,
 'if_discrete': False}


@patch('builtins.print')
def test_print_hello(mock_print):
    get_gym_env_args(gym.make("LunarLanderContinuous-v2"), if_print=False)
    assert mock_print.call_args.args == ({'env_name': 'LunarLanderContinuous-v2',
 'num_envs': 1,
 'max_step': 1000,
 'state_dim': 8,
 'action_dim': 2,
 'if_discrete': False},)