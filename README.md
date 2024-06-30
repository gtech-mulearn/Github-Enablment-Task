# General Enablement| Git & Github

ഈ assignment ഇന്റെ നീട്ടം നോക്കണ്ട 😂  All is well. നമുക്ക് പതിയെ ചോദിച്ചു ചോദിച്ചു ചെയ്യാം.

### Let’s version control it!

Just like knowing how to use the Command Line, Git & Github will be very important in your daily workflow as a programmer / developer. 

Let’s put your Git and GitHub skills to practice! Find the assignment below.

1. The assignment has to be done strictly in a PC.
2. You can either use WSL and ubuntu from your windows machine or use any Linux OS as standalone or use a virtualbox with any Linux OS in it.
3. Do not do the assignment in **powershell or cmd.**

### **Check if Git is installed:**

1. Try the command `git --version` in your shell. If it returns a git version, it means git is installed. If it shows an error message, you need to install git.
2. Go to https://git-scm.com/downloads to download git for your OS. (If you’re using WSL and doesn’t have git, choose Linux/Unix version of git when downloading)

### **Configuring Git:**

Once Git is installed setup your global config values if you haven’t. Run the commands:

```
git config --global user.name "Your Name"
git config --global user.email "email@something.com"
```

Replace the parts in quotes with your info.

Setup is done! You’re good to go.

### **Configuring GitHub:**

Create an account in https://github.com/ → Sign Up.

### **Setting up SSH keys:**

You might wonder what really this is, and why you need to do this setup (എന്തിനു നിങ്ങൾ ഇത് ചെയ്യണം?)

Let’s refer to our machine as ‘local machine’, where we use git ‘locally’ for version control. We refer to GitHub as ‘remote’, this is where we push our project files to using git from our local machine.

So, GitHub is a service something like Google drive. To save our files or to make changes to our data in Google drive we need to login with our google account. Right? The same applies for GitHub. GitHub needs to know it is the right user trying to push files to a particular GitHub account. (ആരാണെന്നു മനസിലായില്ലെങ്കിൽ GitHub സമ്മയ്ക്കൂല 🤧 )

So the question is how would GitHub know it is you, the right user trying to push files to a particular GitHub account from a local machine using git?

**Using SSH Keys(Linux/Mac) (താക്കോൽ എവിടെ?** 🤔 **)**
GitHub has the feature to use SSH keys to establish a secure, authenticated way of data transfer. It would basically ensure you are the right user. So let’s setup SSH keys for your GitHub account. 

This wasn’t covered in the session, but it’s fairly easy to do. Follow the steps below.

1. Open your terminal.
2. Make sure you are in your home directory. (It will show a ~)
3. Type `ls -a` It will list all hidden files. See if you can find. the `.ssh` directory in it.
4. If you can’t find it in the list, create the `.ssh` directory.
5. Now, let’s generate an SSH key pair. Use the command
 `ssh-keygen -t ed25519 -C*"your_email@example.com"*`
6. It will ask you for a file to save the key. Press Enter for now.
7. You will now be asked for a passphrase. You don’t have to set a passphrase. You can press Enter twice.
8. You’ve now created a SSH private and public key. We will be using the private key in your local machine and we’ll add the public key to your Github.
9. Now do the command `eval "$(ssh-agent -s)"` It will start an ssh agent in the background.
10. Now let’s add you ssh key to the ssh-agent.
11. Do the command `ssh-add ~/.ssh/id_ed25519` 

You’ve now successfully created and added your SSH key to your local machine. (നമ്മൾ പൊളി ആണ് ⚡)

**Adding SSH key to your GitHub account**

As we mentioned before, your GitHub needs to know it is the right user trying to connect with GitHub from a local machine. 

So we’ll add the public key of your SSH to your GitHub account. Follow from step 1 in this link to add your SSH public key to your GitHub account.

https://docs.github.com/en/enterprise-server@3.1/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

