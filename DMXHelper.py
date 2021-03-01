from DMXTarget import DMXTarget


def get_manufactory_target():
    print("1: Sony, 2: LG, 3: Mobell, 4: FFALCON, 5: Samsung, 6: TCL, 7: Casper")
    selection = input("Input your selection: ")
    switch_case = {
        1: "tivi-sony",
        2: "tivi-lg",
        3: "tivi-mobell",
        4: "tivi-ffalcon",
        5: "tivi-samsung",
        6: "tivi-tcl",
        7: "tivi-casper"
    }
    kind = switch_case.get(int(selection), "nothing")
    return kind


def get_resolution_target():
    print("1: 8K, 2: 4K, 3: 1080p, 4: 720p")
    selection = input("Input your selection: ")
    switch_case = {
        1: "8k",
        2: "ultra-hd-4k",
        3: "full-hd",
        4: "hd",
    }
    resolution = switch_case.get(int(selection), "nothing")
    return resolution


def get_kind_target():
    print("1: Smart Tivi, 2: Tivi QLED, 3: TV NanoCell, 4: Tivi OLED, 5: Tivi Android, 6: Tivi thiết kế đặc biệt")
    selection = input("Input your selection: ")
    switch_case = {
        1: "smart-tivi",
        2: "tivi-qled",
        3: "-nanocell",
        4: "tivi-oled",
        5: "android-tivi",
        6: "-co-thiet-ke-dac-biet"
    }
    kind = switch_case.get(int(selection), "nothing")
    return kind


def get_second_parameter():
    print("1: Kind or 2: Resolution")
    selection = input("Input your selection: ")
    if selection == str(1):
        while True:
            second_parameter = get_kind_target()
            if second_parameter != 'nothing':
                break
    else:
        while True:
            second_parameter = get_resolution_target()
            if second_parameter != 'nothing':
                break
    return second_parameter


def input_info_target():
    while True:
        manufactory = get_manufactory_target()
        if manufactory != 'nothing':
            break
    second_parameter = get_second_parameter()
    target = DMXTarget(manufactory, second_parameter)
    return target
