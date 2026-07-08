from tabulate import tabulate

def render_table(stars):
    headers = ["Name", "RA", "Dec", "Mag"]
    table_data = [[s["name"], s["ra"], s["dec"], s["mag"]] for s in stars]

    return tabulate(table_data, headers=headers, tablefmt="grid")