import sys
import json

# This function prints an error message in JSON format
# with a specific error code and message.
def print_error_json(error_code, message):
    data = {
        "status": "error",
        "error_code": error_code,
        "error_message": message
    }

    print(json.dumps(data, indent=2))

# This function checks if any delivery addresses are not present in the given path.
# It returns a tuple where the first element is a boolean indicating
# whether there are missing addresses, and the second element is a list of those addresses.
def delivery_address_not_in_path(deliveries, path):
    wrong_addresses = []
    for delivery in deliveries:
        for step in delivery:
             if step not in path:
                wrong_addresses.append(step)
    if wrong_addresses:
        return (True, wrong_addresses)
    return (False, [])

# This function checks if any deliveries are not in the correct order
# based on the given path. It returns a tuple where the first element is a boolean
# indicating whether there are deliveries out of order, and the second element is a list of those deliveries.
def deliveries_not_in_order(path, deliveries):
    wrong_deliveries = []
    for delivery in deliveries:
        for address in path:
            if address == delivery[0]:
                break
            elif address == delivery[1]:
                wrong_deliveries.append(delivery)
    if wrong_deliveries:
        return (True, wrong_deliveries)
    return (False, [])

# This function plans the delivery steps based on the deliveries and the path.
# It creates a list of steps where each step contains the address and the action (pickup or dropoff).
# If an address is not part of any delivery, it is marked as a null
def plan_delivery_steps(deliveries, path):
    steps = []
    for address in path:
        action = False
        for pickup, dropoff in deliveries:
            if address == pickup:
                steps.append({"address": address, "action": "pickup"})
                action = True
            elif address == dropoff:
                steps.append({"address": address, "action": "dropoff"})
                action = True
        if not action:
            steps.append({"address": address, "action": "null"})

    data = {
        "status": "success",
        "steps": steps
    }

    print(json.dumps(data, indent=2))

# The core function that runs too checks and plans the delivery steps if everything is valid.
# It takes parameters from the command line.
def deliveryChecker(params):
    if len(params) != 2:
        print("Usage: deliverychecker <param1> <param2>")
        return
    
    try:
        deliveries = json.loads(params[0])
        path = json.loads(params[1])
    except json.JSONDecodeError:
        print("One or both parameters are not valid JSON.")
        return

    check_exist = delivery_address_not_in_path(deliveries, path)
    if check_exist[0]:
        if (len(check_exist[1]) == 1):
            addr = "address"
            w = "was"
        else:
            addr = "addresses"
            w = "were"
        print_error_json("delivery_address_not_in_path", f"The {addr} {check_exist[1]} {w} not found in the path.")
        return
    
    check_order = deliveries_not_in_order(path, deliveries)
    if check_order[0]:
        if (len(check_order[1]) == 1):
            deli = "delivery"
        else:
            deli = "deliveries"
        print_error_json("delivery_dropoff_before_pickup", f"The {deli} {str(check_order[1])} can't be made in the current direction of the path.")
        return
    
    plan_delivery_steps(deliveries, path)
    
# The entry point of the script, which calls the deliveryChecker function with command line arguments.
deliveryChecker(sys.argv[1:])