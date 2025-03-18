from browser import document, html
from calculate import get_packages

rides = int(input("Amount of rides: "))
ride_len = int(input("Minutes per ride: "))

dott = get_packages()
# best_package = f"Best package for given price: {min(dott, key=lambda p: p.get_price(rides, ride_len))}"
# table = [(str(p), p.get_price(rides, ride_len)) for p in dott]

document <= html.P(f"Best package for given price: {min(dott, key=lambda p: p.get_price(rides, ride_len))}")
document <= html.HR()
document <= html.P("Cost for all packages:")
table = html.TABLE()
table <= html.TR([html.TD("Package price"), html.TD("Total cost")])
for p in dott:
    table <= html.TR([html.TD(str(p)), html.TD(p.get_price(rides, ride_len))])
document <= table