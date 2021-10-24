from flask import Flask
from flask_restful import Api,Resource,reqparse,abort

app=Flask(__name__)
api=Api(app)

Students={"Fatema":{ "Roll":20010,"Dept":"CSE"},
          "Ayesha":{ "Roll":19017,"Dept":"CSE"},
          "Shahnaz":{ "Roll":20019,"Dept":"CSE"},}
data_put_args=reqparse.RequestParser()
data_put_args.add_argument("name", type=str,help="Name of the data",required=True)
data_put_args.add_argument("num", type=int,help="Number of the data",required=True)
datas={}
def abort_if_data_id_doesnt_exist(data_id):
    if data_id not in datas:
        abort(404, message="Couldnt find data")
def abort_if_data_id_exist(data_id):
    if data_id in datas:
        abort(409, message="Data already exist with this id")

class First(Resource):
    def get(self):
        return {"Name":"Fatema"}
    def post(self):
        return {"Name":"Fatema"}
class Sec(Resource):
    def get(self,name):
        return Students[name]
class Third(Resource):
    def get(self,data_id):
        abort_if_data_id_doesnt_exist(data_id)
        return datas[data_id]
    def post(self,data_id):
        abort_if_data_id_exist(data_id)
        args=data_put_args.parse_args()
        datas[data_id]=args
        return datas[data_id],201
    def put(self,data_id):
        abort_if_data_id_doesnt_exist(data_id)
        args=data_put_args.parse_args()
        datas[data_id]=args
        return datas[data_id],201
    def delete(self,data_id):
        abort_if_data_id_doesnt_exist(data_id)
        del datas[data_id]
        return 'Deleted',204


api.add_resource(First,'/info')
api.add_resource(Sec,'/info/<string:name>')
api.add_resource(Third,'/info/<int:data_id>')
if __name__=="__main__":
    app.run(debug=True)
