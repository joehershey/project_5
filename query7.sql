Select Count(Distinct Category) From Category C 
Where exists (Select Distinct ItemID from Item I where Currently > 100.0 and 
Number_of_Bids > 0 and C.ItemID = I.ItemID)

