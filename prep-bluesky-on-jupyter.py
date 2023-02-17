import os
import pykern.pkio

cwd = os.getcwd()
p = pykern.pkio.py_path(cwd)
if not p.join('radiasoft').exists():
    p.mkdir('radiasoft')
if not p.join('radiasoft/sirepo').exists():
    os.chdir('radiasoft')
    os.system('git clone https://github.com/radiasoft/sirepo')
    os.chdir('sirepo')
    os.system('pip install -e .')
os.chdir(cwd)
if not p.join('NSLS-II').exists():
    p.mkdir('NSLS-II')
if not p.join('NSLS-II/sirepo-bluesky').exists():
    os.chdir('NSLS-II')
    os.system('git clone https://github.com/NSLS-II/sirepo-bluesky')
    os.chdir('sirepo-bluesky')
    os.system(f'cp {cwd}/patch/setup.py .')
    os.system(f'cp {cwd}/patch/prepare_det_env.py examples')
    os.system(f'cp {cwd}/patch/prepare_flyer_env.py examples')
    os.system('pip install -e .')
    os.system('pip install srwpy')

# run sirepo http server with bluesky enabled
os.system(f'SIREPO_SRDB_ROOT={cwd}/NSLS-II/sirepo-bluesky/sirepo_bluesky/tests/SIREPO_SRDB_ROOT SIREPO_AUTH_BLUESKY_SECRET=bluesky SIREPO_AUTH_METHODS=bluesky SIREPO_FEATURE_CONFIG_PACKAGE_PATH=sirepo SIREPO_PKCLI_SERVICE_REACT_PORT= sirepo service http')