from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APIapp.models import *
from APIapp.serializers import *
from rest_framework.renderers import JSONRenderer
from django.urls import reverse
from rest_framework import status
import random
import re
from datetime import datetime


def checkSecondDigits(num):
    length = len(num)
    sum =  0
    for i in range(length-2,-1,-2):
      number = eval(num[i])
      number = number * 2
      if number > 9:
          strNumber = str(number)
          number = eval(strNumber[0]) + eval(strNumber[1])
          sum += number
      return sum

def odd_digits(num):
    length = len(num)
    sumOdd = 0
    for i in range(length-1,-1,-2):
        print('type...', type(num))
        sumOdd += eval(num[i])
    return sumOdd

def card_length(num):
    length = len(num)
    if length >= 13 and length <= 16:
        if num [0] == "4" or num [0] == "5" or num [0] == "6" or (num [0] == "3" and num [1] == "7"):
            return True
        else:
            return False
    else:
        return False

def card_validation(num):
    even = checkSecondDigits(num)
    odd = odd_digits(num)
    c_len = card_length(num)
    tot = even + odd
    if c_len == True and tot % 10 == 0:
        return True
    else:
        return False


@api_view(['GET','POST'])
def Payment_Gateway(request):
    if request.method=='POST':
        txnserializer=TxnSerializer(data=request.data)
        if txnserializer.is_valid():
            
            amount = txnserializer.validated_data['amount']
            ccnum = txnserializer.validated_data['card']['cc_number']
            exp_year = txnserializer.validated_data['card']['expirationYear']
            t=txnserializer.save()
            t.txn_id=random.randint(1, 100000000)
            
            pattern = re.compile(r'(?:\d)')
            if re.match(pattern, ccnum):
                card_valid = card_validation(ccnum)
               
                if not card_valid:
                    t.status='Error : Invalid Card Number'

                else:
                    t.status='Success'

            elif not re.match(pattern, ccnum) :
                t.status='Error : Invalid Card Number'
            
            if int(amount) <= 0:
                t.status='Error : Amount should be greater than zero'

            else:
                t.status='Success'

            if int(exp_year) < int(datetime.now().strftime('%Y')):
                t.status='Error : Invalid Card Expiry Year'
            else:
                t.status='Success'
                
              

            t.save()



        else:
            return Response({"Error" : txnserializer.errors })
           
        return Response({
                        "amount": t.amount,
                        "currency": t.currency,
                        "card_type": t.card_type,
                        "card": {
                                "cc_number": t.card.cc_number,
                                },
                        "status":t.status,
                        "authorization_code":t.txn_id,
                        "time":t.time}, status=status.HTTP_201_CREATED)
    else:
        return Response({"amount":"<This is a sample request, enter proper values>",
                        "currency":"INR",
                        "card_type":"creditcard",
                        "card": {
                            "cc_number":"6784561290785623",
                            "expirationMonth": "12",
                            "expirationYear": "2020",
                            "cvv": "782"
                        }})



