Last login: Sun Dec  1 19:51:21 on ttys002
docker compose up


docker compose up



(base) timseubert@MacBook-Air-3 ~ % docker compose up
no configuration file provided: not found
(base) timseubert@MacBook-Air-3 ~ % 
(base) timseubert@MacBook-Air-3 ~ % 
(base) timseubert@MacBook-Air-3 ~ % docker compose up
no configuration file provided: not found
(base) timseubert@MacBook-Air-3 ~ % 
(base) timseubert@MacBook-Air-3 ~ % 
(base) timseubert@MacBook-Air-3 ~ % 
(base) timseubert@MacBook-Air-3 ~ % docker compose up

no configuration file provided: not found
(base) timseubert@MacBook-Air-3 ~ % docker --version
Docker version 27.3.1, build ce12230
(base) timseubert@MacBook-Air-3 ~ % docker compose version
Docker Compose version v2.30.3-desktop.1
(base) timseubert@MacBook-Air-3 ~ % mkdir getting-started
cd getting-started

mkdir: getting-started: File exists
(base) timseubert@MacBook-Air-3 getting-started % nano app.py


  UW PICO 5.09                                       File: app.py                                        Modified  

import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
















^G Get Help        ^O WriteOut        ^R Read File       ^Y Prev Pg         ^K Cut Text        ^C Cur Pos         
^X Exit            ^J Justify         ^W Where is        ^V Next Pg         ^U UnCut Text      ^T To Spell        
