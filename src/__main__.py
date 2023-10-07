import gui, config, scan, compare, schedule, time, send_mail

def monthly_mail():
    conf = config.readConfig()
    recipient = conf['hids']['email_to_notify']
    #recipient = "jule.nogaj@gmail.com"
    send_mail.send_email(recipient)
    print("Monthly report was sent.")
    with open("log.log", 'w') as log_file:
        log_file.write("")
        print("Log file cleared.")


def daily_scan():
    conf = config.readConfig()
    dict_new_hashes = scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"], True, False)
    compare.compare_hashes(dict_new_hashes)
    print("Daily scan is finished.")


def main():
    conf = config.writeDefaultConfig()
    scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"], False, True)
    print("Basic scan finished.")
    compare.initialize_log()
    print("Log initialized.")
    gui.startGUI()

# schedule the scans
    scan_interval = conf["hids"]["scan_interval"]
    # normally 3 means testing daily, here only 10 seconds for testing purposes because 3 is default value
    if scan_interval == "3":
        schedule.every(10).seconds.do(daily_scan)  
    elif scan_interval == "2":
        schedule.every(1).hour.do(daily_scan)
    else:
        schedule.every().day.at("10:30").do(daily_scan)

# schedule the emails for testing purpose
    log_interval = conf['hids']['log_interval']
    if log_interval == "3":
        schedule.every(1).minute.do(monthly_mail)


    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()
