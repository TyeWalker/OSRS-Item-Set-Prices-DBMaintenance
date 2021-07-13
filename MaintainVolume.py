import mysql.connector
import requests
import json
import osrsPriceSetLists


def fetchOneHourVolume():
    one_hour_volume = 'https://prices.runescape.wiki/api/v1/osrs/1h'
    response = requests.get(one_hour_volume, headers={'User-Agent': 'Item Set Prices Checker - YOURDISCORDINFO'}).json()
    with open("jsonfiles/OneHourVolume.json", "w") as write_file:
        json.dump(response, write_file)


def fetchOneDayVolume():
    one_day_volume = 'https://prices.runescape.wiki/api/v1/osrs/24h'
    response = requests.get(one_day_volume, headers={'User-Agent': 'Item Set Prices Checker - YOURDISCORDINFO'}).json()
    with open("jsonfiles/OneDayVolume.json", "w") as write_file:
        json.dump(response, write_file)


def updateOneHourVolume():
    # Prepared SQL statements:
    select_onehourvolume = ("SELECT * FROM onehourvolume "
                            "WHERE itemID = %s;")
    insert_onehourvolume = ("INSERT INTO onehourvolume "
                            "(itemID, ohHighPriceVolume, ohLowPriceVolume) "
                            "VALUES (%s, %s, %s)")
    update_onehourvolume_high = ("UPDATE onehourvolume "
                                 "SET ohHighPriceVolume = %s "
                                 "WHERE itemID = %s")
    update_onehourvolume_low = ("UPDATE onehourvolume "
                                "SET ohLowPriceVolume = %s "
                                "WHERE itemID = %s")
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices",
                                        port=3303)
    cursor = connectDB.cursor()
    with open("jsonfiles/OneHourVolume.json", "r") as read_file:
        data = json.load(read_file)
        for a in osrsPriceSetLists.allItemIDs:
            try:
                query_tuple = (str(a),)
                cursor.execute(select_onehourvolume, query_tuple)
                myresult = cursor.fetchone()
                if myresult is None:
                    insert_first_tuple = (str(a), 0, 0)
                    cursor.execute(insert_onehourvolume, insert_first_tuple)
                    connectDB.commit()
                if data['data'][str(a)]['highPriceVolume'] is None:
                    insert_high_nodata = (0, a)
                    cursor.execute(update_onehourvolume_high, insert_high_nodata)
                    connectDB.commit()
                if data['data'][str(a)]['lowPriceVolume'] is None:
                    insert_low_nodata = (0, a)
                    cursor.execute(update_onehourvolume_low, insert_low_nodata)
                    connectDB.commit()
                if data['data'][str(a)]['highPriceVolume'] is not None:
                    insert_high_data = (data['data'][str(a)]['highPriceVolume'], a)
                    cursor.execute(update_onehourvolume_high, insert_high_data)
                    connectDB.commit()
                if data['data'][str(a)]['lowPriceVolume'] is not None:
                    insert_low_data = (data['data'][str(a)]['lowPriceVolume'], a)
                    cursor.execute(update_onehourvolume_low, insert_low_data)
                    connectDB.commit()
            except KeyError:
                print("Could not find data on item (One Day Volume): " + str(a))
            except Exception as e:
                print("Exception error: ", e)
    connectDB.commit()
    cursor.close()
    connectDB.close()


def updateOneDayVolume():
    # Prepared SQL statements:
    select_onedayvolume = ("SELECT * FROM onedayvolume "
                           "WHERE itemID = %s;")
    insert_onedayvolume = ("INSERT INTO onedayvolume "
                           "(itemID, odHighPriceVolume, odLowPriceVolume) "
                           "VALUES (%s, %s, %s)")
    update_onedayvolume_high = ("UPDATE onedayvolume "
                                "SET odHighPriceVolume = %s "
                                "WHERE itemID = %s")
    update_onedayvolume_low = ("UPDATE onedayvolume "
                               "SET odLowPriceVolume = %s "
                               "WHERE itemID = %s")
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices",
                                        port=3303)
    cursor = connectDB.cursor()
    with open("jsonfiles/OneDayVolume.json", "r") as read_file:
        data = json.load(read_file)
        for a in osrsPriceSetLists.allItemIDs:
            try:
                query_tuple = (str(a),)
                cursor.execute(select_onedayvolume, query_tuple)
                myresult = cursor.fetchone()
                if myresult is None:
                    insert_first_tuple = (str(a), 0, 0)
                    cursor.execute(insert_onedayvolume, insert_first_tuple)
                    connectDB.commit()
                if data['data'][str(a)]['highPriceVolume'] is None:
                    insert_high_nodata = (0, a)
                    cursor.execute(update_onedayvolume_high, insert_high_nodata)
                    connectDB.commit()
                if data['data'][str(a)]['lowPriceVolume'] is None:
                    insert_low_nodata = (0, a)
                    cursor.execute(update_onedayvolume_low, insert_low_nodata)
                    connectDB.commit()
                if data['data'][str(a)]['highPriceVolume'] is not None:
                    insert_high_data = (data['data'][str(a)]['highPriceVolume'], a)
                    cursor.execute(update_onedayvolume_high, insert_high_data)
                    connectDB.commit()
                if data['data'][str(a)]['lowPriceVolume'] is not None:
                    insert_low_data = (data['data'][str(a)]['lowPriceVolume'], a)
                    cursor.execute(update_onedayvolume_low, insert_low_data)
                    connectDB.commit()
            except KeyError:
                print("Could not find data on item (One Hour Volume): " + str(a))
            except Exception as e:
                print("Exception error: ", e)
    connectDB.commit()
    cursor.close()
    connectDB.close()


