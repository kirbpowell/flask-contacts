#Why Python and Flask?

I will be honest - this was the first web app I've ever made, and definitely my first experience with Flask. I choose to use Flask, and more generally Python, because Python is easily the language I'm most comfortable coding in and I've been itching to try out Flask. 

#Thought Process


This being my first go around on this kind of thing, I immediately hit the web, searching for tutorials, code snippets, or anything that could show me how to get up and running on Flask as quick as possible. Through this searching process I found the Twitter Bootstrap "jumbotron-narrow" site theme, which I thought would be perfect for the contacts app. 

Once I'd found the theme i'd be using, I spent a bit of time tailoring the homepage to look like the wireframes that were included in the prompt. After I'd settled on a good preliminary layout, I went to work learning how to pass data from one page into another page in Flask. That took a little while, but the solution I settled on ended up being fairly simple. Since I'm not working with a database, I decided that rather than pass around the various JSONs needed for the detailed contact page as unicode text, I would pass in the detailsURL and employeeId fields, and use them to grab the JSONs I would need. 

With all of that sorted out and working preliminary, I went back to Bootstrap, and spent the rest of my time with the code playing with the layout and smoothing things out until it was in a nice, consistent form I was happy with. 

#Final Thoughts

* I thought it was interesting that many of the sample contacts seemed to be born in the past five years, while others had more normal birthdates. I left them all as is, though I suspect that some of the timestamps could be Javascript style, rather than straight UNIX timestamps. 

* If I get the chance to come back and tinker with this project again, I think it'd be interesting to add in database functionality. With that change, it would be fairly simple to add in things like user logins and user-specific contact lists etc. 

#Use Instructions

Since I've used virtualenv to isolate my development environment, you *shouldn't* even need to have python installed to run my app locally. Assuming you've got access to a *nix machine, you'll simply need to do the following:

1. Open the source directory in a terminal

2. Enter the command ```$ source venv/bin/activate``` this will activate a self-contained Python runtime with all needed dependencies installed. 

3. Enter the command ```$ python app.py```
    * This will launch the app locally. The output from this command should tell you where to point your browser (*localhost:5000 for me*).

4. From there, you can interact with the app as expected in the browser of your choice! h