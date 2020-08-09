from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('vhA1+kXzgas95S+7VwjJewGKs2wq8giWnMy3GO5Hg/RhY6OMjdzU4o1f4RekJiFpsn+QE97R14GJp2/WxpF81VqFBcSuofb8KGLHZFTvjLQCdW6mmurQIiZt78LXcWgmkgGRH3FDt63Gkx1UtWkeuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4cfc30dece639679d8160dc21a532661')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text
	s = '吃了嗎'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()