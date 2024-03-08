# Salesperson-Task
# Introduction:
This task involves retrieving sales orders from an Odoo server using XML-RPC requests. It aims to evaluate your familiarity with the Odoo framework, specifically in making requests and working with sales orders and user data models.
# Prerequisites
- Prerequisites
- Python 3 installed on your system
- Access to an Odoo server
# Usage
1. Replace the placeholders in the code/configurations with your Odoo server details.

- localhost:8069 with your Odoo server URL
- odoo17 with your database name
- admin with your Odoo username
- admin with your Odoo password
2. Run the script.

 Code Explanation
- The script connects to Odoo using XML-RPC.
- It authenticates with the provided credentials.
- If authentication is successful, it retrieves the sales orders.
- It then processes and prints the retrieved orders with order ID, salesperson, and total amount.

  
Notes
- Make sure to replace the placeholder values with your actual Odoo server details.
- Handle any authentication failures by verifying your database name, username, and password.

Troubleshooting
- If you encounter authentication failures, double-check your database name, username, and password.


