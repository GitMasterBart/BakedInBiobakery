drop table if exists Users;

CREATE TABLE Users(username char(4)
                  , userID int not null AUTO_INCREMENT
                  , primary key(userID));