import gym


env = gym.make('LunarLander-v2')
env.reset()

for step in range(2000):
	env.render()
	# take random action
	obs, reward, done, info = env.step(env.action_space.sample())
	print(reward, done)

env.close()