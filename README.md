# Backend Test

##  How to run
In order to run the project just rund `docker-compose up` and that's build the docker and run the app on port `5001`.

## How I finished to project
1. How did you complete the DB schema:
    Database was created using `SQLAlchemy` library. I created `Metric` and `ValueDefinition` tables and following commands created my schema:
    ```
    from app import db
    db.create_all()
    ```
    which creates following schema:
    ```
    CREATE TABLE metric (
        id INTEGER NOT NULL, 
        code VARCHAR(200) NOT NULL, 
        description VARCHAR(200) NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (code)
    );
    CREATE TABLE value_definition (
        id INTEGER NOT NULL, 
        label VARCHAR(200) NOT NULL, 
        type VARCHAR(200) NOT NULL, 
        metric_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(metric_id) REFERENCES metric (id)
    );
    ```
2. How to import the CSV to the SQL database:
    You can import csv from `localhost:5001/upload-csv` which imports csv file using `pandas`. you can find the method in `upload.py` file.
3. How to start your web framework, document the entry point in your software:
    By running `docker-compose up` from the project root, the app will be accessible on `localhost:5001`.

4. How to call your API endpoint to read the database and show the result of your route(s). Document your route(s):
    1. `http://localhost:5001`: shows the content of tables (if any data is uploaded) as well as links to json of metrics and value definitions and upload csv page.
    2. `http://localhost:5001/metrics`: shows the metrics in json form
    3. `http://localhost:5001/definitions`: shows the definitions in json form
    4. `http://localhost:5001/upload-csv`: provides a form to upload and import csv file into database

5. Any additional documentation you wish to provide or is required to run your project:
    I had planned to add some testing to the project but unfortunately I ran out of time.