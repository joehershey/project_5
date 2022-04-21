Select Count(Distinct Category) From Category, 
(Select Distinct ItemID From Bid Where Amount > 100)a 
Where Category.ItemID = a.ItemID