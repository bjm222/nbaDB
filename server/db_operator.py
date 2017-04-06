#!/usr/bin/python
import mysql.connector
import json
import stored_sql
from db_connector import *
from stored_sql import *
from machine_learning import *
from decimal import *

def db_operate_type1(index):
    db = db_connect()

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    stored_query_type1 = fetch_sql1(int(index) - 1)
    cur.execute(stored_query_type1)

    result = []

    # print all the first cell of all the rows
    for row in cur.fetchall():
        dic = {}
        dic['fname'] = row[0]
        dic['lname'] = row[1]
        result.append(dic)

    db.close()

    return result

def db_operate_type2(index, fname, lname):
    db = db_connect()

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    stored_query_type2 = fetch_sql2(int(index) - 1, fname, lname)

    # Use all the SQL you like
    cur.execute(stored_query_type2)

    result = []

    # print all the first cell of all the rows
    for row in cur.fetchall():
        dic = {}
        dic['fname'] = row[0]
        dic['lname'] = row[1]
        dic['points'] = float(row[2])
        dic['year'] = row[3]
        result.append(dic)
    
    print result
    prediction = linear_regression(result)
    
    db.close()
    return prediction

def db_operate_type3(fname, lname):
    db = db_connect()

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    stored_query_type3 = fetch_sql3(fname, lname)

    # Use all the SQL you like
    cur.execute(stored_query_type3)

    result = []

    # print all the first cell of all the rows
    for row in cur.fetchall():
        dic = {}
        dic['fname'] = row[0]
        dic['lname'] = row[1]
        dic['points'] = float(row[2])
        dic['year'] = row[3]
        result.append(dic)
    
    print result
    prediction = linear_regression(result)
    
    db.close()
    return prediction

def db_operate_type4(fname, lname):
    db = db_connect()

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    stored_query_type4 = fetch_sql4(fname, lname)

    # Use all the SQL you like
    cur.execute(stored_query_type4)


    # print all the first cell of all the rows
    fname = ''
    lname = ''
    points = 0.0
    assist = 0.0
    rebound = 0.0
    steal = 0.0
    block = 0.0
    career_len = 0
    for row in cur.fetchall():
        fname = row[0]
        lname = row[1]
        points += float(row[2])
        assist += float(row[3])
        rebound += float(row[4])
        steal += float(row[5])
        block += float(row[6])
        career_len += 1
    dic = {}
    dic['fname'] = fname
    dic['lname'] = lname
    dic['points'] = points / career_len
    dic['assist'] = assist / career_len
    dic['rebound'] = rebound / career_len
    dic['steal'] = steal / career_len
    dic['block'] = block / career_len
    
    db.close()
    return dic