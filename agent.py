import tensorflow as tf
import numpy as np
import gym
import math
import os

import model
import architecture as policies
import gumball_lite_environ as env

# SubprocVecEnv creates a vector of n environments to run them simultaneously.
from baselines.common.vec_env.subproc_vec_env import SubprocVecEnv
from baselines.common.vec_env.dummy_vec_env import DummyVecEnv
from tensorflow.keras import backend as K


def main():
	config = tf.ConfigProto()

	# Avoid warning message errors
	os.environ['CUDA_VISIBLE_DEVICES'] = '0'

	# Allowing GPU memory growth
	config.gpu_options.allow_growth = False
	K.clear_session()

	with tf.Session(config=config):
		model.learn(policy=policies.PPOPolicy,
							env=SubprocVecEnv([
									env.make_gumball_env(),
									env.make_gumball_env(),
									env.make_gumball_env(),
									env.make_gumball_env(),
								]),
							nsteps=16, # Steps per environment
#							nsteps=2048, # Steps per environment
#							total_timesteps=10000000,
							total_timesteps=10000000,
							gamma=0.99,
							lam=0.95,
							vf_coef=0.5,
							ent_coef=0.01,
							lr = lambda _:2e-4,
							cliprange = lambda _:0.1, # 0.1 * learning_rate
							max_grad_norm = 0.5,
							log_interval  = 10
							)


if __name__ == '__main__':
	main()
