# channel-admin-bot
[![Python](https://img.shields.io/badge/Python-3.12.2-3776AB?style=flat&logo=Python&logoColor=yellow)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.3-336791?style=flat&logo=PostgreSQL&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.13.1-3776AB?style=flat&logo=telegram&logoColor=white)](https://aiogram.dev/)
[![Ruff](https://img.shields.io/badge/Ruff-0.6.9-FCC21B?style=flat&logo=ruff&logoColor=white"/)](https://github.com/astral-sh/ruff)
[![Ruff](https://img.shields.io/badge/Babel-2.16-F9DC3E?style=flat&logo=babel&logoColor=white)](https://github.com/astral-sh/ruff)
[![Flake8](https://img.shields.io/badge/flake8-checked-blueviolet?style=flat)](https://flake8.pycqa.org/en/latest/)

**Admin Bot** — is a simple Telegram bot designed for managing content and users in a Telegram channel. 
The project is built using Python 3.12.2, leveraging `aiogram`, `asyncpg`, `Babel`, and `SQLAlchemy` for interacting with a `PostgreSQL` database.

## Table of Contents
 - [Key Features 🎯](#Key-Features)
 - [Installation and Setup ⚙️](#Installation-and-Setup)
 - [Project Structure 🗂️](#Project-Structure)
 - [Makefile Commands 🛠️](#Makefile-Commands)
 - [Adding New Languages 🌐](#Adding-New-Languages)
 - [Future Plans 🚀](#Future-Plans)
 - [Contributing 💡](#Contributing)
 - [License 🏷️](#License)
 - [Author 👤](#Author)

## Key Features:
- Post management: view, create, edit, and delete posts.
- Publish posts to a channel.
- Assign and remove user roles: administrator, content manager.

![Admin Bot](./img/image.png)

## Installation and Setup
**Requirements:**
- Python 3.12.2
- PostgreSQL 16.3

***Install dependencies from `requirements.txt`***

### Installation Steps
#### Clone the repository:
```sh
git clone https://github.com/dev-lymar/channel-admin-bot.git
```
#### Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
#### Install dependencies:
```sh
pip install -r requirements.txt
```
#### Create a `.env` file: Copy `.env.example` file:
```sh
cp .env.example .env
```
#### Edit the `.env` file with your API token and PostgreSQL database details:
```sh
API_TOKEN=your_bot_token
ADMIN_ID=administrator_ID (For initial setup)
DB_URL=postgresql+asyncpg://user:password@localhost:5432/database_name
CHAT_ID=channel_ID_for_publications
```
#### Run the bot with automatic translation compilation and migrations:
```sh
make run
```
## Project Structure
```sh
.
├── main.py                 # Entry point of the application
├── config/                 # Configuration files
│   ├── .env.example        # Example environment variables file
│   └── bot_config.py       # Bot configuration and settings
├── db/                     # Database management
│   ├── db_handler/         # Handlers for posts and user roles
│   └── models/             # Database models
├── handlers/               # Command and function handlers for the bot
│   ├── admin_panel/        # Logic for the admin panel
│   └── start/              # Start command
├── locales/                # Localization files
│   ├── en/                 # English translations
│   └── ru/                 # Russian translations
├── keyboards/              # Telegram keyboards for user interaction
├── states/                 # User state management
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── LICENSE                 # License for project usage
```

## Makefile Commands
- `make run`: Runs the bot and compiles translation files `.po` into `.mo`.
- `make lint`: Checks the code for style compliance using `ruff` and `flake8`.

## Adding New Languages
1. If there are changes in the text, update the message template (`if not, proceed to step 3`):
```sh
pybabel extract -k _:1,1t -k _:1,2 -k __ --input-dirs=. -o locales/messages.pot
```
2. Update existing locales:
```sh
pybabel update -d locales -D messages -i locales/messages.pot
```
3. Create a new locale (e.g., `uk` for Ukrainian):
```sh
pybabel init -i locales/messages.pot -d locales -D messages -l uk
```
4. Compile translations automatically using `make run` or manually:
```sh
pybabel compile -d locales -D messages
```

## Future Plans
- **Docker Integration**: Implement a Docker file for easier project deployment.
- **Documentation**: Provide detailed documentation for all modules, including usage examples and possible scenarios.
- **Role Expansion**: Add more roles and access management capabilities.

## Contributing
We welcome contributions from the community! If you want to add new features or fix bugs, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/feature-name`
3. Make your changes and commit them: `git commit -m 'Added a new feature'`
4. Push your changes: `git push origin feature/feature-name`
5. Create a **pull request**.

*Before creating a pull request, make sure your code passes all **ruff** and **flake8** checks.*


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author
This project was developed by [dev-lymar](https://github.com/dev-lymar). 
If you enjoyed the project, please give a star ⭐️ on the [repository](https://github.com/dev-lymar/channel-admin-bot).

If you have any questions or suggestions, feel free to reach out:

<a href="https://t.me/vlymar">
<img src="https://img.shields.io/badge/-Telegram-26A5E4?style=flat&logo=telegram&logoColor=white"/>
</a>
<a href="mailto:lymarvolodymyr1@gmail.com">
<img src="https://img.shields.io/badge/-Gmail-EA4335?style=flat&logo=gmail&logoColor=white"/>
</a>

