import xmlrpc.client

# Odoo server information
server_url = 'http://localhost:8069'  # Replace with your Odoo server URL
db = 'odoo17'  # Replace with your database name
username = 'admin'  # Replace with your Odoo username
password = 'admin'  # Replace with your Odoo password

# Connect to Odoo via XML-RPC
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(server_url))
uid = common.authenticate(db, username, password, {})

if uid:
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(server_url))

    # Define the fields to be loaded
    fields = ['name', 'user_id', 'amount_total']

    # Search for sales orders
    order_ids = models.execute_kw(db, uid, password,
                                  'sale.order', 'search',
                                  [[]])

    # Read the sales orders
    orders = models.execute_kw(db, uid, password,
                               'sale.order', 'read',
                               [order_ids], {'fields': fields})

    # Process and print the retrieved orders
    if orders:
        for order in orders:
            order_id = order['name']
            salesperson = order['user_id'][1] if order['user_id'] else 'Unassigned'
            total_amount = order['amount_total']
            print(f"Order ID: {order_id}, Salesperson: {salesperson}, Total Amount: {total_amount}")
    else:
        print("No sales orders found.")
else:
    print("Authentication failed. Check your database name, user name, or server url.")
