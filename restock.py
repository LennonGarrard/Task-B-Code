import random
def restock_inventory(available_items, inventory_records, current_day):

    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
    sales = 0
    restocked_items = 0
    
    # Restocking logic
    if current_day == 0:
        restocked_items = 2000
        available_items = 2000  
        inventory_records.append((current_day, sales, restocked_items, available_items))
    
    elif current_day % 7 == 0 :
        sales_last_6_days = sum(record[1] for record in inventory_records[-6:])  # Sums all sales of the last 6 days
        restocked_items = sales_last_6_days
        
        available_items += restocked_items
    # Append to records
        inventory_records.append((current_day, sales, restocked_items, available_items))
    
        
    return available_items
