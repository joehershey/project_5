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
    Name CHAR(256), 
    Location CHAR(256), 
    Country CHAR(256), 
    Buy_Price FLOAT, 
    Currently FLOAT,
    UserID CHAR(256),
    Description CHAR(1000),
    PRIMARY KEY(ItemID)
    FOREIGN KEY (UserID)
        REFERENCES Seller(UserID)
);

create table Bid (
    Amount INT, 
    ItemID INT, 
    Time DATETIME,
    UserID CHAR(256),
    PRIMARY KEY(UserID, Time)
    FOREIGN KEY (ItemID)
        REFERENCES Item(ItemID)
);

create table Seller (
    Rating INT,
    UserID CHAR(256),
    Location CHAR(256), 
    Country CHAR(256), 
    ItemID INT,
    PRIMARY KEY(UserID,ItemID)

);

create table Bidder (
    Rating INT,
    UserID CHAR(256),  
    Location CHAR(256),
    Country CHAR(256),
    PRIMARY KEY(UserID)
);

create table Category (
    ItemID INT, 
    Category CHAR(256),
    PRIMARY KEY(ItemID, Category)
);

