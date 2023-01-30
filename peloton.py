# V1 goals:
    # List the output required for stage 1 (half-zone), stage 2 (3/4 zone), and stage 3 (full zone)
    # Inputs don't need to be dynamic yet


#
#

def main():
    # Goal: List the output required for stage 1 (half-zone), stage 2 (3/4 zone), and stage 3 (full zone)

    # Steps:
        # Prompt user w menu, 1 for view Stage 1 outputs, 2 for Stage 2, etc
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

    #use algorithm to give top range to Zone 7 because it comes uncalculated


    for zone in zones:
        if zone['name'] == 'Zone 1':
            zone['tgt'] = int(zone['bt_range'] + zone['tp_range'] * .62)
        elif zone['name'] == 'Zone 7':
            zone['tp_range'] = int(zone['bt_range'] * 1.25)
            zone['tgt'] = int((zone['bt_range'] + zone['tp_range']) / 2)
        else:
            zone['tgt'] = int((zone['bt_range'] + zone['tp_range']) / 2)

        print(f"{zone['name']} (Stage 1): {zone['tgt']}")

    #testing commit
    #print(zones)

    input()










main()