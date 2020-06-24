# AnimalCrossingTurnipNotifier
This is a repository for a turnip notifier. It's to help you be the first one to know when someone makes a post on the TurnipsExchange subreddit.
I made this because I'll find myself refreshing the new page on the subreddit, checking to see if anyone has good prices available.
Even being a few minutes late mean that you'll be waiting in a queue for a while. So I decided to create this.

What it does is it monitors the subreddit, and whenever a new post is made containing numbers (most likely turnip prices), it'll check to see if this
number is higher than an amount that you have entered. If it is, it'll notify you and display the amount. If you're happy with this amount, you can
quickly go to the subreddit and check out the post.

It is by no means perfect. If a user enters multiple numbers, it'll only analyze the first one.
If multiple posts are made between the intervals that the user selected, it'll only analyze the most recent one.
If a user posts something such as 'looking for someone who's island is buying turnips for 500', it'll trigger the noise.

In order to set it up, first you need to follow the first steps guide in order to get access to Reddit's api:
https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

Once thats done, open up the credentials.json file using something like notepad++ and insert your client id and secret key into its respective field, as such:
{
    "app_id" :  "<id>",
    "app_secret" : "<secret>"
}
 
Install pipenv using:
'python -m pip install pipenv'

Once thats done,run main.py using pipenv to install all of the dependencies.
To do this on windows, shift+right click in the folder where all the files are located. Open Powershell, and run the following command:
'pipenv install'

Once this is done, run:
'pipenv run main.py'.

You'll be prompted to enter the minimum turnip price that you want to be notified for. I like to use 400.

Then you'll want to type how many seconds should pass before the script checks to see if a new post has been made.
A value between 5 - 30 works fine, make sure to use an integer.

Once a post is made containing the values for a turnip that is greater than or equals your minimum price, you'll hear the coin noise from Mario.

Enjoy
