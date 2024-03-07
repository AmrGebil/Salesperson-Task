# Salesperson-Task
# Introduction:
This task is designed to test your understanding of the Odoo framework, specifically in making JSON-RPC requests and working with sales orders and user data models.
# Prerequisites
- Prerequisites
- Python 3 installed on your system
- odoorpc library installed (pip install odoorpc)
- Access to an Odoo server
# Usage
1. Replace the placeholders in the code/configurations with your Odoo server details.

- localhost with your Odoo server domain
- 8069 with your Odoo server port
- odoo17 with your database name
- admin with your Odoo username
- admin with your Odoo password
2. Run the script.

2.1. Code Explanation
- The script uses the ODOO class from the odoorpc library to connect to the Odoo server.
- It attempts to authenticate with the provided credentials.
- If authentication is successful, it loads the required models and fields for the sales order.
- It makes a JSON-RPC request to retrieve the sales orders.
- Finally, it processes and prints the retrieved orders with order ID, salesperson, and total amount.
  
2.2.Notes
- Make sure to replace the placeholder values with your actual Odoo server details.
- Handle any RPC errors, typically caused by incorrect login credentials.
- Troubleshooting
- If you encounter authentication failures, double-check your database name, username, and password.


