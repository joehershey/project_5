CREATE TABLE Buys(
    prodname CHAR(40),
    prodcategory CHAR(20),
    ssn CHAR(11),
    date DATE,
    PRIMARY KEY(prodname,prodcategory,ssn)
    FOREIGN KEY (ssn) 
        REFERENCES Person,
    FOREIGN KEY (prodname, prodcategory) 
        REFERENCES Product(name, category))


drop table if exists Seller;
drop table if exists Bidder;
drop table if exists Bid;
drop table if exists Category;
drop table if exists Item;
create table Item (
    ItemID INT, 
    Started DATETIME, 
    Ends DATETIME, 
    Number_of_Bids INT, 
    First_Bid FLOAT, 
    Name CHAR(), 
    Location CHAR(), 
    Country CHAR(), 
    Buy_Price FLOAT, 
    Currently FLOAT, 
    UserID CHAR()
);

create table Item (
    ItemID INT, 
    Started DATETIME, 
    Ends DATETIME, 
    Number_of_Bids INT, 
    First_Bid FLOAT, 
    Name CHAR(), 
    Location CHAR(), 
    Country CHAR(), 
    Buy_Price FLOAT, 
    Currently FLOAT, 
    UserID CHAR()
);