## This is a simple version of a program that can parse your telegram messages and show some stats.

### 1. Installation
Clone the repository to your local machine.
```bash
git clone https://github.com/VTiganov/tg_parser_and_statistics.git
```

### 2. Installing dependencies.
All requirements can be automatically installed by running this:
```PowerShell
pip install -r requirements.txt
```

### 3. Creating and setting up config file.
Firstly, you need to visit _[Telegram for developers](https://my.telegram.org/apps)_ website. \
\
Then you will need to get your **api_id** and **api_hash** like on the picture below.
![example](img\api_hash_example.png)
\
\
Then you have to create your **.env** file in the root of the copied repository. Put your **api_id** and **api_hash** there like that:
```
API_ID=<YOUR_API_ID>
API_HASH=<YOUR_API_HASH>
```
