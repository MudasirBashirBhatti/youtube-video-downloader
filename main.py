from flask import Flask, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
@app.route('/youtube-video-downloader/<string:n>')
def plus(n):
    myLink = (f"https://www.youtube.com/watch?v={n}")
    myTube = YouTube(myLink)
    myid = myTube.channel_id
    author = myTube.author

    minutes = int(myTube.length/60)
    sec = myTube.length%60
    length= (f"{minutes}:{sec}")

    channelUrl= myTube.channel_url
    title = myTube.title
    views = myTube.views
    thumbnail = myTube.thumbnail_url
    oneFourty = myTube.streams.filter(resolution='144p').first().url

    twoFourty = myTube.streams.filter(resolution='240p').first().url

    threeSixty = myTube.streams.filter(resolution='360p').first().url

    fourEighty = myTube.streams.filter(resolution='480p').first().url

    seavenTwenty = myTube.streams.filter(resolution='720p').first().url

    oneEighty = myTube.streams.filter(resolution='1080p').first().url

    desiredBitrate1 = 128
    audio_stream = myTube.streams.filter(only_audio=True, abr=f"{desiredBitrate1}kbps").first().url
    result={
        'title':title,
        "id":myid,
        "channel_name":author,
        "videos":{
        "144p":{
            "url":oneFourty,
        },
        "240p":{
            "url":twoFourty,
        },
        "360p":{
            "url":threeSixty,
        },
        "480p":{
            "url":fourEighty,
        },
        "720p":{
            "url":seavenTwenty,
        },
        "1080p":{
            "url":oneEighty,
        },
        },
        "mp3":{
            "128kbps":audio_stream
        },
        "length":length,
        "channel_url":channelUrl,
        "views":views,
        "thumbnail":thumbnail,
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
