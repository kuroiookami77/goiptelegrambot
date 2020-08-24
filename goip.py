#!/usr/bin/python
# -*- coding: utf-8 *-*
import time
# time - module is used for sleep operator,
# and for unique message id generating
import sys
# sys - module is used here to retreive
# arguments that are followed with this script launch
import requests
# requests - module is used for a web-access (via GUI for instanse)
from subprocess import Popen, PIPE, STDOUT
# subprocess - module is used here to launch a zabbix_sender console command
from content import arguments

# Этот модуль осуществляет отправку и обработку ussd кодов. Общается с симбазой. Параметры симбазы в content.
# default system par, dont need to change

ussd_answer_wait_timer = 8
Data = {'send': 'Send'}
Headers = {'Accept': '*/*'}
arguments.update({'mode': 'ussd'})

def console_exec(cmd):
    p = Popen(
            cmd,
            shell=True,
            stdin=PIPE,
            stdout=PIPE,
            stderr=STDOUT,
            close_fds=True)
    cmd_output = p.stdout.read()
    return cmd_output

# Парс с линий с формата xml
def parse_balances(xml_line):
    i = 0
    a = ''
    result_list = []
    while i < len(xml_line):
        while i < len(xml_line) and xml_line[i:i+6] != '<error':
            i += 1
        while i < len(xml_line) and xml_line[i:i+7] != '</error':
            i += 1
            a = a + xml_line[i]
    b = a.replace('>Баланс: ', '>')
    c = b.split('>')
    for d in c:
        pos = d.find('.')
        if d != 'error1':  # drop the first split
            result_list.append(d[0:pos + 3])
    return result_list

# отправка sms или кодов (смс избыточный функционал, не используется)
def send_message(lines, message_type):
    for i in range(0, len(lines)):
        dat = Data
        dat.update({'line': lines[i]})

        if message_type == 'sms':

            dat.update({'action': 'SMS', 'smscontent': arguments['message']})
            dstnums = arguments['dstphonenumbers'].split(',')
            for j in range(0, len(dstnums)):
                dat.update({
                    'telnum': dstnums[j],
                    'smskey': str(int(round(time.time() * 1000000)))[8:]})
                ses.post(
                       'http://'
                        + arguments['user']
                        + ':'
                        + arguments['passwd']
                        + '@'
                        + arguments['our_gsm_gateway_ip']
                        + '/default/en_US/sms_info.html?type='
                        + message_type, data=dat).content

        if message_type == 'ussd':
            dat.update({
                'action': 'USSD',
                'telnum': arguments['balance_tel_number' + lines[i]],
                'smskey': str(int(round(time.time() * 1000000)))[8:]})
            ses.post(
                    'http://'
                    + arguments['user']
                    + ':'
                    + arguments['passwd']
                    + '@'
                    + arguments['our_gsm_gateway_ip']
                    + '/default/en_US/sms_info.html?type='
                    + message_type, data=dat).content

# чтение ответа с симбазы
def read_ussd_response_out_of_xml(session):
    Answer = session.post(
        'http://'
        + arguments['our_gsm_gateway_ip']
        + '/default/en_US/send_sms_status.xml?u=' + arguments['user']
        + '&p='
        + arguments['passwd']).content
    return Answer

# парс аргументов при запуске скрипта руками
def args_parse():
    for i in range(1, len(sys.argv)):
        if sys.argv[i][0:2] == '--':
            arguments.update({sys.argv[i][2:]: sys.argv[i+1]})


ses = requests.session()
args_parse()

# главный сплиттер запросов, запускает скрипт
def runner():
    if arguments['mode'] == 'ussd':
        send_message(arguments['ussdports'].split(','), arguments['mode'])
        time.sleep(ussd_answer_wait_timer)
        resp = read_ussd_response_out_of_xml(ses)
        ses.close()
        return resp
    elif arguments['mode'] == 'sms':
        send_message(arguments['smsports'].split(','), arguments['mode'])
        ses.close()

