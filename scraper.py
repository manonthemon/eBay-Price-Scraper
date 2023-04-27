import bs4, requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body.vi-contv2.lhdr-ie-.vi-hd-ops.vi-wide-watch-btn.vi-ds3-global.vi-bb-flex.label-right-align.vi-bb-btnclr1.vi-ds6.vi-bb-r-btn.vi-white-spacing.vi-rounded-btns.vi-long-cta div#Body.sz940.sz1280 div#CenterPanelDF div div#CenterPanel.ebaylocale_en_US.ebay_longlngsite div#CenterPanelInternal div#LeftSummaryPanel.lsp-c.lsp-cRight.lsp-cL500.vi-v-img-strp500.lsp-de div#mainContent.is form div.vim-buybox-wrapper div.vim.x-buybox div.x-buybox__section div.x-buybox__price-section div.vim.x-bin-price div.x-bin-price__content div.x-price-primary span span.ux-textspans')
    return elems[0].text.strip()


def getEbayName(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body.vi-contv2.lhdr-ie-.vi-hd-ops.vi-wide-watch-btn.vi-ds3-global.vi-bb-flex.label-right-align.vi-bb-btnclr1.vi-ds6.vi-bb-r-btn.vi-white-spacing.vi-rounded-btns.vi-long-cta div#Body.sz940.sz1280 div#CenterPanelDF div div#CenterPanel.ebaylocale_en_US.ebay_longlngsite div#CenterPanelInternal div#LeftSummaryPanel.lsp-c.lsp-cRight.lsp-cL500.vi-v-img-strp500.lsp-de div.vi-swc-lsp div div.vim.x-item-title h1.x-item-title__mainTitle span.ux-textspans.ux-textspans--BOLD')
    return elems[0].text.strip()

url = 'https://www.ebay.com/itm/185765752964?_trkparms=pageci%3A72c68f0e-e4f1-11ed-9cfd-6aa0876eaf24%7Cparentrq%3Ac28b3e7e1870a4b7123e3d04ffff6eec%7Ciid%3A1'
price = getEbayPrice(url)
name = getEbayName(url)
print('The price of ' + name + ' is ' + price)
