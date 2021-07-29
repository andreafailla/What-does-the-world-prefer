# What Does The World Prefer? (WDTWP)
Ever wondered what is the most popular between two topics? You can find out with WDTWP!
<br>This application works as follows:
- Gets two words chosen by the user;
- Fetches the 100 most recent tweets for each word and cleans them;
- Computes and compares sentiment polarity scores between the two batches;
- Informs the user :)
<br>

GUI built with [Tkinter](https://docs.python.org/3/library/tkinter.html).<br>
Tweets scraped via [Twint](https://github.com/twintproject/twint) and cleaned via [Preprocessor](https://github.com/s/preprocessor).<br>
Sentiment analysis via [TextBlob](https://github.com/sloria/TextBlob).<br>


## Setup
- Download the repository and unzip it;
- Open a terminal window;
- [optional] Create a virtual environment: <code>$conda create --name myenv</code> and activate it <code>$conda activate myenv</code> 
- Install dependencies: <code>$pip install -r requirements.txt</code>


## Usage
- To run the program and launch the GUI type: <code>$python3 ./src/main.py</code>
- Type two words in the text boxes;
- Hit run;
- Done!


<br><br><br>Based on an idea by [Karolina Sowinska](https://github.com/karolina-sowinska)
