from flask import Flask, render_template, request, redirect, session
from models.Users import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html',users=User.get_all())

@app.route('/user/new')
def new():
    return render_template('new_users.html')

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    user_id=User.save(request.form)
    return redirect('/users/show/'+str(user_id))

@app.route('/users/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')

@app.route('/users/show/<int:id>')
def show(id):
    return render_template('user_show.html',user=User.get_one(id))

@app.route('/users/edit/<int:id>')
def edit(id):
    return render_template('user_edit.html',user=User.get_one(id))

@app.route('/users/update/<int:id>',methods=['POST'])
def update(id):
    user={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'id':id,
    }
    User.edit(user)
    return redirect('/users/show/'+str(id))