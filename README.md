# Running sirepo-bluesky on jupyter:

# The first time:
- open a terminal in jupyter
  - cd ~/jupyter
  - mkdir moellep
  - cd moellep
  - gcl sirepo-bluesky-on-jupyter
  - cd sirepo-bluesky-on-jupyter
  - python prep-bluesky-on-jupyter.py
  - and wait for it get to the "Running on ..." line
  - now open a notebook in the moellep/sirepo-bluesky-on-jupyter/NSLS-II/sirepo-bluesky/docs/source/notebookes directory


# After the first time:
- open a terminal in jupyter
  - cd ~/jupyter/moellep/sirepo-bluesky-on-jupyter
  - python prep-bluesky-on-jupyter.py
  - now open a notebook in the moellep/sirepo-bluesky-on-jupyter/NSLS-II/sirepo-bluesky/docs/source/notebookes directory or moellep/sirepo-bluesky-on-jupyter/NSLS-II/bloptools/docs/source/notebooks/gp-optimizer.ipynb


# Adding a new simulation:
To add a new simulation to the bluesky testing environment, follow the steps in this wiki.

https://github.com/moellep/sirepo-bluesky-on-jupyter/wiki/Add-a-sim-to-bluesky
