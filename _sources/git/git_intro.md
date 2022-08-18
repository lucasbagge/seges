# Git 

![](gitlogo.png)

it is used for version control. 

## GitHub CLI: Brings GitHub to Your Terminal

If you create a local folder before creating a GitHub repository for it, you might need to go to the GitHub website then create a new repository, then add a remote to your current folder. Is there any way that all of these steps could be done in the terminal in 1 line of code?

That is when GitHub CLI comes in handy. The code snippet below shows how to create a new Github repository in your local folder.

```
$ cd your_local_folder

# Create an empty local git repo
$ git init
```

## Create a new GitHub repo

```
$ gh repo create
```

With GitHub CLI, you can also manage your pull requests, issues, repositories, gists, and so much more! Check out GitHub CLI here.

Pull One File from Another Branch Using Git
Pull the files from another branch into your branch can be messy. What if you just want to pull one file from another branch? You can easily to like that with the code snippet below:

## downloads contents from remote repository
```
$ git fetch

# navigate to another branch
$ git checkout

# adds a change in the working directory to the staging area
$ git add 

# captures the state of a project at that point in time
$ git commit
```

Now you just update one file in your branch without messing with the rest!