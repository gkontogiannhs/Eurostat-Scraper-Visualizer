from dfi import DataFromInternet


class Main:
    # list which will hold dfi objects
    dfi_list = []

    # Simple Console style Menu
    while True:
        print(70 * '=')
        print('1. Download or process data')
        print('2. Plot data')
        print('3. Store data')
        print('4. Exit')
        choice = input('Choice: ')

        if choice == '1':
            print(70 * '=')
            # page url for the data we want to download
            url = input('Give url: ')
            # local filename
            filename = input('Give filename: ')
            # default excel format save
            filename += '.xlsx'

            # appending the 'to be downloaded' urls
            dfi_list += [DataFromInternet(url, filename)]

        elif choice == '2':
            # iterate through DFI objects and plot data for each
            for dfiObj in dfi_list:
                dfiObj.plot_data()

        elif choice == '3':
            # for every dif object in the list
            for dfiObj in dfi_list:
                print(70 * '=')
                ff = input('Give file format for \'' + dfiObj.get_title() + '\':')
                # save the filtered data with the required format
                dfiObj.export_data(ff)
        # cya
        elif choice == '4':
            break




