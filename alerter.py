alert_failure_count = 0


def network_alert_stub(celsius):
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celsius > 100.00:
        print(f'ALERT: Temperature is {celsius} celsius')
        return 500
    return 200


def alert_in_celsius(fahrenheit: float):
    celsius = (fahrenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celsius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1


alert_in_celsius(400.5)  # should increment the alert_failure_count by 1 because of return code : 500
assert (alert_failure_count == 1)
alert_in_celsius(303.6)  # should increment the alert_failure_count by 1 because of return code : 500
assert (alert_failure_count == 2)
alert_in_celsius(50.6)  # shouldn't increment the alert_failure_count by 1 because of return code : 200
assert (alert_failure_count == 2)
print(f'{alert_failure_count} alerts failed.')
