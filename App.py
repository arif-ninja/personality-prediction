from flask import Flask, redirect,url_for, render_template,request

from flask_caching import Cache
import twitter_pred 
#from twitter_pred import *


app=Flask(__name__)
 
cache=Cache()
app.config['CACHE_TYPE']= 'simple'
cache.init_app(app)





@app.route("/")

@cache.cached(timeout=10)

def Home():
    return render_template("Home.html")
    

@app.route('/',methods=['GET','POST'])
def predict():   
   if request.method=='POST' :
       data=request.form.get("search")
       user=twitter_pred.getTweets(data)
   return render_template('Daskboard.html',data=twitter_pred.mbti, data2=twitter_pred.op_json)


if __name__ == "__main__":
    app.config['TEMPLATE_AUTO_RELOAD']=True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True,use_reloader=False)
