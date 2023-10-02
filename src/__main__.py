import gui, config, scan


def main():
    conf = config.writeDefaultConfig()
    scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"])
    gui.startGUI()

if __name__ == "__main__":
    main()
