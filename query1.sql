--Select Distinct Sellers and Bidder’s ID, From (Seller, Bidder)

Select Count (UserID) From (
    Select UserID From Seller
    Union
    Select UserID From Bidder
)
