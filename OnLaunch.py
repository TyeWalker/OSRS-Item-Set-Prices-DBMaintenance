import mysql.connector
import requests
import json
import osrsPriceSetLists


# Item Mapping:
def fetchItemMapping():
    # URL:
    url = "https://prices.runescape.wiki/api/v1/osrs/mapping"
    # Save data to JSON file
    response = requests.get(url, headers={'User-Agent': 'Item Set Prices Checker - YOURDISCORDINFO'}).json()
    with open("jsonfiles/Mapping.json", "w") as write_file:
        json.dump(response, write_file)


# Check Mapping:
def checkMapping():
    # SQL Prepared Statements:
    # Add item:
    add_item = ("INSERT INTO item "
                "(itemID, ItemName, itemGELimit, itemHighAlch) "
                "VALUES (%s,%s,%s,%s)")
    # Select item by itemID:
    select_item = ("SELECT * FROM item WHERE itemID = '%s'")
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices",
                                        port=3303)
    cursor = connectDB.cursor()
    with open("jsonfiles/Mapping.json", "r") as read_file:
        data = json.load(read_file)
        for a in osrsPriceSetLists.allItemIDs:
            for dict in data:
                if a == dict['id']:
                    select_tuple = (a, )
                    cursor.execute(select_item, select_tuple)
                    myresult = cursor.fetchone()
                    if myresult is None:
                        # Add to DB:
                        add_tuple = (a, dict['name'], dict['limit'], dict['highalch'])
                        cursor.execute(add_item, add_tuple)
                        connectDB.commit()
        connectDB.commit()
        cursor.close()
        connectDB.close()