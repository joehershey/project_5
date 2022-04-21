
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Transform string to escape double quotes and surrond with quotes
"""

def transformString(str):
    str = str.replace('"', '""')
    newStr = "\"" + str + "\""
    return newStr

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f, open("Seller.dat", 'a') as seller_f, open("Category.dat", 'a') as category_f, open("Item.dat", 'a') as item_f, open("Bidder.dat", 'a') as bidder_f, open("Bid.dat", 'a') as bid_f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            # Seller(Rating, *UserID, Location, Country, **ItemID)
            seller = item["Seller"] #contains other fields
            s_rating = seller["Rating"]
            s_id = seller["UserID"]
            if "Location" in item.keys():
                location = transformString(item["Location"])
            else:
                location = "NULL"
            if "Country" in item.keys():
                country = transformString(item["Country"])
            else:
                country = "NULL"
            item_id = item["ItemID"]
            seller_data = s_rating + "|" + s_id + "|" + location + "|" + country + "|" + item_id + "\n"
            
            seller_f.write(seller_data)

            
            bids = item["Bids"] #its a list
            if bids != None:
                #
                for bid_dict in bids:
                    bid = bid_dict["Bid"]
                    bidder = bid["Bidder"]
                    
                    b_rating = bidder["Rating"]
                    b_id = transformString(bidder["UserID"])
                    if "Location" in bidder.keys():
                        b_location = transformString(bidder["Location"])
                    else:
                        b_location = "NULL"
                    if "Country" in bidder.keys():
                        b_country = transformString(bidder["Country"])
                    else:
                        b_country = "NULL"

                    time = transformDttm(bid["Time"])
                    amount = transformDollar(bid["Amount"])
                    # Bidder(Rating, *UserID, Location, Country, **ItemID)
                    
                    """f.write(b_rating+columnSeparator+b_id+columnSeparator+b_location
                                +columnSeparator+b_country+columnSeparator+item_id+"\n")"""
                    bidder_f.write(b_rating+columnSeparator+b_id+columnSeparator+b_location
                            +columnSeparator+b_country+"\n")
                    
                    #Bid (*UserID, Amount, *Time, **ItemID)
                    bid_f.write(b_id+columnSeparator+amount
                            +columnSeparator+time+columnSeparator+item_id+"\n")

            cate_list = item["Category"] #its a list
            """with open("Category.txt", 'a') as f:
                        f.write(','.join(cate_list)+columnSeparator+item_id+"\n")"""
            for category in cate_list:
                category_f.write(item_id+columnSeparator+transformString(category)+"\n")
            
            name = transformString(item["Name"])
            current = transformDollar(item["Currently"]) #transformDollar
            first_bid = transformDollar(item["First_Bid"]) #transformDollar
            number_of_bids = item["Number_of_Bids"]
            if "Buy_Price" in item.keys():
                buy_price = transformDollar(item["Buy_Price"])
            else:
                buy_price = "NULL"
            started = transformDttm(item["Started"]) #transformDttm
            ends = transformDttm(item["Ends"]) #transformDttm
            if  "Description" in item.keys() and item["Description"] is not None:
                description = transformString( item["Description"] )
            else:
                description = "NULL"
           

            #Item (*ItemID, Started, Ends, Number_of_Bids, First_Bid, Name, Location, Country, Buy_Price, Currently, UserID(ofseller)?)
            item_data = (item_id + columnSeparator + started + columnSeparator + ends + columnSeparator + number_of_bids +
                         columnSeparator + first_bid + columnSeparator + name + columnSeparator + location + columnSeparator +
                         country + columnSeparator + buy_price + columnSeparator + current + columnSeparator + s_id + 
                         columnSeparator + description + "\n")
            
            item_f.write(item_data)
            
            


"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    #clear the dat files
    with open("Seller.dat", 'w') as f:
        f.write("")
    with open("Bidder.dat", 'w') as f:
        f.write("")
    with open("Bid.dat", 'w') as f:
        f.write("")
    with open("Category.dat", 'w') as f:
        f.write("")
    with open("Item.dat", 'w') as f:
        f.write("")
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print ("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)
