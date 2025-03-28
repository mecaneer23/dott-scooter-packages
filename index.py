"""Brython html UI for calculate"""
# type: ignore[reportOperatorIssue, reportUnusedExpression]
# ruff: noqa: B015

from browser import DOMEvent, bind, document, html
from calculate import Rides, get_packages

form = html.FORM()

rides_row = html.DIV()
rides_row <= html.LABEL("Amount of rides: ")
rides_input = html.INPUT()
rides_input.autofocus = True
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

form_wrapper = html.DIV()
form_wrapper.classList.add("form-wrapper")
form_wrapper <= form
document <= form_wrapper

wrapper = html.DIV()
wrapper.id = "wrapper"
document <= wrapper


@bind(submit, "click")
def on_submit(event: DOMEvent) -> None:
    """Handle submit button press"""
    event.preventDefault()
    rides = int(rides_input.value)
    ride_len = int(len_input.value)
    dott = get_packages()

    wrapper = document["wrapper"]
    wrapper.clear()
    wrapper <= html.P(
        f"Best package for given price: "
        f"{min(dott, key=lambda p: p.get_price(Rides(rides, ride_len)))}",
    )
    wrapper <= html.HR()
    wrapper <= html.P("Cost for all packages:")
    table = html.TABLE()
    table <= html.TR([html.TD("Package price"), html.TD("Total cost")])
    for p in dott:
        table <= html.TR(
            [html.TD(str(p)), html.TD(p.get_price(Rides(rides, ride_len)))],
        )
    wrapper <= table
    document <= wrapper
