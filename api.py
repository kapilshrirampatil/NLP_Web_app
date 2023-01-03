import paralleldots
paralleldots.set_api_key('JNUNAd4a0yoG1i4PcNs4LEg1bq93Tp4IoVKL7cRqbrQ')


def ner(text):
    response=paralleldots.ner(text)
    return response


def sentiment(text):
    response=paralleldots.sentiment(text)
    return response


def abuse(text):
    response=paralleldots.abuse(text)
    return response

