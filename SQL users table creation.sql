use CalorieCounter;
CREATE TABLE users (
Userid int IDENTITY(1,1) PRIMARY KEY,
Email varchar(255) NOT NULL,
Username varchar(255) NOT NULL,
Password_ varchar(255) NOT NULL,
IsGoalSet BIT,
GoalSet int)