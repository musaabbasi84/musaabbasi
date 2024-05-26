const http = require('http');
const mysql = require('mysql');

// Create a connection to the MySQL database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'your_username',
  password: 'your_password',
  database: 'your_database',
});

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database');
});

// Create an HTTP server
const server = http.createServer((req, res) => {
  // Set the response header
  res.setHeader('Content-Type', 'application/json');

  // Handle POST request to add an employee
  if (req.method === 'POST' && req.url === '/employees') {
    let body = '';
    req.on('data', (chunk) => {
      body += chunk;
    });
    req.on('end', () => {
      // Parse the data from the request body
      const data = JSON.parse(body);

      // Insert the employee into the database
      connection.query('INSERT INTO employees SET ?', data, (err, result) => {
        if (err) {
          console.error('Error executing query:', err);
          res.statusCode = 500;
          res.end(JSON.stringify({ error: 'Internal Server Error' }));
          return;
        }

        // Send the response
        res.statusCode = 201;
        res.end(JSON.stringify({ message: 'Employee added successfully' }));
      });
    });
  }

  // Handle GET request to retrieve all employees
  else if (req.method === 'GET' && req.url === '/employees') {
    // Fetch all employees from the database
    connection.query('SELECT * FROM employees', (err, rows) => {
      if (err) {
        console.error('Error executing query:', err);
        res.statusCode = 500;
        res.end(JSON.stringify({ error: 'Internal Server Error' }));
        return;
      }

      // Send the response
      res.statusCode = 200;
      res.end(JSON.stringify(rows));
    });
  }

  // Handle GET request to retrieve a specific employee
  else if (req.method === 'GET' && req.url.startsWith('/employees/')) {
    const id = req.url.split('/')[2];

    // Fetch the employee from the database by ID
    connection.query('SELECT * FROM employees WHERE id = ?', id, (err, rows) => {
      if (err) {
        console.error('Error executing query:', err);
        res.statusCode = 500;
        res.end(JSON.stringify({ error: 'Internal Server Error' }));
        return;
      }

      if (rows.length === 0) {
        res.statusCode = 404;
        res.end(JSON.stringify({ error: 'Employee not found' }));
        return;
      }

      // Send the response
      res.statusCode = 200;
      res.end(JSON.stringify(rows[0]));
    });
  }

  // Handle PUT request to update an employee
  else if (req.method === 'PUT' && req.url.startsWith('/employees/')) {
    const id = req.url.split('/')[2];
    let body = '';
    req.on('data', (chunk) => {
      body += chunk;
    });
    req.on('end', () => {
      // Parse the data from the request body
      const data = JSON.parse(body);

      // Update the employee in the database
      connection.query(
        'UPDATE employees SET ? WHERE id = ?',
        [data, id],
        (err, result) => {
          if (err) {
            console.error('Error executing query:', err);
            res.statusCode = 500;
            res.end(JSON.stringify({ error: 'Internal Server Error' }));
            return;
          }

          // Send the response
          res.statusCode = 200;
          res.end(JSON.stringify({ message: 'Employee updated successfully' }));
        }
      );
    });
  }

  // Handle DELETE request to delete an employee
  else if (req.method === 'DELETE' && req.url.startsWith('/employees/')) {
    const id = req.url.split('/')[2];

    // Delete the employee from the database
    connection.query('DELETE FROM employees WHERE id = ?', id, (err, result) => {
      if (err) {
        console.error('Error executing query:', err);
        res.statusCode = 500;
        res.end(JSON.stringify({ error: 'Internal Server Error' }));
        return;
      }

      // Send the response
      res.statusCode = 200;
      res.end(JSON.stringify({ message: 'Employee deleted successfully' }));
    });
  }

  // Handle other requests
  else {
    res.statusCode = 404;
    res.end(JSON.stringify({ error: 'Not Found' }));
  }
});

// Start the server on port 3000
server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
