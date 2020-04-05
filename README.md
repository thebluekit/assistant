# Open source personal assistant
## Setting up dotenv
Place `.env` file into `app` folder  
Example of `.env` file:
```
# setting up PORT and IP for Flask server
HOST_IP = ""
PORT = 5000

# Address and password for DataBase (use Neo4j)  
Default link for localhost: http://localhost:7474/db/data/
DB_LINK = ""
DB_PASSWORD = ""
```

## Files structure

    .
    ├── app                        # Flask app folder
    │   ├── static                 # folder for static files of webpage
    │   │   ├── fonts              # fonts folder
    │   │   ├── img                # images folder
    │   │   ├── animations.js      # script for getting and posting messages
    │   │   └── styles.css         # styles for index.html
    │   ├── templates
    │   │   └── index.html         # main page of project
    │   ├── assistant.py           # assistent module - execute command from commands.py
    │   ├── commands.py            # module that containing commands of personal assistant
    │   ├── message.py             # module of recognition command from words
    │   └── script.py              # flask server module (executable file)
    ├── .gitignore
    └── README.md
