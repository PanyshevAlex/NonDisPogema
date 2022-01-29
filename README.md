<div align="center">


[![Pogema logo](https://raw.githubusercontent.com/Tviskaron/pogema-pics/main/pogema-logo.svg)](https://github.com/AIRI-Institute/pogema)    

**Partially-Observable Grid Environment for Multiple Agents**

[![CodeFactor](https://www.codefactor.io/repository/github/tviskaron/pogema/badge)](https://www.codefactor.io/repository/github/tviskaron/pogema)
[![Downloads](https://pepy.tech/badge/pogema)](https://pepy.tech/project/pogema)
[![CI](https://github.com/AIRI-Institute/pogema/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/AIRI-Institute/pogema/actions/workflows/CI.yml)    
</div> 

Pogema is a high-throughput environment for partially observable multi-agent pathfinding tasks (PO-MAPF). Pogema is especially flexible, tunable and scalable environment, which can be tailored to a variety of MAPF settings.

## Installation

Just install from PyPI:

```pip install pogema==1.0b1```

## Using Example

```python
import gym
from pogema.grid_config import GridConfig
from pogema.wrappers.multi_time_limit import MultiTimeLimit
from pogema.animation import AnimationMonitor

env = gym.make('Pogema-v0', config=GridConfig(size=16, num_agents=16))
env = MultiTimeLimit(env, max_episode_steps=64)
env = AnimationMonitor(env)

obs = env.reset()

done = [False, ...]
while not all(done):
    obs, reward, done, info = env.step([env.action_space.sample() for _ in range(env.config.num_agents)])
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/19dSEGTQeM3oVJtVjpC162t1XApmv6APc?usp=sharing) 


## Citation
If you use this repository in your research or wish to cite it, please make a referenct to our IEEE paper: 
```
@article{skrynnik2021hybrid,
  title={Hybrid Policy Learning for Multi-Agent Pathfinding},
  author={Skrynnik, Alexey and Yakovleva, Alexandra and Davydov, Vasilii and Yakovlev, Konstantin and Panov, Aleksandr I},
  journal={IEEE Access},
  volume={9},
  pages={126034--126047},
  year={2021},
  publisher={IEEE}
}
```
