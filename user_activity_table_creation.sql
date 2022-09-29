use CalorieCounter;
CREATE TABLE user_activity (
Userid int,
Date1 date not null,
Amount1 int,
Amount2 int,
Amount3 int,
Amount4 int,
Amount5 int,
DailyTotal int);
update  user_activity
set     Date1 = getdate()
where   Userid = Userid;
