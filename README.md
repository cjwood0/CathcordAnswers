# CathcordAnswers

Monitoring the Catholicism discord server's #Answers channel, created at the reuqest of a mod.

---

## Installation

Clone the repo and execute `pip3 install`

## Environment Variables

`DISCORD_TOKEN` - Copy this value from Discord after authorizing your own AnswerMonitor


## Running

`python AnswerMonitor.py`

## Hosting

AnswerMonitor can be easily be deployed to Heroku:

1. Install the Heroku CLI and `heroku login`
2. Create your own AnswerMonitor app with `heroku create <optional-name>`
3. Set your `DISCORD_TOKEN` heroku environment variables
4. Deploy AnswerMonitor using `git push heroku master`


## License

Copyright (c) 2020 CJ Wood
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
