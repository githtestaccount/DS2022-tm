import gym
import time

env = gym.make('MountainCar-v0')
epic_len = 300
env.reset()

# random action for nonzero initial velocity
obs = env.step(env.action_space.sample())

for step in range(epic_len):

    # strategy ;-)
    if obs[1] < 0:
        action = 0
    else:
        action = 2

    # apply action
    obs, reward, done, info = env.step(action)

    # render
    env.render()
    time.sleep(0.001)

    # restart if done before end of movie
    if done:
        env.reset()

env.close()