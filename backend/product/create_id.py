# Creates a custom Id for a collection
def create_id(json_data, id):

    prod = []

    if len(json_data["data"]) >= 1:
        for i in json_data["data"]:
            if id in i:
                prod.append(i[id])
        identity = max(prod)
        return identity
