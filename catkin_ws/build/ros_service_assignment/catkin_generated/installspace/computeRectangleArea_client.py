#!/usr/bin/env python3

import sys
import rospy
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

def compute_area_client(width, height):
    rospy.wait_for_service('compute_area')
    try:
        compute_area = rospy.ServiceProxy('compute_area', RectangleAreaService)
        resp1 = compute_area(width, height)
        return resp1.area
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [width height]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s*%s"%(width, height)
    s = compute_area_client(width, height)
    print "%s * %s = %s"%(width, height, s)