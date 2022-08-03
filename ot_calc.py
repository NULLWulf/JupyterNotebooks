def output_ot(hours):
    hourly, ot_rate, tax = 24.00, 1.5, .25
    if hours <= 40:
        gross = hourly * hours
    else:
        gross = ( (hours - 40 ) * ot_rate * hourly  ) + ( 40 * hourly)
    taxes = gross * tax
    net = gross - taxes

    print("""
    Hours : {}
    Gross : {}
    Taxes : {}
    Net   : {}
    """.format(hours, gross, taxes, net))