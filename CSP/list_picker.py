def control_f(input_state):
    Us_States = ['Alabama', 'California', 'Georgia', 'Rhode Island', 'Mississippi', 'Tennessee', 'New York',
             'New Hampshire', 'Virginia', 'Florida', 'New Mexico', 'Arizona']
    for state in Us_States:
        if state != input_state:
            boolean1 = 0
        if state == input_state:
            boolean1 = 1
        break
    if boolean1 == 1:
        print("You input state is in the list")
    elif boolean1 != 1:
        print("Your input state is not in the list")
control_f('Alabama')
# control_f('Michigan')

