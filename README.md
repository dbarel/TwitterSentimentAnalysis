# TwitterSentimentAnalysis
============================

This tool analyze the sentiment towards a specific person over time.
The tool will gather tweets from live twitter stream, and present the relative sentiment for the last hour, day and month.
The tool run on 2 separated process.
1. Gather tweets from live twitter stream and analyze the sentiment.
2. A web server that will presnet the resulte.

###Installation and dependency
This tool was build on python 3.6.
*Django (1.10.5) as a web server.
*djangorestframework (3.7.0) for restfull.
*tweepy (3.5.0) for live twitter stream.
 *nltk (3.2.5) and textblob (0.13.0) for sentiment analysis.
 
 After installing python 3.6 or higher install packages by pip:
 ```bash
$ pip install django
$ pip install djangorestframework
$ pip install tweepy
$ pip install nltk
$ pip install textblob
```
For 'textblob' to work you will need to download 'punkt' trained models, Open python console:

 ``` bash
import nltk
nltk.download('punkt')
```

###Setup:
the tool have 'configuration.txt' file oepn it and enter person names/ niknames 'PERSON.KEYWORDS'. 
Example:
```bash
$ PERSON.KEYWORDS = Donald Trump| Trump| #potus| @therealdonalntrump
```

###Runing the tool:
'run_script.bat' will run both programs.
server will be running '127.0.0.1:80' and will update evrey 10 secound the data.

###Known issues and bugs:
1. Input method shuld be more user friendly and hould be from the webserver, not by 'run_script.bat'
2. Data saved on csv file and not on db making analyzeing slow than it should.
3. FrontEnd should look better.
4. 'tweepy' can support only one stream (only one preson).
5. django server was build without any app.
6. django set to  debug mode.

