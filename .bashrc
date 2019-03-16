# Forget commands or lazy? 
alias notebook="jupyter notebook --ip 0.0.0.0 --port 1337 --no-browser"
alias smi="nvidia-smi"
alias ticket="kinit && aklog"
alias gpu="watch -n0.5 --color gpustat -ucp --color"

# Get your favorite environment loaded on start
if (tty -s); then
    source activate $MY_CONDA_ENV
fi
