import numpy as np

from pogema import GridConfig


class PyMarlPogema:

    def __init__(self, env, grid_config, mh_distance=False):
        gc = grid_config
        self._grid_config: GridConfig = gc

        self.env = env
        self._mh_distance = mh_distance
        self._observations = self.env.reset()
        self.max_episode_steps = gc.max_episode_steps
        self.episode_limit = gc.max_episode_steps
        self.n_agents = self.env.get_num_agents()

    def step(self, actions):
        self._observations, rewards, dones, infos = self.env.step(actions)
        info = {}
        if all(dones):
            info.update(CSR=infos[0]['metrics']['CSR'])
            num_agents = self.env.get_num_agents()
            mean_isr = sum([infos[idx]['metrics']['ISR'] for idx in range(num_agents)]) / num_agents
            info.update(ISR=mean_isr)

        return sum(rewards), all(dones), info

    def get_obs(self):
        return np.array([self.get_obs_agent(agent_id) for agent_id in range(self.n_agents)])

    def get_obs_agent(self, agent_id):
        return np.array(self._observations[agent_id]).flatten()

    def get_obs_size(self):
        return len(np.array(self._observations[0]).flatten())

    def get_state(self):
        return self.env.get_state()

    def get_state_size(self):
        return len(self.get_state())

    def get_avail_actions(self):
        actions = []
        for i in range(self.env.get_num_agents()):
            actions.append(self.get_avail_agent_actions(i))
        return actions

    @staticmethod
    def get_avail_agent_actions(agent_id):
        return list(range(5))

    @staticmethod
    def get_total_actions():
        return 5

    def reset(self):
        self._grid_config = self.env.config
        self._observations = self.env.reset()
        return np.array(self._observations).flatten()

    def save_replay(self):
        return

    def get_env_info(self):
        env_info = {"state_shape": self.get_state_size(),
                    "obs_shape": self.get_obs_size(),
                    "n_actions": self.get_total_actions(),
                    "n_agents": self.n_agents,
                    "episode_limit": self.episode_limit,
                    }
        return env_info

    def get_stats(self):
        return {}

    def close(self):
        return

    def sample_actions(self):
        return self.env.sample_actions()
