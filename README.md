python -m venv venv
source venv/bin/activate

pip install numpy flake8 pandas matplotlib seaborn
alias norminette=flake8

deactivate
