# Conenction to Database

## Connect to MFA

Azure AD MFA helps safeguard access to data and applications while meeting user demand for a simple sign-in process. It delivers strong authentication with a range of easy verification options (phone call, text message, smart cards with pin, or mobile app notification), allowing users to choose the method they prefer. Interactive MFA with Azure AD can result in a pop-up dialog box for validation.

### With R

```r
library(odbc)
library(tidyverse)
library(DBI)

server <- "eoe-rating-dev-sqls.database.windows.net"
database = "eoe-rating-dev-sqldb"
username ='lucb@seges.dk'
con <- DBI::dbConnect(odbc::odbc(), 
                      UID = username,
                      Driver="ODBC Driver 17 for SQL Server",
                      Server = server,
                      Database = database,
                      Authentication = "ActiveDirectoryInteractive")

res <- dbGetQuery(con,'
  SELECT * FROM [stg].[KonjukturVariable]
') %>% 
  as_tibble()

res %>% 
  head()
```

### With Python

```python
import pyodbc
import pandas as pd
server = 'eoe-rating-dev-sqls.database.windows.net'
database = 'eoe-rating-dev-sqldb'
username ='lucb@seges.dk'
Authentication='ActiveDirectoryInteractive'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+
                      ';SERVER='+server+
                      ';PORT=1433;DATABASE='+database+
                      ';UID='+username+
                      ';AUTHENTICATION='+Authentication
                      )

print(conn)

df = pd.read_sql("SELECT * FROM [stg].[KonjukturVariable]", conn) 
df.head()

conn.close()
```