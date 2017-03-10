#Kawod Bot v0.1

An early-stage content crawler to assist in content discovery in the eco- and fair-fashion world.

## Installation

Really not recommended. But if you must:

1. Create a virtual environment with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
2. Setup the needed environment variables in the `postactivate` script
3. Clone the repo: `https://github.com/mrgnth/kawod_bot.git`
4. Then install the needed python libraries: `pip install -r requirements.txt`
5. Let 'er rip!

You will need a lot of other requirements (e.g. Slack API secrets, etc) that you can gather from the `settings.py`

## Usage

1. Confige all settings in the settings.py
2. Type `python main.py` and away you go.


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

* v0.1: Initial Version. Rudimentary functionality. Only works with SQLite as db, Reddit and Newswire as sources, and Slack as publishing channel.

## Credits

Kawod Bot makes use of several superb Python Packages. Some include:
* [Pony ORM](https://ponyorm.com/): The most pythonic ORM (cool "Talk Python"-episode [here](https://talkpython.fm/episodes/show/87/ponyorm-the-most-pythonic-orm-yet))
* [PRAW](https://praw.readthedocs.io/): The Python Reddit API Wrapper
* [Requests](http://python-requests.org/): HTTP for Humans. So simple, you gotta love it!

## License

MIT License

Copyright (c) 2017 Thomas Schmitt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Todos

### What is this supposed to do:

1. ~~Collect popular posts from /r/Entrepreneur (24h)~~
2. Collect popular comments from /r/Entrepreneur (24h)
3. ~~Collect news stories on fair fashion~~
4. Collect twitter posts
5. Collect new blog posts from blog collection (RSS)
6. ~~Check for dupes~~
7. ~~Push them to DB~~
8. ~~Post summary to Slack channel~~
9. Document structures of scraped items!

### OOP-Redesign:

Post-Types are objects that can:

- get their data
- prepare their db commits
- fetch db-data for publishing
- return publish-ready formatted texts
