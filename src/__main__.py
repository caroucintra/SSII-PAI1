import gui, config, scan, compare, schedule, time

def task():
    conf = config.writeDefaultConfig()
    dict_new_hashes = scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"], True, False)
    compare.compare_hashes(dict_new_hashes)


def main():
    conf = config.writeDefaultConfig()
    scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"], False, True)
    print("before compare")
    compare.initialize_log()
    print("before gui")
    gui.startGUI()
    print("after gui")


""""
    scan_interval = conf["hids"]["scan_interval"]
    if scan_interval == 1:
        schedule.every(3).minutes.do(task)  
    elif scan_interval == 2:
        schedule.every(1).hour.do(task)
    else:
        schedule.every().day.at("10:30").do(task)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
"""


if __name__ == "__main__":
    main()
