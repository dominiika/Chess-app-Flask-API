# Chess-App


Chess App is an application which enables the user to list all the possible moves for each chess figure from each field. The user can also check if moves from particular fields are permitted. 

Flask version: 1.1.1
<br />
Python version: 3.6.9
<br />
The app uses Black for linting and formatting.
<br />
The app contains unit tests.
<br />

### Installing and Prerequisites

To run the app locally, you can use Docker or a virtual environment.

**If you decide to use Docker:**
1. Create Docker container:

```
docker build -t chessapp:latest . 
```

2. Run the server:

```
docker run --network host -d chessapp

```

3. You can use the app at port 5000.

4. If you want to stop the server:

```
docker stop {image-d}

```

5. To get the image id, type:

```
docker ps

```

<br />

**If you decide to use a virtual environment:**

1. Create virtualenv:

```
virtualenv env
```


2. Activate the environment:

```
source env/bin/activate
```

3. Install the requirements

```
pip install -r requirements.txt
```

4. Run the app

```
python3 app.py
```

5. You can use the app at port 5000.


### Usage

1. To list all the available moves for a particular figure at a particular field, type a URL using the following pattern:

```
http://localhost:5000/api/v1/{chess-figure}/{current-field}
```

For example:

```
http://localhost:5000/api/v1/king/a2
```

2. To check if a particular move is possible, type a URL using the following pattern:

```
http://localhost:5000/api/v1/{chess-figure}/{current-field}/{dest-field}
```
For example:

```
http://localhost:5000/api/v1/king/a2/a3
```

3. The application will return a JSON response.

For example:

```json
{
  "availableMoves": [
    "A1",
    "B1",
    "B2",
    "B3",
    "A3"
  ],
  "currentField": "A2",
  "error": null,
  "figure": "king"
}
```
or

```json
{
   "move":"valid",
   "figure":"rook",
   "error": null,
   "currentField":"H2",
   "destField":"H3"
}
```

### Tests

1. To run the tests, type

```
python3 test_app.py
python3 test_figures.py
python3 test_converters.py
```
