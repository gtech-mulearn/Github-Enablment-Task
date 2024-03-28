# General Enablement | Github Desktop

## About

This is a simplified version of [original task](./README.md). Sometimes it's too hard to deal with command lines, and it's much easier to do the same using a Graphical User Interface. [Github Desktop](https://desktop.github.com/) is a GUI software released by Github themselves. This helps us do things just with 2 or 3 button clicks instead of running all those commands. `I think as a beginner it is better to start with GUI and later move on to a Command line.` Let's get started with our task [#ge-intro-to-github](https://discordapp.com/channels/771670169691881483/1115381777792499805/1115716726533931009).

> [Github Desktop](https://desktop.github.com/) is only available for windows and mac.

## Creating a Github Account

> The first step is to get yourself a Github account.

Let's see How, Goto [github.com](https://github.com/signup) and crete an account. If you already have an account, login to it.

## Cloning Task Repository

> The second step is to clone our task repository.

<p id="forkRepo">Let's see How, </p>

1. Goto [Task repository](https://github.com/gtech-mulearn/Github-Enablment-Task).

   ![1. Goto task repository](./z.githubDesktopTutorials/2.png)

2. Click on the `fork` Button

   ![fork](./z.githubDesktopTutorials/3.png)

3. In the next window opened, click on `create fork`

   ![create fork](./z.githubDesktopTutorials/4.png)

4. Now a copy/clone of the task repository has been created in your github account.

> Let's Install Github Desktop.

## Installing Github Desktop

1. Goto [desktop.github.com](https://desktop.github.com/).

2. Select and download package for your OS (Only available for windows and mac). Windows users could choose between [.exe file](https://central.github.com/deployments/desktop/desktop/latest/win32) or [.msi file](https://central.github.com/deployments/desktop/desktop/latest/win32?format=msi).

3. After downloading the file, install the software as usual and open it.

This is the basic Interface of Github.
![Github Desktop Home screen on launch](./z.githubDesktopTutorials/1.png)

Now it's time to connect Github Desktop with your Github account.

## Connecting Github Desktop with your Github Account

> You must connect Github Desktop with your Github account to continue with this task.

Let's see How,

1. Open Github Desktop and click on `Clone a repository from the internet` button.
   ![Clone a repository from the internet button](./z.githubDesktopTutorials/5.png)

2. In the pop-up. Select the first tab `Github.com` and click on `sign in`.
   ![Select the first tab Github.com and click on sign in](./z.githubDesktopTutorials/6.png)

3. In the next pop-up select `continue with browser` option.
   ![select continue with browser](./z.githubDesktopTutorials/7.png)

4. Now you'll be redirected to your browser. If you had logged into your github account, you'll see a popup like this. If not, then login to your github account and the pop-up will show up. Click on the `open github desktop` option in the pop-up.
   ![click on the open github desktop option in the pop-up](./z.githubDesktopTutorials/8.png)

5. Then you'll be redirected to Github Desktop and you could see all your repositories there.
   ![click on the open github desktop option in the pop-up](./z.githubDesktopTutorials/9.png)

## Let's create a local copy of our task repo.

> To continue with the task, you need to clone the task repository to your computer.

Let's see How,

1. After connecting your Github Account with Github desktop, you can see a pop-up like that in the previous image. In the search bar there search for `Github-Enablment-Task` and select the repository.( Make sure you had <a href="#forkRepo">forked the repository</a>)
   ![search for Github-Enablment-Task and select that repository](./z.githubDesktopTutorials/10.png)

> If you lost that pop-up, then press `ctrl+shift+O` or goto `files` in the menubar and select `clone a repository` option to get that pop-up again.

2. Click on the `clone` button and it'll start cloning the repository. Make sure to choose an approppriate location to clone the repository.
   ![cloning the repository](./z.githubDesktopTutorials/11.png)

3. It'll take sometime for the cloning to complete based on your network speed. After cloning is completed, another pop-up will show up. There click on the `contribute to the parent project` option then select `continue`.
   ![cloning the repository](./z.githubDesktopTutorials/12.png)

> Just like that, you've successfully completed the first steps. Now let's begin the task.

## The Assessment

> **Let’s write a book!** Assume that you’re building a book app. It has the feature for the author to add a book. We’ll be working on that feature of the app today. (Don’t worry we’ll be using text files for now). The aim of this task is to get you familiarise with basic Git and Github operations.

Let's start the task.

1. Open Github Desktop.

2. <p id="createBranch"> Lets create another <mark>branch</mark> named <mark>develop</mark>. </p> 
   Let's see How,

   - Click on the box named `current branch` in the right side of Github Desktop. We can create and manage new branches there.
  ![current branch](./z.githubDesktopTutorials/21.png)

   - Now a pop-up will appear. There click on the `new branch` button.
      ![in the first text box there type develop and click on new branch option.](./z.githubDesktopTutorials/22.png)

   - In the next pop-up enter `develop` in the text box and click on `create branch` button to create a new branch `develop`.
      ![enter develop in the text box and click on create branch button to create a new branch develop](./z.githubDesktopTutorials/23.png)

   - In the next pop-up select the second option `bring my changes to develop` and click on the `switch branch`.
   ![select the second option bring my changes to develop and click on the switch branch.](./z.githubDesktopTutorials/24.png)

3. After creating the `develop` branch, press `ctrl+shift+F` or click on `repository` in the menubar and select `show in explorer` there to open the folder containing the repository.
   ![open the folder containing the repository](./z.githubDesktopTutorials/13.png)

4. Inside that folder, create another folder in the format `yourname_book_app`. eg: `christo_john_book_app`.
   ![create folder in the format yourname_book_app](./z.githubDesktopTutorials/14.png)

5. Open that folder and create another folder named `add_books_feature`.

   ![ create another folder named add_books_feature](./z.githubDesktopTutorials/15.png)

6. Open the `add_books_feature` folder, and create a file `create_book.txt`. (Do `right click` → `new` → `Text Document` to create a new text file.)

   ![create a file create_book.txt](./z.githubDesktopTutorials/16.png)

7. Open `create_book.txt` using notepad (or any text editor) and enter the text `This is the feature for the author to add a new book.` inside it.
   ![Open create_book.txt and enter the text](./z.githubDesktopTutorials/17.png)
8. save the file.

9. **<p id="commitChanges">Lets commit your change now.</p>**

   - Open Github Desktop.
   - You could see all the new files and changes in the repository in the left side.
     ![new files and changes in the repository in the left side](./z.githubDesktopTutorials/18.png)

   - Select any file (there is only one file though) and in the right side, you can see all the changes you made to it; Line-by-line!
     ![Select any file and in the right side, see all the changes inside it](./z.githubDesktopTutorials/37.png)

   - To commit your changes, in the left side there are two text boxes. Type something into the first smaller box and click on `commit to develop` button.

     ![Type something into the first smaller box and click on commit.](./z.githubDesktopTutorials/19.png)

> Just like that, your first commit is a success. In the `history` section, you can see all the commits made in the repository. First in the top is the commit that you have just committed.

   ![View All the commits in the repository](./z.githubDesktopTutorials/20.png)

10. Return to the `add_books_feature` folder and create another text file named `list_all_books.txt`.
    ![create another text file named list_all_books.txt](./z.githubDesktopTutorials/25.png)

11. Open `list_all_books.txt` and insert the text `This is the feature which shows the user all the books they’ve created as a list.` inside it.
    ![insert the text to list_all_books.txt](./z.githubDesktopTutorials/26.png)

12. Now commit changes agin. (Refer step 9).

## Unstaging changes

> You just realised that you don’t need to add the change made to `list_all_books.txt` now. Since, `list_all_books.txt` is another feature, you decide to complete developing it on another branch. Hence you should `unstage` your previous commit.

Let's see How,

1. Open Github desktop
2. In the left side, open the `history` tab.

   ![create another text file named list_all_books.txt](./z.githubDesktopTutorials/27.png)

3. You can see your previous two commits there.
   ![open the history tab](./z.githubDesktopTutorials/28.png)

4. Right click on the first commit (First in list: top commit) and select `undo commit` to undo that commit.
   ![select undo commit to undo that commit.](./z.githubDesktopTutorials/29.png)

5. You have successfully unstaged your last commit. Now in the changes section you can see the file `list_all_books.txt`.
   ![In the changes section you can see the file list_all_books.txt](./z.githubDesktopTutorials/30.png)

<p id="checkoutBranch"></p>

6. Now let's switch to `main` branch. (Checkout to `main` branch)

   Let's see How,

   - Click on the `develop` branch and select `main` just below the `default branches` title.
   ![Click on the `develop` branch and select `main` just below the `default branches` title](./z.githubDesktopTutorials/44.png)

   - In the next pop-up select `bring my changes to main` option and click on `switch branch` button.
  ![select bring my changes to main option and click on switch branch button.](./z.githubDesktopTutorials/31.png)

> Now it's time to create another branch to develop `list_all_books.txt` file. (Just like you decided before).

Let's see How,

7. Create another branch named `feature`. (Refer to <a href="#createBranch">step 2</a> in `The Assessment` section.)
8. After creating and switching to the `feature` branch, commit changes to the branch now.(Refer to <a href="#commitChanges">step 9</a> in `The Assessment` section.)
9. After that open the ` list_all_books.txt` file and enter `List all books will list all books in ascending order.` into it. Now the `list_all_books.txt` file will have 2 lines. Save the file.
   ![Open the list_all_books.txt file and enter text into it](./z.githubDesktopTutorials/32.png)

10. Open Github Desktop and commit again. Now the ` feature` branch have two commits.

## Merging the branches and Pushing Back changes to the parent repository

> Now, it's time to push your changes and conrtibute to the `GTech µLearn Github repository`, you need to raise a Pull Request. Before that remember that, now you have two different branches, namely, `develop` and `feature`. The commits you've made so far are in these two branches. Let’s merge them together before pushing.

For that,

1. Change to the `develop` branch. (Refer to <a href="#checkoutBranch">step 6</a> in the ` unstaging changes` section).

2. Click on the `develop` branch. In the new pop-up click on the `choose a branch to merge into develop`.
   ![click on the choose a branch to merge into develop](./z.githubDesktopTutorials/33.png)

3. In the next pop-up search for `feature` in the text box and select the `feature` branch and click on the `create a merge commit` button.
   ![search for feature in the text box and select the feature branch and click on the create a merge commit button](./z.githubDesktopTutorials/34.png)

4. Then you'll get a message of succession.

   ![message of succession.](./z.githubDesktopTutorials/35.png)

5. Now both branches were merged into one branch.

> Once the merge is complete. Push the develop branch to the remote (Github Cloud).

Let's see How, 

6. In the Github Desktop, you could see an option `publish branch`. Click on it and all your commits and files will be uploaded to the Github Cloud. It'll take some time based on your network speed.
![Pushing to Github Cloud](./z.githubDesktopTutorials/36.png)

7. After sometime you'll get an option to create a `pull request`.
   ![option to create a pull request](./z.githubDesktopTutorials/38.png)

8. Now it's time to create a pull request to the parent repository `GTech µLearn Github repository`.
   Let's see how:

9. After your branch is published, press `ctrl+R` and you'll be redirected to your browser. (If not open this link 
   
         github.com/gtech-mulearn/Github-Enablment-Task/compare/main...USERNAME:Github-Enablment-Task:develop
   
   Before opening, replace `USERNAME` with your github username Eg: <pre>github.com/gtech-mulearn/Github-Enablment-Task/compare/main...christo-zero-john:Github-Enablment-Task:develop</pre>).

   ![open the link](./z.githubDesktopTutorials/39.png)

10. Once you open the link, you could create a pull request. Make sure that in the first box `main` is selected and in the second box `develop` is selected.
    ![Make sure that in the first box `main` is selected and in the second box `develop` is selected.](./z.githubDesktopTutorials/40.png)

11. Click on `Create Pull Request` Button.
    ![Click on create Pull Request Button](./z.githubDesktopTutorials/41.png)

12. In the next screen give some title and click on `Create Pull Request` again.

### Assignment Submission

> It's time to submit your task.

1. After creating your pull request copy the URL of the new window that opened just now.
   ![copy the URL of the new window that opened just now](./z.githubDesktopTutorials/43.png)

2. Submit the link in `#task-dropbox` channel with the hashtag, `#ge-intro-to-github`.
3. With your submission, feel free to drop in a small note about your experience with doing this assignment. We’d be delighted to read it.

> ## By the way, If you are interested, you could always try the [original task using command line](./readme)
