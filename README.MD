# AI Roadmap Workspace

## Python Environment Setup

### 1. Create a Virtual Environment

At the project root, run:

```bash
python3 -m venv .venv
```

### 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 3. Verify Installation

```bash
python --version
pip --version
```

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install Core Dependencies

```bash
pip install numpy pandas matplotlib jupyter ipykernel
```

### 6. Save Dependencies

```bash
pip freeze > requirements.txt
```

### 7. Install from Requirements (Future Use)

From now onwards, to set up the environment:

```bash
pip install -r requirements.txt
```

---

## Global Aliases (Optional)

Only set these if you need `python` / `pip` to point to Python 3 globally:

```bash
alias python=python3
alias pip=pip3
```

To persist across terminal sessions, add them to your shell config:

```bash
echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc
source ~/.zshrc
```