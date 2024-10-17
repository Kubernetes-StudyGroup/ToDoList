from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import pymysql

pymysql.install_as_MySQLdb()

load_dotenv()

db_host = os.getenv("DB_HOSTNAME")
db_usr = os.getenv("DB_USERNAME")
db_psw = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_usr}:{db_psw}@{db_host}/{db_database}'
db = SQLAlchemy(app)


# http://127.0.0.1:5000/?user_id=1


# 定義todos模型
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# 创建数据库表
with app.app_context():
    db.create_all()

# 获取所有待办事项
@app.route('/', methods=['GET'])
def index():
    user_id = request.args.get('user_id')  # 從查詢參數獲取用戶 ID
    if not user_id:
        return jsonify({"error": "User ID is missing"}), 400

    todos = Todo.query.filter_by(user_id=user_id).all()
    return render_template('index.html', todos=todos, user_id=user_id)

# 添加新的待办事项
@app.route('/add_todo', methods=['POST'])
def add_todo():
    task = request.form.get('task')  # 从表单获取任务
    user_id = request.form.get('user_id')  # 从表单获取用户ID

    if not task or not user_id:
        return jsonify({"error": "Task or User ID is missing"}), 400

    new_todo = Todo(task=task, user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()
    
    return redirect(url_for('index', user_id=user_id))

# 删除待办事项
@app.route('/delete_todo/<int:id>', methods=['POST'])
def delete_todo(id):
    user_id = request.form.get('user_id')  # 从表单获取用户ID
    if not user_id:
        return jsonify({"error": "User ID is missing"}), 400
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index', user_id=user_id))

if __name__ == '__main__':
    app.run(debug=True)
    
 