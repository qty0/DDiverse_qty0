### Mini fullstack project for @DevelopDiverse

Install (I'm using ubuntu 20.04LTS): \
Requires python 3 and npm 6+ \
(you can copy paste the whole code block)

Backend:

```
cd be &&
python3 -m venv venv &&
source venv/bin/activate &&
pip install -r req.txt &&
flask run
```

That should start the be dev server.

In a different terminal run:
Frontend:

```
cd fe &&
npm i &&
npm run serve

```

Server should be running at [http://localhost:8080/](http://localhost:8080/)
