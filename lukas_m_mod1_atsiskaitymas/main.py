from requests  import get

def crawl(source, time_limit=60):
    time_limit = 60
    formats =['.csv', '.txt', ".json"]
    response = get(source)
    print(response)
    text = response.text
    print(text)


if __name__=="__main__":
    crawl("https://www.lrytas.lt/")
