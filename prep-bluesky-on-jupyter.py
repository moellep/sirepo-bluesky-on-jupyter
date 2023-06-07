import os
import pykern.pkio

cwd = os.getcwd()
p = pykern.pkio.py_path(cwd)
if not p.join('NSLS-II').exists():
    p.mkdir('NSLS-II')
if not p.join('NSLS-II/sirepo-bluesky').exists():
    os.chdir(f'{cwd}/NSLS-II')
    os.system('git clone https://github.com/NSLS-II/sirepo-bluesky')
    os.chdir('sirepo-bluesky')
    os.system(f'cp {cwd}/patch/sirepo-bluesky/prepare_det_env.py examples')
    os.system(f'cp {cwd}/patch/sirepo-bluesky/prepare_flyer_env.py examples')
    os.system("perl -pi.bak -e 's/srwpy\.//g' sirepo_bluesky/srw_handler.py")
if not p.join('NSLS-II/bloptools').exists():
    os.chdir(f'{cwd}/NSLS-II')
    os.system('git clone https://github.com/NSLS-II/bloptools')
    os.chdir('bloptools')
    os.system(f'cp {cwd}/patch/bloptools/prepare_bluesky.py examples/')

os.chdir(f'{cwd}/NSLS-II/sirepo-bluesky')
os.system('pip install -e .')
os.chdir(f'{cwd}/NSLS-II/bloptools')
os.system('pip install -e .')
os.chdir(cwd)
# run sirepo http server with bluesky enabled
port = 8000
os.system(f'SIREPO_PKCLI_SERVICE_PORT={port} SIREPO_PKCLI_JOB_SUPERVISOR_PORT={port + 1000} SIREPO_JOB_DRIVER_LOCAL_SUPERVISOR_URI=\'http://127.0.0.1:{port + 1000}\' SIREPO_JOB_API_SUPERVISOR_URI=\'http://127.0.0.1:{port + 1000}\' SIREPO_SRDB_ROOT={cwd}/NSLS-II/sirepo-bluesky/sirepo_bluesky/tests/SIREPO_SRDB_ROOT SIREPO_AUTH_BLUESKY_SECRET=bluesky SIREPO_AUTH_METHODS=bluesky SIREPO_PKCLI_SERVICE_REACT_PORT= sirepo service http')
