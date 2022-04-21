Select Count (UserID) From (
    Select UserID From Seller Where Location = 'New York'
    Union
    Select UserID From Bidder Where Location = 'New York'
)