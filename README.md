Handles creation and deletion of simple pastes.  
Designed as a personal and self-hosted alternative to services such as paste.rs.
---
Start Server  
`sudo python3 src/server.py <ip> <storage dir> <password dir>`   
   
Add Paste (Will return id)   
`curl --data @<file.txt> <ip>/paste/create?pass=<pass>`   
   
Delete Paste (Will return success)   
`curl <ip>/paste/delete?id=<id>&pass=<pass>`  