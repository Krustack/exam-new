""" ให้ขนาดนี้แล้วหวังว่าจะทำได้นะจ๊ะ """

import os
from flask import Flask, render_template, request, redirect
from supabase import create_client, Client

app = Flask(__name__)

# เชื่อมต่อกับ Supabase
url = ""
key = ""
client = create_client(url, key)


def sum_amount(): #หาผลรวม amount ทั้งหมด
    pass



""" หน้าหลักและแสดง form  เพิ่ม และ update ข้อมูล และแสดงข้อมูลทั้งหมด """
@app.route('/', methods=['POST', 'GET'])
def index():
    # expense = {}
    # if request.method == 'POST' :
    #     id = request.form['id']
    #     response = supabase.table(ชื่อtable).select("*").eq('id',id).execute()
    #     expense = response.data[0]
    # response = supabase.table(ชื่อtable).select("*").execute()
    #return render_template('index.html', argumentตัวที่1=response.data, argumentตัวที่2=expense)
    return render_template('index.html')

""" ลิงค์ ไปใช้ request เพิ่ม ข้อมูล """
@app.route('/add-expense', methods=['POST'])
def add_student():
    # ตัวแปรเก็บค่า = request.form['name ของ input']
    # supabase.table(ชื่อtable).insert({ข้อมูล}).execute()
    return redirect('/')

""" ลิงค์ ไปใช้ request ลบ ข้อมูล """
@app.route('/del-expense', methods=['POST'])
def del_student():
        # id = request.form['id']
        # response = supabase.table(ชื่อtable).delete().eq('id', id).execute()
    return redirect('/')

""" ลิงค์ ไปใช้ request แก้ไข ข้อมูล """
@app.route('/update-expense', methods=['POST'])
def update_student():
    # ตัวแปรเก็บค่า = request.form['name ของ input']
    # response = (supabase.table(ชื่อtable).update({ข้อมูล}).eq('id', id).execute())
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)