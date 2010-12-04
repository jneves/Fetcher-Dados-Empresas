#!/usr/bin/env python

import urllib
import urllib2
from cookielib import CookieJar
import sys

dir = "/home/joao/projectos/polvo/repo/"
dir_save = dir + 'dump/'

def get_doc(number):
    #make a cookie and redirect handlers
    cookies = CookieJar() 
    cookie_handler= urllib2.HTTPCookieProcessor(cookies)
    redirect_handler= urllib2.HTTPRedirectHandler()

    opener = urllib2.build_opener(redirect_handler,cookie_handler) #make opener w/ handlers

    #build the url
    req = urllib2.Request("http://publicacoes.mj.pt/Index.asp")
    page = opener.open(req) #open the page
    req = urllib2.Request("http://publicacoes.mj.pt/pt/Pesquisa.asp?iNIPC=&sFirma=&dfDistrito=&dfConcelho=&dInicial=&dFinal=&iTipo=0&sCAPTCHA=&pesquisar=Pesquisar&dfConcelhoDesc=")
    page = opener.open(req) #open the page
    req = urllib2.Request("http://publicacoes.mj.pt/pt/PesquisaDetalhe.asp?iID=%d" % 1000000)
    page = opener.open(req) #open the page

    f = open(dir_save + str(number) + ".html", "w")
    f.write(page.read())
    f.close()

number_from = 0
if len(sys.argv) > 1:
    number_from = long(sys.argv[1])

number_to = number_from
if len(sys.argv) > 2:
    number_to = long(sys.argv[2])

for i in range(number_from, number_to+1):
    get_doc(i)
