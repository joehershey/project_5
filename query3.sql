Select Count(Distinct ItemID) 
From (Select ItemID From Category Group By ItemID Having Count(ItemID) = 4 )