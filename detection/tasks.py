from SystemOfRoadPotholeDetectionDRF.celery import app
from detection.detection_files.run_detection import PotholeDetection
from .models import DetectionTable


@app.task
def run_detection(ident):

    table = DetectionTable.objects.filter(id=ident).first()
    print('hi')
    d = PotholeDetection(
        'detection/model/yolov4-pothole.weights',
        'detection/model/yolov4-pothole.cfg',
        'detection/model/obj.names',
        416,
        table,
    )

    d.run()



