At Root
to crete virtual env
python3 -m venv .venv

Activate it 
source .venv/bin/activate


Check 
python --version
pip --version

Upgrade pip 
python -m pip install --upgrade pip

pip install numpy pandas matplotlib jupyter ipykernel

Save dependencies
pip freeze > requirements.txt

From now onwards - we can do 
pip install -r requirements.txt


If required globally then only we will do following things
alias python=python3
alias pip=pip3

echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc
source ~/.zshrc