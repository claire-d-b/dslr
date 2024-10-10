source ~/.zshrc
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
alias norminette=flake8

python tester.py

deactivate
