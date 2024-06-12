from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()  # make sure the request has the right arguments, and this is for the put # request
video_put_args.add_argument("name", type=str, help="No name sent for video",
                            required=True)  # add an argument to the request
video_put_args.add_argument("views", type=int, help="No views sent for video",
                            required=True)  # add an argument to the request
video_put_args.add_argument("likes", type=int, help="No likes sent for video",
                            required=True)  # add an argument to the request

Videos = {}


def abort_if_video_not_found(video_id):
    if video_id not in Videos:
        abort(404, message="We couldn't find the video...")


class Video(Resource):  # create a class that inherits from Resource
    def get(self, video_id):  # defines a get method
        abort_if_video_not_found(video_id)  # if video id is not there it will call abort which will end this method
        return Videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        Videos[video_id] = args
        return Videos[video_id], 201


api.add_resource(Video, "/video/<int:video_id>")  # access this resource at this endpoint

# this just runs our flask server, if we run it off main
if __name__ == '__main__':
    app.run(debug=True)
