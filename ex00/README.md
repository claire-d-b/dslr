source ~/.zshrc
python -m venv venv
source venv/bin/activate

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

python tester.py

deactivate

rm -rf __pycache__
rm -rf venv
