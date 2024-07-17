source ~/.zshrc
python -m venv venv
source venv/bin/activate

echo alias python='./venv/bin/python' >> ./venv/bin/activate
source venv/bin/activate

pip install flake8
alias norminette=flake8

pip install numpy

python tester.py

deactivate

rm -rf __pycache__
rm -rf venv
