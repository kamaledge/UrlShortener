from flask import Flask, jsonify, request, render_template, redirect, flash, url_for
from helpers import  generate_short_url
import json
from config import url_file, url_file_dir

# url_file_dir = os.getcwd()
# url_file = url_file_dir + '\\' +  'url_repo.json'
url_app = Flask(__name__, template_folder='static')





# @url_app.route('/', methods=['GET'])
# def index():
#     # if request.method == 'POST':
#     #     request_data = request.json()
#     #     input_url = request_data.get('url')
#     #     short_url = generate_short_url(input_url)
#     #     url_dict = {short_url:input_url}
#     #     url_file = url_file_dir + short_url+'.json'
#     #     with open(url_file,'w') as f:
#     #         json.dump(url_dict,f)
#     #     # return jsonify({'short_url':short_url})
#     #     return  render_template('/static/index.html', short_url=short_url)
#     # return render_template(url_file_dir+r'\static\index.html')
#     return render_template('index.html')

@url_app.route('/shorten', methods=['POST', 'GET'])
def shorten_url():
    '''
    Picks up full url from the request
    :return: Shortened URL
    '''
    print(request.json)
    if request.method == 'POST':
        request_data = request.json
        print(f'request_data: {request.data}')
        # input_url = request.form['url']
        input_url = request_data.get('url')
        print(f'input_url: {input_url}')
        short_url = generate_short_url(input_url)
        url_dict = {short_url:input_url}
        # url_file = url_file_dir + '\\' + short_url+'.json'
        print(url_file)
        with open(url_file,'r') as f:
            try:
                d = json.load(f)
            except:
                d = {}
            else:
                d.update(url_dict)
                print(d)
            finally:
                with open(url_file, 'w') as f:
                    json.dump(d,f)
        return jsonify({'short_url':short_url})
    #     return  render_template('index.html', short_url=short_url, )
    # return render_template('index.html')






@url_app.route('/lengthen', methods=['POST'])
def lengthen_url():
    '''
        Picks up shortened url from the request
        :return: Full URL if present
        '''
    if request.method == 'POST':
        # url = request.form['url']
        request_data = request.json
        print(request_data)
        # short_id = request.form['custom_id']
        short_url = request_data.get('short_url')
        print(short_url)

        try:
            f= open(url_file,'r')
            data = json.load(f)
            f.close()
        except:
            # print(e)
            return jsonify({'longurl':''})
        else:
            long_url = data.get(short_url)
            print(long_url)
            return jsonify({'longurl':long_url})
        return redirect(long_url)

    #     if short_id and os.path.join(os.path.dirname(__file__), short_id+".json"):
    #         filename = os.path.join(os.path.dirname(__file__), short_id+".json")
    #         with open(filename, 'r') as fr:
    #             data = json.load(fr)
    #             long_url = data.get(short_id)
    #         flash('Please enter different custom id!')
    #         return redirect(url_for(long_url))
    # return render_template('index.html')
        # if not url:
        #     flash('The URL is required!')
        #     return redirect(url_for('index'))

        # if not short_id:
        #     short_id = generate_short_url(8)





if __name__ == '__main__':
    url_app.run(port=5010)
