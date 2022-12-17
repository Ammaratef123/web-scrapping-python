import requests
import bs4
Links = []
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=washers+machines&_sacat=0')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=2')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=3')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=4')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=5&rt=nc')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=6&rt=nc')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=7&rt=nc')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=8&rt=nc')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_pgn=9&rt=nc')
Links.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=washers+machines&_sacat=0&_ipg=60&_pgn=10&rt=nc')
wicher_details = []
wicher_prices = []
for i in range(len(Links)):
    page = requests.get(Links[i])
    content = page.content
    soup = bs4.BeautifulSoup(content, "html.parser")
    details = soup.findAll("div", {"class": "s-item__title"})
    prices = soup.findAll("span", {"class": "s-item__price"})

    for i in range(len(details)):
        wicher_details.append(details[i].text)
    for i in range(len(prices)):
        wicher_prices.append(prices[i].text)

for i in range(len(wicher_prices)):
    print('washer number ', i+1)
    print('washer details is: ',wicher_details[i])
    print('washer price is: ',wicher_prices[i])
    print()

