from concurrent import futures
import os
import io
from collections import defaultdict
import logging
import threading

import grpc

import numpy as np
import cv2

import random

import sys
sys.path.append("image")
import image_pb2 as service
import image_pb2_grpc as rpc

class ShowVideoStream:
    image = None
    thread = futures.ThreadPoolExecutor(max_workers=1)

    def start(self):
        self.thread.submit(self.show_image)

    def set(self, image):
        self.image = image

    def show_image(self):
        while True:
            if self.image is not None:
                cv2.imshow('Processed Image', self.image)
                k = cv2.waitKey(1)
                if k == ord('q'):
                    break

class ImageServiceServer(rpc.ImageServiceServicer):  # inheriting here from the protobuf rpc file which is generated

    def __init__(self):
        # self.images = defaultdict(io.BytesIO)
        logging.info("successfuly created the images store")

    def start(self):
        print('start')
        self.show_image()

    def Upload(self, request_iterator, context):
        for request in request_iterator:
            if request.StatusCode == service.ImageUploadStatusCode.InProgress:
                logging.info(f'> {request.Id} - receiving image')

                # Image = Image.open(io.BytesIO(request.Content))
                # image.save(f"{round(time.time() * 1000)}.png")

                img_stream = io.BytesIO(request.Content)
                '''
                Use cv2.IMREAD_UNCHANGED for png since there are 4 channels.
                Use cv2.IMREAD_COLOR otherwise.
                '''
                png = False
                if (png): # png
                    image = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), cv2.IMREAD_UNCHANGED)
                    image = 255 - image[:,:,3]
                else:
                    image = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), cv2.IMREAD_COLOR)

                '''
                # Center coordinates
                center_coordinates = (random.randint(30, 150), random.randint(30, 150))
                
                # Radius of circle
                radius = 20
                
                # Blue color in BGR
                color = (255, 0, 0)
                
                # Line thickness of 2 px
                thickness = 2
                
                # Using cv2.circle() method
                # Draw a circle with blue line borders of thickness of 2 px
                image = cv2.circle(image, center_coordinates, radius, color, thickness)
                '''

                show.set(image)

                result = service.ImageUploadResponse(Id=request.Id, StatusCode=service.ImageUploadStatusCode.Ok, Message="image uploaded")
                return result
            #     self.images[request.Id].write(request.Content)
            #     result = service.ImageUploadResponse(Id=request.Id, StatusCode=service.ImageUploadStatusCode.Ok, Message='waiting for more')

            # if request.StatusCode == service.ImageUploadStatusCode.Ok and not request.Content:
            #     logging.info('transfer completed!')
            #     logging.info(f'> {request.Id} - sending image')
            #     image = self.images[request.Id].getvalue()
                
            #     print(image)

            #     result = service.ImageUploadResponse(Id=request.Id, StatusCode=service.ImageUploadStatusCode.Ok, Message=response.text.encode('utf8'))
            #     return result


show = ShowVideoStream()

def serve():
    port = 22222
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ImageServiceServicer_to_server(ImageServiceServer(), grpc_server)
    logging.info(f'Starting server. Listening at {port}...')
    grpc_server.add_insecure_port(f'[::]:{port}')
    grpc_server.start()
    grpc_server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    thread = threading.Thread(target=serve)
    thread.start()

    show.start()
    