# ML_practicals1
# Reinforcement Learning Practical: CartPole-v1 and FrozenLake-v1

##  Summary
CartPole-v1 and FrozenLake-v1 were the two environments I investigated in this practical.  
In **CartPole**, I made and initialized the environment, looked at its action and observation spaces, and then used a loop to render the movements and execute one episode with random actions.  

In **FrozenLake**, I created a random agent that played 1000 episodes, recorded the rewards, and determined the average reward.  

Through these tasks, I gained a better understanding of how agents interact with their surroundings and how performance is evaluated in reinforcement learning environments.

##  Exercise 1: CartPole Environment

The CartPole environment has a **discrete action space** with two possible actions:  
- `0` → Push the cart to the left  
- `1` → Push the cart to the right  

Its **observation space** is continuous and consists of four values:  
1. Pole angle  
2. Pole angular velocity  
3. Cart position  
4. Cart velocity  

These values describe the state of the system at each timestep. Running the loop with random actions showed the instability of the pole without a proper strategy, highlighting the importance of learning in reinforcement learning.

##  Exercise 2: FrozenLake Random Agent

I set up a random agent in **FrozenLake-v1** to play **1000 episodes**. Rewards were collected as the agent performed random actions in each episode.  

The random agent performed poorly, achieving an **average reward of roughly 0.02**, since the environment is slippery and completing the goal requires careful planning.  

This result demonstrates that in environments where rewards are sparse and the path to the objective is uncertain, random actions are ineffective.

##  Challenges

Understanding and managing the **`step()` function's outputs**—the next observation, reward, termination status, truncation status, and additional information—was the most difficult aspect of this practical.  

It also required some effort to set up the environment with correct rendering. Additionally, **FrozenLake** was challenging because rewards were infrequent, making it difficult to track progress and requiring patience when running multiple episodes.

##  Key Takeaways

The main takeaway from this exercise is that in reinforcement learning contexts, **random agents are insufficient** to achieve decent performance. While random actions are useful for testing and getting familiar with the environment, successful agents require strategies that make efficient use of the **observation space**.  

I also realized how crucial it is to understand both the **action space** and the **observation space**, as they define the agent’s capabilities and the information it can use to learn.  

Overall, this exercise gave me a clearer understanding of how reinforcement learning operates and highlighted the importance of careful agent design.



