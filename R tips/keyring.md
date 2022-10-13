# Intro to `keyring`

Saving tokens and passwords in an R environment variable means they’re stored in an unencrypted, clear text file. With the keyring package, your credentials are more secure
----
The good news is that if you use R environment variables, they don’t show up in your environment tab. And, if you share your code with someone or post the code on GitHub, you won’t reveal your credentials by mistake.

Install it from CRAN with the usual `install.packages("keyring")` and then load it with `library(keyring)`.

You can then store a value in the keyring from R with the key_set() function. For example, key_set("MY_FAKE_TOKEN") to store a value for MY_FAKE_TOKEN. You’ll be asked to enter a “password,” which is actually how you enter the value you want to securely store. By using the password dialog box, you can set the value once interactively and never have to type the value in clear text.


You can then store a value in the keyring from R with the key_set() function. For example, key_set("MY_FAKE_TOKEN") to store a value for MY_FAKE_TOKEN. You’ll be asked to enter a “password,” which is actually how you enter the value you want to securely store. By using the password dialog box, you can set the value once interactively and never have to type the value in clear text.

```r
key_set("MY_FAKE_TOKEN")
```

The best way to use a value that’s stored in a keyring is as an argument within a function. That way, the actual values never show up in your environment tab or history, as they would if you stored the value in a new variable in your script.

You can access the value with the key_get() function, such as key_get("MY_FAKE_TOKEN"), and then use it in an argument such as setting an option: 

```r
options(googleAuthR.client_id = key_get("MY_FAKE_TOKEN"))
```

This still isn’t very secure. It’s a big improvement that your credentials are stored in an encrypted keyring. But anyone who can access your machine and knows about the keyring package can still get to your credentials. keyring_list() will show all the available entries in the keyring, if not their values.

To add a layer of security, you can create a keyring that’s password-protected within R. Do that with keyring_create() and the name of a new keyring, such as keyring_create("Rcredentials").

```r
keyring_create("Rcredentials")
```

You’ll be asked for a password using the same type of password dialog box as when setting a value with the key_set() function.

You can unlock a password-protected keyring called Rcredentials at the start of an R session with 

```r
keyring_unlock("Rcredentials")
```
Now you can set a value for a new token, specifying the new keyring, with code such as:

```r
key_set("NEW_FAKE_TOKEN", keyring ="Rcredentials")
```


And, you can retrieve a value the same way as before, but specifying the keyring

```r
key_get("NEW_FAKE_TOKEN", keyring ="Rcredentials")
```

Finally, you can lock the keyring at the end of your script with

```r
keyring_lock("Rcredentials")
```

After locking the keyring, if you (or anyone else) run 

```r
key_get("NEW_FAKE_TOKEN") 
```

you (or they) will be asked for the keyring password.

As an example for securing a acces to A SQL server you could the following

```r
require(keyring)
require(RMySQL)
keyring::keyring_create("set_keyring_password_here") #Remember this password
keyring::key_set("dbname", keyring = "Your_set_keyring_password_here") 
keyring::key_set("host", keyring = "Your_set_keyring_password_here")
keyring::key_set("port", keyring = "Your_set_keyring_password_here")
keyring::key_set("user", keyring = "Your_set_keyring_password_here")
keyring::key_set("pass", keyring = "Your_set_keyring_password_here")
keyring::key_set("unix.sock", keyring = "Your_set_keyring_password_here")

m<-MySQL() #set the driver to mysql check your database driver and edit
summary(m)
    con<-dbConnect(m, dbname = keyring::key_get("dbname",
                      keyring = "Your_set_keyring_password_here"),
                   host=keyring::key_get("host",
                      keyring = "Your_set_keyring_password_here"),
                   port=as.numeric(keyring::key_get("port",
                      keyring = "Your_set_keyring_password_here")),
                   user=keyring::key_get("user",
                      keyring = "Your_set_keyring_password_here"),
                   pass=keyring::key_get("pass",
                      keyring = "Your_set_keyring_password_here"),
                   unix.sock=keyring::key_get("unix.sock",
                      keyring = "Your_set_keyring_password_here"),
                     )
keyring::keyring_lock("Your_set_keyring_password_here") #Lock keyring after using it.
```