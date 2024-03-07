from odoorpc import ODOO

# Connect to the Odoo server
from odoorpc.error import RPCError

odoo = ODOO('localhost', port=8069) # Replace with your Odoo server (Domain and Port)
db_name = 'odoo17' # Replace with your database name
user = 'admin' # Replace with your Odoo username
password = 'admin' # Replace with your Odoo password

try:
    # Attempt to login
    odoo.login(db_name, user, password)
    # Define the fields to be loaded
    fields = ['name', 'user_id', 'amount_total']

    # Load the required models 
    odoo.env['sale.order']

    # Retrieve sales orders using a JSON-RPC request
    orders = odoo.env['sale.order'].search_read([], fields)

    # Process and print the retrieved orders
    if orders:
        for order in orders:
            order_id = order['name']
            salesperson = order['user_id'][1] if order['user_id'] else 'Unassigned'
            total_amount = order['amount_total']
            print(f"Order ID: {order_id}, Salesperson: {salesperson}, Total Amount: {total_amount}")
    else:
        print("No sales orders found.")


except RPCError as e:
    # Handle RPC error, typically caused by wrong login credentials
    print("Authentication failed. Check your database name, user name, or Odoo parameters(domain or port).")






