from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('i7DLB6HwAsDNZjOIMXtA8ZuddDuGZLx8iZYLF5XIs9TG8vf3iLS3P94YS+InWJWSsn+QE97R14GJp2/WxpF81VqFBcSuofb8KGLHZFTvjLTLjLm1qJ6XPjWqcZREaC1zStVAatgCq7gt83EJ3jXTRAdB04t89/1O/w1cDnyilFU=')
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
    r = '我不知道你在說啥'
    
    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'   
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)
        return

    if msg in ['Hi' , 'hi']:
        r = '嗨'
    elif msg == '你是誰':
        r = '別管我是誰'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

if __name__ == "__main__":
    app.run()