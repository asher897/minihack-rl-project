import gym
import minihack

env = gym.make("MiniHack-Quest-Hard-v0")
env.render()
state, _ = env.reset()
next_state, reward, done, info = env.step(1)
