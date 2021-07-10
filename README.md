# Simple Player Level API

## GETs
https://\<URL\>/players/all - returns an array of player/level json
https://\<URL\>/players/get?name=\<name\> - returns a json of the player/level matching name

## POSTs
https://\<URL\>/players/add?name=\<name\>&level=\<level\> - adds a player/level to the database
https://\<URL\>/players/delete?name=\<name\>&level=\<level\> - deletes a player/level to the database
https://\<URL\>/players/update?name=\<name\>&level=\<level\> - updates a player with a new level

https://\<URL\>/players/resetallplease - removes all player/level records from the database
