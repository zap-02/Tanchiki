import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='tank-v0',
    entry_point='gym_foo.envs:FooEnv',
)
