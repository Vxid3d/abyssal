# abyssal_
a python framework (unorganized) for make python easier to work with.
<img width="1089" height="511" alt="Screenshot 2026-05-31 at 10 11 17 AM" src="https://github.com/user-attachments/assets/ae67cfd7-9894-46f4-ac6f-3ddb2a4c57f1" />
# Setup
## this is the format you want to format your code (from the repo) in.
```text
.
├── pytooler
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-314.pyc
│   │   ├── __utility__.cpython-314.pyc
│   │   └── color.cpython-314.pyc
│   ├── __utility__.py
│   └── color.py
└── verse
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-314.pyc
    │   └── crux.cpython-314.pyc
    ├── crux.py
    └── test.py
  ^ folder name: abyssal, path = /Users/_______/abyssal
  _______ = your username
  ## read the GUIDE.md to find out how to use this.
```
### sample code:
```text
from abyssal.pytooler import __utility__ as u,  color as c
from abyssal.verse import crux
crux.Spam.cli_spam(
    100,
    100,
    "hi"
    )
listx = [1,2,3,4,5,6,7,8,9,10]
u.Programm.binary_search(listx, 7)
print(f"{c.RED} hi {c.RESET}")
```


