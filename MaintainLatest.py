import mysql.connector
import requests
import json
import datetime
import osrsPriceSetLists


def fetchLatestPrices():
    latest_url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
    response = requests.get(latest_url, headers={'User-Agent': 'Item Set Prices Checker - YOURDISCORDINFO '}).json()
    with open("jsonfiles/LatestPrices.json", "w") as write_file:
        json.dump(response, write_file)


def updateLatestPrice():
    # Prepared SQL statements
    insert_latest = ("INSERT INTO itemlatest "
                     "(itemID, itemHigh, itemHighTime, itemLow, itemLowTime) "
                     "VALUES (%s,%s,%s,%s,%s)")
    update_high = ("UPDATE itemlatest "
                   "SET itemHigh = %s, itemHighTime = %s "
                   "WHERE itemID = %s")
    update_low = ("UPDATE itemlatest "
                  "SET itemLow = %s, itemLowTime = %s "
                  "WHERE itemID = %s")
    select_itemlatest = ("SELECT * FROM itemlatest "
                         "WHERE itemID = %s;")
    sql_insert_high = ("INSERT INTO itemhightimes "
                       "(ItemID, itemHigh, itemHighTime)"
                       "SELECT itemID, itemHigh, itemHighTime FROM itemlatest "
                       "WHERE itemID = %s")
    sql_insert_low = ("INSERT INTO itemlowtimes "
                      "(ItemID, itemLow, itemLowTime)"
                      "SELECT itemID, itemLow, itemLowTime FROM itemlatest "
                      "WHERE itemID = %s")
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices",
                                        port=3303)
    cursor = connectDB.cursor()
    # Read from file and save to database:
    with open("jsonfiles/LatestPrices.json", "r") as read_file:
        data = json.load(read_file)
        for a in osrsPriceSetLists.allItemIDs:
            try:
                for dict in data:
                    hTime = datetime.datetime.fromtimestamp(data['data'][str(a)]['highTime']).strftime('%Y-%m-%d %H:%M:%S')
                    lTime = datetime.datetime.fromtimestamp(data['data'][str(a)]['lowTime']).strftime('%Y-%m-%d %H:%M:%S')
                    query_tuple = (str(a),)
                    cursor.execute(select_itemlatest, query_tuple)
                    myresult = cursor.fetchone()
                    insert_touple = [str(a), data['data'][str(a)]['high'], hTime, data['data'][str(a)]['low'], lTime]
                    if myresult is None:
                        print("Inserting: " + str(a))
                        cursor.execute(insert_latest, insert_touple)
                        connectDB.commit()
                    else:
                        # If both times are equal:
                        if str(myresult[2]) == str(hTime) and str(myresult[4]) == str(lTime):
                            print("ItemLatest: Up to date: " + str(a))
                        if str(myresult[2]) < str(hTime):
                            print("Updating Item Latest High: " + str(a))
                            # Copy to hightimes
                            cursor.execute(sql_insert_high, query_tuple)
                            connectDB.commit()
                            # update
                            update_high_tuple = (data['data'][str(a)]['high'], hTime, str(a))
                            cursor.execute(update_high, update_high_tuple)
                            connectDB.commit()
                        if str(myresult[4]) < str(lTime):
                            print("Updating Item Latest Low: " + str(a))
                            # copy to lowtimes
                            cursor.execute(sql_insert_low, query_tuple)
                            connectDB.commit()
                            update_low_tuple = (data['data'][str(a)]['low'], lTime, str(a))
                            cursor.execute(update_low, update_low_tuple)
                            connectDB.commit()
            except KeyError:
                print("Failed. Could not find data on item: " + str(a))
            except Exception as e:
                print("Exception error: ", e)
    connectDB.commit()
    cursor.close()
    connectDB.close()


def deleteOld():
    # SQL:
    delete_old_high = ("DELETE FROM itemhightimes "
                  "WHERE itemHighTime < now() - INTERVAL 30 DAY;")
    delete_old_low = ("DELETE FROM itemlowtimes "
                       "WHERE itemLowTime < now() - INTERVAL 30 DAY;")
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices",
                                        port=3303)
    cursor = connectDB.cursor()
    cursor.execute(delete_old_high)
    connectDB.commit()
    cursor.execute(delete_old_low)
    connectDB.commit()
    cursor.close()
    connectDB.close()
