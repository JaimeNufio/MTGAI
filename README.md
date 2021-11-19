
<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Magicthegathering-logo.svg/1280px-Magicthegathering-logo.svg.png" height="200"></img>
</div>
<h1>Sentiment Analysis of Magic the Gathering Cards</h1>
<b>Start here for an introduction on how classification works in Magic the Gathering!</b>


<a href="https://docs.google.com/presentation/d/1HtjL74-q6moKKO0Gb97HJQsNIhVykAZY3LiDlPMnKe4/edit?usp=sharing">Presentation</a><br>

<h2>Summary: </h2>
<p>
Magic the Gathering is a game split into five colors (White, Blue, Black, Red, Green), with the additional possibility of no color at all (Colorless), that can be thought of as classes. It’s a “resource management” type trading card game where players build decks around a chosen color identity. This identity can range from only one color, to all of them. The game is built such that players must decide which classes they wish to play in; the more colors in your deck, the les consistent. Cards in the game are given abilities that exist within their “class”, ideally. However, as the game has grown, the class identity of some abilities have bled into other colors. Additionally, the game designer have historically enjoyed expanding these definition in the name of more diverse deck building, at the expense of these class definitions. There exist communities online debating if some cards in the game are designed incorrectly. There also exist communities where fans of their game design new cards based on the more-or-less ‘accepted’ definitions, and other debate their design decisions. “Color identity” is often a hotly debated one. This project seeks to use sentiment analysis to come up with standardized answers, quickly.
<p>
  
<h1>Vocab</h1>
Oracle Text: "rules text", but the revised "official" versions kept online. (Old magic cards were not formatted as they are now, this was Wizard of the Coast's compromise for this)
</p>

<p>
Summary: Magic the Gathering is a game split into five colors (White, Blue, Black, Red, Green), with the additional possibility of no color at all (Colorless), that can be thought of as classes. It’s a “resource management” type trading card game where players build decks around a chosen color identity. This identity can range from only one color, to all of them. The game is built such that players must decide which classes they wish to play in; the more colors in your deck, the les consistent. Cards in the game are given abilities that exist within their “class”, ideally. However, as the game has grown, the class identity of some abilities have bled into other colors. Additionally, the game designer have historically enjoyed expanding these definition in the name of more diverse deck building, at the expense of these class definitions. There exist communities online debating if some cards in the game are designed incorrectly. There also exist communities where fans of their game design new cards based on the more-or-less ‘accepted’ definitions, and other debate their design decisions. “Color identity” is often a hotly debated one. This project seeks to use sentiment analysis to come up with standardized answers, quickly. 
<p>
The project makes use of a modified library offered by Facebook, fasttext. Originally, the goal was to build a LTSM (long short-term memory) recurrent neural network, and then utilize the bag-of-words technique. Additionally, it built for fast learning. It uses an approximation of the softmax algorithm, instead opting for a hierarchical softmax to cut on learning time, the idea being that some classifier are more frequent than other. It uses something called the “Hogwild” algorithm asynchronous stochastic gradient descent, which unfortunately sometimes leads to different answers when building on the same data. This however already happen with the way I cut the corpus into a training set, and a validation set, so it’s not unexpected.
</p>

<div align="right">
  <img src="https://www.pngkit.com/png/full/145-1458869_jace-beleren-ultra-pro-magic-the-gathering-shadows.png"></img>
</div>


<h2>Ussage:</h2>
in MTGAI:

run:
```bash
$build.sh X
```
```bash
$python3 Oracle.py
```

<p>where X is some number less than the size of the data (9000 works).</p>

<p>Then you are free to type any oracle text for the program to parse</p>

