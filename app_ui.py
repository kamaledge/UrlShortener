from flask import Flask, jsonify, request, render_template, redirect, flash, url_for
from helpers import  generate_short_url
import json
from config import url_file, url_file_dir

url_app_ui = Flask(__name__, template_folder='templates')



@url_app_ui.route('/', methods=['GET'])
def home():
    '''
    Redirects to short URl page
    :return:
    '''
    return redirect('/shorten')

@url_app_ui.route('/lengthen', methods=['GET', 'POST'])
def lengthen():
    '''
        Picks up short url from the request form
        :return: None
        Redirects to original url mapped to short irl
        '''
    if request.method == 'POST':
        short_id = request.form['custom_id']
        print(f'shortid is {short_id}')
        if short_id:
            try:
                f = open(url_file, 'r')
                data = json.load(f)
                f.close()
            except:
                return jsonify({'longurl': ''})
            else:
                long_url = data.get(short_id)
                print(f'long url is {long_url}')
                if not long_url.startswith('http://'):
                    long_url = 'http://'+long_url
                print(f'long url recreated as {long_url}')
                return redirect(long_url)

        if not short_id:
            return render_template('lengthen.html')

    return render_template('lengthen.html')

@url_app_ui.route('/shorten', methods=['POST', 'GET'])
def shorten():
    '''
        Picks up full url from the request
        :return: Shortened URL
    '''
    if request.method == 'POST':
        input_url = request.form['url']
        short_url = generate_short_url(input_url)
        url_dict = {short_url:input_url}
        with open(url_file,'r') as f:
            try:
                d = json.load(f)
            except Exception as e:
                print(e)
                d = {}
            else:
                d.update(url_dict)
                print(d)
            finally:
                with open(url_file, 'w') as f:
                    json.dump(d,f)

        return  render_template('shorten.html', short_url=short_url, )
    return render_template('shorten.html')


if __name__ == '__main__':
    url_app_ui.run(port=5011)
