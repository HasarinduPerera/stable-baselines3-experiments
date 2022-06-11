import gym

# Create the environment
env = gym.make('LunarLander-v2')

# Reset the environment
env.reset()

# Sample action
print("sample action:", env.action_space.sample())

# Cbservation space shape
print("observation space shape:", env.observation_space.shape)

# Sample observation
print("sample observation:", env.observation_space.sample())

# Close environment 
env.close()