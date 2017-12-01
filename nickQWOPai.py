
#adapted from https://github.com/awjuliani/DeepRL-Agents/blob/master/Vanilla-Policy.ipynb
import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np
import gym
import matplotlib.pyplot as plt
from .server import QWOPInputOutput
class Agent():
    def __init__(self, lr, s_size,a_size,h_size):
        #These lines established the feed-forward part of the network. The agent takes a state and produces an action.
        self.state_in= tf.placeholder(shape=[None,s_size],dtype=tf.float32)
        hidden = slim.fully_connected(self.state_in,h_size,biases_initializer=None,activation_fn=tf.nn.relu)
        self.output = slim.fully_connected(hidden,a_size,activation_fn=tf.nn.softmax,biases_initializer=None)
        self.chosen_action = tf.argmax(self.output,0)

        #The next six lines establish the training proceedure. We feed the reward and chosen action into the network
        #to compute the loss, and use it to update the network.
        self.reward_holder = tf.placeholder(shape=[None],dtype=tf.float32)
        self.action_holder = tf.placeholder(shape=[None],dtype=tf.int32)

        self.indexes = tf.range(0, tf.shape(self.output)[0]) * tf.shape(self.output)[1] + self.action_holder
        self.responsible_outputs = tf.gather(tf.reshape(self.output, [-1]), self.indexes)

        self.loss = -tf.reduce_mean(tf.log(self.responsible_outputs)*self.reward_holder)

        tvars = tf.trainable_variables()
        self.gradient_holders = []
        for idx,var in enumerate(tvars):
            placeholder = tf.placeholder(tf.float32,name=str(idx)+'_holder')
            self.gradient_holders.append(placeholder)

        self.gradients = tf.gradients(self.loss,tvars)

        optimizer = tf.train.AdamOptimizer(learning_rate=lr)
        self.update_batch = optimizer.apply_gradients(zip(self.gradient_holders,tvars))

class QWOPai:
    def calcReward():
        qio.currscore / (qio.tickcount + 1) 
    def __init__(self):
        self.qio=QWOPInputOutput()
        self.gamma = 0.99
        self.agent = Agent(lr=1e-2,s_size=4,a_size=2,h_size=8)
        self.episodeTotal=5000 #number of episodes that will run
        self.numEpsInBatch=100 #how long to remember
        self.updateFreq=5 #how long to remember
    def discount_rewards(self, rewards):
        """ take 1D float array of rewards and compute discounted reward """
        discounted_r = np.zeros_like(rewards)
        running_add = 0
        for t in reversed(range(0, rewards.size)): #count backwards
            running_add = running_add * self.gamma + rewards[t]
            discounted_r[t] = running_add
        return discounted_r

    def runAI(self):
        
        tf.reset_default_graph() #Clear the Tensorflow graph.
        init = tf.global_variables_initializer()

        # Launch the tensorflow graph
        with tf.Session() as sess:
            sess.run(init)
            i = 0
            total_reward = []
            total_length = []

            gradBuffer = sess.run(tf.trainable_variables())
            for ix,grad in enumerate(gradBuffer):
                gradBuffer[ix] = grad * 0

            while i < self.episodeTotal:
                s = env.reset() #start one round of the game here
                running_reward = 0
                ep_history = []
                while self.qio.died==True:#game hasn't started restarted
                    a=3; #basically stuck in this loop til died changes
                    
                while self.qio.died==False:
                    #Probabilistically pick an action given our network outputs.
                   a_dist = sess.run(self.agent.output,feed_dict={self.agent.state_in:[s]})
                   a = np.random.choice(a_dist[0],p=a_dist[0])
                   a = np.argmax(a_dist == a)

                    s1,r,d,_ = env.step(a) #Get our reward for taking an action given a bandit.
                    ep_history.append([s,a,r,s1]) #s=prevState, action, reward nextState
                    s = s1
                    # running_reward += r #use fuction for reward
                    running_reward=calcReward();
                    #Update the network.
                ep_history = np.array(ep_history)
                ep_history[:,2] = self.discount_rewards(ep_history[:,2])
                feed_dict={self.agent.reward_holder:ep_history[:,2],
                           self.agent.action_holder:ep_history[:,1],self.agent.state_in:np.vstack(ep_history[:,0])}
                grads = sess.run(self.agent.gradients, feed_dict=feed_dict)
                for idx,grad in enumerate(grads):
                    gradBuffer[idx] += grad

                if i % self.updateFreq == 0 and i != 0:
                    feed_dict=dict(zip(self.agent.gradient_holders, gradBuffer))= sess.run(self.agent.update_batch, feed_dict=feed_dict)
                    for ix,grad in enumerate(gradBuffer):
                        gradBuffer[ix] = grad * 0

                total_reward.append(running_reward)


                #Update our running tally of scores.
                if i % 100 == 0:
                    print(np.mean(total_reward[-100:]))
                    i += 1

    # def step(action):
        
