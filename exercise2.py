import gymnasium as gym

# Create the environment (no rendering for speed)
env = gym.make("FrozenLake-v1")

num_episodes = 1000
rewards_per_episode = []

for episode in range(num_episodes):
    observation, info = env.reset()
    terminated, truncated = False, False
    episode_reward = 0.0

    while not terminated and not truncated:
        # Take a random action
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        # Update reward
        episode_reward += reward

    # Store the total reward for this episode
    rewards_per_episode.append(episode_reward)

# Calculate average reward over all episodes
average_reward = sum(rewards_per_episode) / num_episodes
print(f"Average reward over {num_episodes} episodes: {average_reward:.4f}")

# Close the environment
env.close()
