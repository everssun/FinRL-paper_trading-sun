from paper_trading_1 import get_gym_env_args
from unittest.mock import patch
import gym

def test_hello():
    assert get_gym_env_args(gym.make("FrozenLake-v1"), if_print=False) == {'env_name': 'FrozenLake-v1',
 'num_envs': 1,
 'max_step': 100,
 'state_dim': (),
 'action_dim': 4,
 'if_discrete': True}


@patch('builtins.print')
def test_print_hello(mock_print):
    get_gym_env_args(gym.make("FrozenLake-v1"), if_print=False)
    assert mock_print.call_args.args == ({'env_name': 'FrozenLake-v1',
 'num_envs': 1,
 'max_step': 100,
 'state_dim': (),
 'action_dim': 4,
 'if_discrete': True},)