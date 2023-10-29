import random
import nle
import gym
import minihack

env = gym.make("MiniHack-Quest-Hard-v0")
state = env.reset()
env.render(mode="human")
for i in range(10000):
    action = random.randint(0, env.action_space.n-1)
    next_state, reward, done, info = env.step(action)
    env.render(mode="human")