Now as we said earlier, you’ve successfully setup an authentication method between Github( the remote), and your local machine. Hip Hip Hurray! 🥂 (പെവെർ 😎 💪 )

**Using HTTPS**

1. If you are a Windows user, you skip the SSH part and clone the github repository using the HTTPS Option, mentioned in the clone button.
2. Just copy the link from the clone button, and use the `git clone [link]` command to clone the repository

**The Assignment:**

1. Let’s write a book! You’re building a book app. It has the feature for the author to add a book. We’ll be working on that feature of the app today. (Don’t worry we’ll be using text files for now)
2. Fork this repo - [](https://github.com/gtech-mulearn/Github-Enablment-Task)https://github.com/gtech-mulearn/Github-Enablment-Task
3. Once the fork is made, clone the repo using the SSH option/HTTP Option. (Google if you don’t know how to)
4. After you’ve cloned it locally, do the list command, you should be able to see the repo now.
5. Change directory into the cloned repo folder.
6. Make a new branch called `develop`
7. Do a `git status` 
8. You should now be able to see that the working tree is clean.
9. Make another directory in the root of the app, with your **full name.** Eg: `bijoy_sijo_book_app`
10. Change directory into it. 
11. Now, create another directory inside your book app directory called `add_books_feature` 
12. Let’s build some features in it now!
13. Now let’s make two text files in your books_feature directory.
    1. Add a `create_book.txt` file.
    2. Add the text `"This is the feature for the author to add a new book."` in to the create_book.txt file.
    3. Let’s commit your change now. 
    4. Next, create another file named `list_all_books.txt`
    5. Add the text `“This is the feature which shows the user all the books they’ve created as a list.”` to the list_all_books.txt
    6. Let’s add your change now. 
14. Uh oh! You just realised that you don’t need to add the change made to list_all_books.txt now.
15. Unstage the list_all_books.txt. (If you don’t know the command, try a `git status` and read the output 😉. or Google for it)
16. You realise that, since, list_all_books.txt is another feature, you decide to complete developing it on another branch. **Checkout to main branch first** and then create a new branch called `feature` and commit the list_all_books.txt file and it’s changes in that branch.
17. In the same feature branch, now let’s make another change, to your list_all_books.txt file add the text `"List all books will list all books in ascending order."` without deleting the first line, You just added a new feature and Ideally you should have 2 lines in list_all_books.txt now.
18. Check the log to see the changes you’ve made so far.
19. Let’s commit it. Your feature branch should ideally have a minimum of two commits now. 
20. Now, to push back your changes and conrtibute your code to the GTech µLearn Github repository, you need to raise a Pull Request (പേടിക്കണ്ട നമുക്ക് സെറ്റ് ആക്കാം).
21. But before that, remember that you now have two different branches, namely, `develop` and `feature` The commits you made so far are in two branches. Let’s merge them together to get a complete project with all features and then push back to the GTech µLearn Github to raise a Pull Request.
22. Checkout to the `develop` branch and then merge the `feature` branch into develop branch. 
23. Once the merge is complete. Push the develop branch to the remote.
24. Navigate to your forked repo in your Github.
25. Find the option to open a PR. Open your PR from your develop branch to the main branch of the GTech µLearn repo. Give your PR a meaningful title and description. Open the PR.

You’re a superstar! You just learned the basic Git & Github workflow! 🥳  

### Assignment Submission

Now if you go to the pull requests tab in GTech µLearn repo, you’ll be able to see your pull request. Open it and copy your pull request URL.

1. Submit the link in #task-dropbox channel with the hashtag, `#ge-intro-to-github`
2. With your submission, feel free to drop in a small note about your experience with doing this assignment. 😄  We’d be delighted to read it.

### Resources

Refer to the session recording here → [https://www.youtube.com/watch?v=Bg2U_Cgp3K0&ab_channel=GTechµLearn](https://www.youtube.com/watch?v=Bg2U_Cgp3K0&ab_channel=GTech%C2%B5Learn)

Google is your best friend. You can refer to other simple Git and GitHub videos in YouTube.
