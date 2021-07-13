import OnLaunch
import datetime
import time
import threading
import MaintainLatest
import MaintainVolume

sleep_updateLatest = 120     # Updates every 120 seconds
sleep_oneHourVolume = 3300  # Updates every 55 minutes
sleep_oneDayVolume = 86400  # Updates every 24 hours


def updateLatest():
    while True:
        for attempt in range(10):
            right_now = datetime.datetime.now()
            try:
                print(right_now)
                print("Fetching Latest Prices")
                MaintainLatest.fetchLatestPrices()
                print("Latest Prices Completed")
                print("Updating Latest Prices")
                MaintainLatest.updateLatestPrice()
                print("Latest Prices Completed")
                print("Finished. Sleep for: " + str(sleep_updateLatest) + " Seconds")
                time.sleep(sleep_updateLatest)
            except:
                print(right_now)
                print("updateLatest() failed.")


def updateOneHourVolume():
    while True:
        for attempt in range(10):
            right_now = datetime.datetime.now()
            try:
                print(right_now)
                print("Fetching One Hour Volume")
                MaintainVolume.fetchOneHourVolume()
                print("One Hour Volume Updated")
                print("Updating One Hour Volume")
                MaintainVolume.updateOneHourVolume()
                print("One Hour Volume Updated")
                print("OHV Finished. Sleep for: " + str(sleep_oneHourVolume) + " Seconds")
                time.sleep(sleep_oneHourVolume)
            except:
                print(right_now)
                print("updateOneHourVolume() failed.")


def updateOneDayVolume():
    while True:
        for attempt in range(10):
            right_now = datetime.datetime.now()
            try:
                print(right_now)
                print("Fetching One Day Volume")
                MaintainVolume.fetchOneDayVolume()
                print("One Day Volume Updated")
                print("Updating One Day Volume")
                MaintainVolume.updateOneDayVolume()
                print("One Day Volume Updated")
                print("ODV Finished. Sleep for: " + str(sleep_oneDayVolume) + " Seconds")
                time.sleep(sleep_oneDayVolume)
            except:
                print(right_now)
                print("updateOneDayVolume() failed.")


def deleteOldEntries():
    while True:
        for attempt in range(10):
            right_now = datetime.datetime.now()
            try:
                print(right_now)
                print("Deleting old entries in DB")
                MaintainLatest.deleteOld()
                print("Old entries deleted")
                print("Sleep for: " + str(sleep_oneHourVolume) + " Seconds")
                time.sleep(sleep_oneHourVolume)
            except:
                print(right_now)
                print("deleteOldEntries() failed.")


# Threads:
thread_itemlatest = threading.Thread(target=updateLatest)
thread_onehourvolume = threading.Thread(target=updateOneHourVolume)
thread_onedayvolume = threading.Thread(target=updateOneDayVolume)
thread_deleteold = threading.Thread(target=deleteOldEntries)


def main():
    print("Starting:")
    print("Fetching Item Mapping...")
    # OnLaunch.fetchItemMapping()
    print("Saved to Mapping.json")
    print("Comparing mapping with DB")
    OnLaunch.checkMapping()
    print("Mapping Completed")
    thread_itemlatest.start()
    thread_onehourvolume.start()
    thread_onedayvolume.start()
    thread_deleteold.start()


if __name__ == "__main__":
    main()