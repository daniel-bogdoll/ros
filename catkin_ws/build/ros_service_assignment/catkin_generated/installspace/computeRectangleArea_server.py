#!/usr/bin/env python3

from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

import rospy

def handle_compute_area(req):
    print("Returning [%s * %s = %s]"%(req.width, req.height, (req.width * req.height)))
    return RectangleAreaServiceResponse(req.width * req.height)

def compute_area_server():
    rospy.init_node('compute_area_server')
    s = rospy.Service('compute_area', RectangleAreaService, handle_compute_area)
    print("Ready to compute rectangle area.")
    rospy.spin()
    
if __name__ == "__main__":
    compute_area_server()