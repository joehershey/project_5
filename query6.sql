Select Count(*) From 
(Select UserID From Seller 
Intersect 
Select UserID From Bidder)