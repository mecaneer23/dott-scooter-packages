# pyright: ignore
# type: ignore

from browser import DOMEvent, bind, document, html
from calculate import get_packages

form = html.FORM()

rides_row = html.DIV()
rides_row <= html.LABEL("Amount of rides: ")
rides_input = html.INPUT()
rides_input.type = "number"
rides_row <= rides_input
form <= rides_row

len_row = html.DIV()
len_row <= html.LABEL("Minutes per ride: ")
len_input = html.INPUT()
len_input.type = "number"
len_row <= len_input
form <= len_row

submit = html.INPUT()
submit.type = "submit"
form <= submit

document <= form

wrapper_defined = False

# rides = int(input("Amount of rides: "))
# ride_len = int(input("Minutes per ride: "))


@bind(submit, "click")
def on_submit(event: DOMEvent) -> None:
    event.preventDefault()
    global wrapper_defined
    if wrapper_defined:
        del document["wrapper"]
    wrapper_defined = True
    rides = int(rides_input.value)
    ride_len = int(len_input.value)
    dott = get_packages()

    wrapper = html.DIV()
    wrapper <= html.P(
        f"Best package for given price: {min(dott, key=lambda p: p.get_price(rides, ride_len))}"
    )
    wrapper <= html.HR()
    wrapper <= html.P("Cost for all packages:")
    table = html.TABLE()
    table <= html.TR([html.TD("Package price"), html.TD("Total cost")])
    for p in dott:
        table <= html.TR(
            [html.TD(str(p)), html.TD(p.get_price(rides, ride_len))]
        )
    wrapper <= table
    document <= wrapper
