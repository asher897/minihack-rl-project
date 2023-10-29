<h1>Minihack Reinformcent Learning Project</h1>
<h2>Reinformcemnt Learning task to train an agent to navigate the Minihack-Quest-hard envrionment</h2>


<p>The goal of this project is to compare the accuracy of different algorithms in navigating the Minihack-Quest-hard envrionment. The two algorithms used here are the Deep Q-Network (DQN) and the Actor-Critic model, an implmentation of a policy gradient method.</p>

<p>For both algorithms the general methodology was as follows
Train the agent on skill acquisation tasks whereby the agent learns certain skills thay will help it navigate the Minihack-Quest-hard envrionment.
Once learned, the agent will attempt to navigate the quest easy and medium environments before attempting the hard environment.</p>

<h2>DQN</h2>


<h2>Actor-Critic</h2>
<p>The Actor-Critic model was implemented. This method follows the approach whereby the actor part of the algorithm chooses the actions to take (the policy) and the critic evaluates the performance of the actor. Each has its own set of weights that are trained to optimize their task.</p>

<p>Policy gradient methods (the actor) make updates to the probability distribution of actions to take whereby the actions with a higher expected reward will have a higher probability value for a state observation. The objective for the actor is to learn a policy that maximizes the cumulative future reward from any given time 't' until the run ends at a terminal time 'T'.</p>

<p>The objective of the critic is to evaluate the policy. It does so by constructing its value function or action-value function. In this case, the action-value (Q-value) was used. Both the actor and critic are initialized with a neural network, each with their own weights.</p>


<h2>Results</h2>
<h3>Actor-Critic</h3>


<h3>DQN</h3>
