#! /usr/bin/env ruby
# -*- coding: utf-8 -*-

require 'rubygems'
require 'mechanize'
require 'logger'

def get_doc(number)
  dir='/home/joao/projectos/polvo/repo/'
  dir_save=dir + 'dump/'

  @agent = WWW::Mechanize.new {|a| a.log = Logger.new('/tmp/polvo.log') }
  
  $stderr.print "A ligar ao sítio das Publicações do Ministério da Justiça...\n"
  page = @agent.get('http://publicacoes.mj.pt/Index.asp')
  
  $stderr.print "A ligar à pesquisa...\n"
  page = @agent.get('http://publicacoes.mj.pt/pt/Pesquisa.asp?iNIPC=&sFirma=&dfDistrito=&dfConcelho=&dInicial=&dFinal=&iTipo=0&sCAPTCHA=&pesquisar=Pesquisar&dfConcelhoDesc=', page)
  
  $stderr.print "A obter o registo #{number}...\n"
  page = @agent.get "http://publicacoes.mj.pt/pt/PesquisaDetalhe.asp?iID=#{number}", page
  
  File.open(dir_save + "#{number}.html", 'w') {|f| f.write(page.content) }
end

number_from = 0
number_from = ARGV[0] if ARGV.size > 0
number_to = number_from 
number_to = ARGV[1] if ARGV.size > 1

for doc in number_from..number_to
  get_doc(doc)
end
