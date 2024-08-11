# Interview Task (vervoe-flask-app)
---

### Project Overview

#### High-level Design
##### Flow Chart


![image](https://github.com/user-attachments/assets/80f17c09-14b7-4d1b-a9b8-0a0d6e1707be)



##### 1. Purpose:
  The primary goal of this project is to retrieve data from an external API, process it, and save the results to a database and retrive from the database.

##### 2. Architecture:
  - **Data Fetching:** The data retrieval process is designed to fetch information from the external service API.
  - **Data Processing:** After fetching, the data undergoes processing to prepare it for storage.
  - **Data Storage:** Processed data is stored in a structured format within a database.

##### 3. Optimization Strategy:
  - **Task Distribution:** To optimize processing time for large datasets, the project divides the data fetching and processing into multiple subtasks.
  - **Parallel Execution:** By distributing these subtasks across multiple processes or threads, the system reduces bottlenecks and accelerates data handling.

##### 4. Benefits:
  - **Efficiency:** Parallelizing the workflow minimizes the time required to process extensive datasets.

##### 5. Data Transformation:
  - **Case Conversion:** As part of the data processing step, the system performs case conversion, where uppercase words are changed to lowercase and vice versa. This ensures consistency and can be useful for normalization or comparison tasks.


## Installation

##### 1. Clone the repository:

  ```bash
    git close https://github.com/venkatasidhartha/vervoe-flask-app.git
  ```

##### 2. Navigate to the project directory:

  ```bash
    cd vervoe-flask-app
  ```

##### 3. Create and Enable Virtual Enviroment:

  ```bash
    python3 -m venv env
    source env/bin/active
  ```

##### 4. Install dependencies:

   ```bash
    pip install -r requirements.txt
  ```

##### 4. Configure .env:

  ```bash 
  cat .env.example > .env
```

##### 4. To Give Execute Permission:

  ```bash 
  chmod +x start.sh
```

## Usage
After installing the project and configuring the environment settings, follow these steps to start the web server:

##### Start the Web Server:
  - To launch the web server, execute the following command:
    ```bash
    ./start.sh
    ```
  - This script will initiate the server and make the application available at the specified host and port.

**Note:** Ensure that `start.sh` has execution permissions. If not, you can set the permissions using:
  ```bash 
  chmod +x start.sh
```

### API Endpoints

  1. Fetch Data
     -   **Endpoint:** `http://127.0.0.1:5000/fetch-data`
     -   **Method:** GET
     -   **Description:** This endpoint triggers the process to fetch data from an external service. It distributes the tasks to subtasks using Python's multiprocessing library, processes the data, and stores it in the database.
     -   **Response:**
     
             ```json
              {
                "message": "Process is started",
                "status": "green"
              }
             ```
      - **Error Handling:**
          - **External Service Errors:** Errors encountered while fetching data from the external service will be logged.
          - **Processing Errors:** Errors during data processing will be logged, and the problematic data will be saved in the `capture_data_error` folder for further analysis.
          - **Storage Errors:** Errors that occur while storing data in the database will be logged, with the problematic data also saved in the `capture_data_error` folder.

  2. Get Processed Data
      - **Endpoint:** `http://127.0.0.1:5000/get-processed-data`
      - **Method:** GET
      - **Description:** This endpoint retrieves processed data from the database. By default, it returns the first 10 records.
      - **Parameters:**
          - `page_no` (optional): The page number for pagination.
          - `page_length` (optional): The number of records per page.
      - **Usage:**
          - **Pagination:** Set `page_no` to the desired page number and `page_length` to the number of records per page to implement pagination.
          - **Retrieve All Data:** Set `page_no` to `0` and `page_length` to `0` to retrieve all records from the database without pagination limits.
      - **Responses:**
          - **Successful Data Retrieval:**
              - If records are present, the data will be returned as per the pagination or limit specified.
          - No Data Present:
              ```json
                  {
                    "message": "Data is Empty",
                    "status": "green"
                  }
              ```
      - **Error Handling:**
          - Common Error Handling: Any errors occurring with this endpoint will be logged by the system.

### Common API Response Status
  - **Success:** All successful API responses will have `"status": "green"`, indicating that the API executed successfully.
  - **Failure:** If the API execution fails, the `"status"` will be `"red"`, and the response will include a `"trace"` with details of the error.

### Common API Error Message
  In the event of an error, the response will be:

    ```json
      {
        "message": "An unexpected error occurred",
        "status": "red",
        "trace": "Detailed error description"
      }
    ```
  - Status Code: The default HTTP status code for errors is `500`.
---

**Note :** In-memory storage was not used due to the need for persistent storage while employing the `multiprocessing` library. Data is stored persistently in the database to ensure that the system can manage and recover from processes effectively.

Additionally, I am adding a Postman collection to the repository. Check it out for detailed API testing and examples.
        

      




