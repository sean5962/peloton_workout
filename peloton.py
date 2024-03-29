# V1 goals:
    # Menu that asks 1, 2, 3 for which stage to display
    # List the output required for stage 1 (half-zone), stage 2 (3/4 zone), and stage 3 (full zone)
    # Inputs don't need to be dynamic yet

# V1.1 goals: 
    # Make formula dynamic
    # Add quit button
    # Clean code presentation

# V2.0 goals: 
    # Add ability to get weightlifting numbers
    # Press '9' to get to weightlifting numbers
    # Ask for which types of weights you have, then desired rep range
    # Output list of increasing difficulty sets w percentage increase listed

def main():
    

    # Steps:
        # Prompt user w menu, 1 for bike, 2 for weights, q for quit
            # Bike menu: Prompt user w menu, 1 for view Stage 1 outputs, 2 for Stage 2, etc
                # Display each zone for each stage
                # Zone 1 rest is 62% of Zone 1
                # Current Top/Bottom as of Jan '23:
                    # Zone 1: 0 - 106 (Rest 65)
                    # Zone 2: 106 - 144
                    # Zone 3: 144 - 173
                    # Zone 4: 173 - 202
                    # Zone 5: 202 - 230
                    # Zone 6: 230 - 288
                    # Zone 7: 288+
            # Weight menu: Prompt for weight amounts available, then rep range requested
                #calculate different options, with 0-10% increase in each option, heavier weights classified as more difficult if same total weight

    

    # Menu loop that prompts for which zone to display

    while True:
        prompt =  int(input("Which zone do you need? "))
        
        if prompt == 1 or prompt == 2 or prompt == 3:
            zone_display(prompt)
            break
            


def zone_display(number):
    #use algorithm to give top range to Zone 7 because it comes uncalculated

    #list of dictionaries, listing name, bottom of the range, top of the range, and target output
    zones = [
        {"name": "Zone 1", "bt_range": 0, "tp_range": 106, "tgt": 0},
        {"name": "Zone 2", "bt_range": 106, "tp_range": 144, "tgt": 0},
        {"name": "Zone 3", "bt_range": 144, "tp_range": 173, "tgt": 0},
        {"name": "Zone 4", "bt_range": 173, "tp_range": 202, "tgt": 0},
        {"name": "Zone 5", "bt_range": 202, "tp_range": 230, "tgt": 0},
        {"name": "Zone 6", "bt_range": 230, "tp_range": 288, "tgt": 0},
        {"name": "Zone 7", "bt_range": 288, "tp_range": None, "tgt": 0}
    ]

    #initialize var to populate stage number 
    stage = number

    #stage multiplier that makes it more difficult w each stage increase
    #initialize and then set based on parameter passed through function
    stage_mult = 1
    if number == 1:
        stage_mult = .5
    elif number == 2:
        stage_mult = .75
    elif number == 3:
        stage_mult = 1


    #calculate and print 

    for zone in zones:
        if zone['name'] == 'Zone 1':
            zone['tgt'] = int(zone['bt_range'] + zone['tp_range'] * .62)
        elif zone['name'] == 'Zone 7':
            zone['tp_range'] = int(zone['bt_range'] * 1.25)
            zone['tgt'] = int((zone['tp_range'] - zone['bt_range']) * stage_mult + zone["bt_range"])
        else:
            zone['tgt'] = int((zone['tp_range'] - zone['bt_range']) * stage_mult + zone["bt_range"])

        print(f"{zone['name']} (Stage {stage}): {zone['tgt']}")

    input()


main()