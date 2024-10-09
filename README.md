source ~/.zshrc
python -m venv venv
source venv/bin/activate

echo alias python='./venv/bin/python' >> ./venv/bin/activate
source venv/bin/activate

alias norminette=flake8

pip3 freeze > requirements.txt

python tester.py

deactivate

rm -rf **pycache**
rm -rf venv
