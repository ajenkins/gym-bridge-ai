from gym.envs.registration import register

register(
    id='bridge-v0',
    entry_point='gym_bridge.envs:BridgeEnv',
)