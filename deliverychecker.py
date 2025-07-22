import sys
import json

def print_error_json(error_code, message):
    data = {
    "status": "error",
    "error_code": error_code,
    "error_message": message
    }

    print(json.dumps(data, indent=2))

def delivery_address_not_in_path(deliveries, path):
    wrong_addresses = []
    for delivery in deliveries:
        for step in delivery:
             if step not in path:
                wrong_addresses.append(step)
    if wrong_addresses:
        return (True, wrong_addresses)
    return (False, 0)

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
    return (False, 0)

def plan_delivery_steps(deliveries, path):
    steps = []
    for address in path:
        action = False
        for delivery in deliveries:
            if address == delivery[0]:
                steps.append({"address": address, "action": "pickup"})
                action = True
            elif address == delivery[1]:
                steps.append({"address": address, "action": "dropoff"})
                action = True
        if not action:
            steps.append({"address": address, "action": "null"})

    data = {
        "status": "success",
        "steps": steps
    }

    print(json.dumps(data, indent=2))

def deliveryChecker(params):
    if len(params) < 2:
        print("Usage: deliverychecker <param1> <param2>")
        return
    
    deliveries = json.loads(params[0])
    path = json.loads(params[1])

    check_exist = delivery_address_not_in_path(deliveries, path)
    if check_exist[0]:
        if (len(check_exist[1]) == 1):
            addr = "address"
            w = "was"
        else:
            addr = "addresses"
            w = "were"
        print_error_json("delivery_address_not_in_path", "The " + addr + " " + str(check_exist[1]) + " " + w + " not found in the path.")
        return
    
    check_order = deliveries_not_in_order(path, deliveries)
    if check_order[0]:
        if (len(check_order[1]) == 1):
            deli = "delivery"
        else:
            deli = "deliveries"
        print_error_json("delivery_dropoff_before_pickup", "The " + deli + " " + str(check_order[1]) + " can't be made in the current direction of the path.")
        return
    
    plan_delivery_steps(deliveries, path)
    


deliveryChecker(sys.argv[1:])