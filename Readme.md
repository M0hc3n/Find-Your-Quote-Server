## Find Your Quote Server

This repository is the backend of Find Your Quote. A Web application that helps you find the quotes that you barely remember a part from, but still want to mention because they perfectly reflect your ideas (or because you simply want to show off).

### Dropbox

If you decide to use dropbox make sure you have `dl=1` at the end of your url. EX: `"https://www.dropbox.com/s/randnumbers/<export_name>.pkl?dl=1"`

## To run (with docker)

Clone the repo and use `docker build . -t fastapi-fastai2` Then you can use `docker run -p 8888:8000 fastapi-fastai2` and go to `localhost:8888` to see the app.

## To run (without docker)

You can try `python app/server.py` although I've not been able to get pytorch/fastai to play nice on my windows machine. And on my ubuntu 19.04 machine I had several problems as well. Still unsolved.
