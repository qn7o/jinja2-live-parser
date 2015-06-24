
# Jinja2 live parser

A lightweight live parser for [Jinja2](http://jinja.pocoo.org/docs/dev/) based on [Flask](http://flask.pocoo.org/) and [Jquery](http://jquery.com/).


## Install

    $ git clone git@github.com:falconsocial/jinja2-live-parser.git
    $ pip install -r requirements.txt
    $ python parser.py

Also, you'll need to have browsersync installed. Instructions on how to install it can be found [here](http://www.browsersync.io/#install)

## Usage

* Clone the `notifications-templates` repository on your local file system
* In your `bs-config.js`, change the `files` key to point to your notifications-templates repository location
* Run `browser-sync` as follows:
    `$ browser-sync start --config bs-config.js`
* Open `http://localhost:3000/<channel>/<prefix>/<template>` in your browser, and edit your template in your favorite editor and have your preview pane refreshed with your changes automatically

Note that in the URL, you have to provide your template path you want to edit in the form of: `http://localhost:3000/render/<channel>/<prefix>/<template>`
