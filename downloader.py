import os
import re
from collections import OrderedDict
from multiprocessing import Pool

import requests

COURSE_PATTERN = '<td><a href="(.+?)\/">.+?\/<\/a><\/td>'
OPEN_CLASSROOM_BASE = 'http://openclassroom.stanford.edu/MainFolder/courses'
COURSE_MANIFEST_URL = OPEN_CLASSROOM_BASE + '/%s/course.xml'
VIDEO_BASE_TEMPLATE = OPEN_CLASSROOM_BASE + '/%s/videos/%s.mp4'

VIDEO_FILENAME_PATTERN = '<file>(.+?)<\/file>'


def get_course_list():
    """Return the full list of possible courses to download"""
    return re.findall(COURSE_PATTERN, requests.get(OPEN_CLASSROOM_BASE).content.decode())


def get_course_videos(course_name):
    """Return the full list of videos per course name"""
    return re.findall(VIDEO_FILENAME_PATTERN, requests.get(COURSE_MANIFEST_URL % course_name).content.decode())


def download_video(output_folder, course_name, video_name):
    """Build the video URL, fetch it and save it to the output folder"""
    print("Downloading: %s: %s" % (course_name, video_name))
    video_url = VIDEO_BASE_TEMPLATE % (course_name, video_name)
    filename = os.path.join(output_folder, video_name + '.mp4')
    with open(filename, 'wb') as f:
        f.write(requests.get(video_url).content)
    print("Finished Downloading: %s: %s" % (course_name, video_name))


if __name__ == '__main__':
    course_ids = sorted(get_course_list())
    # build a dictionary from course number to course name
    courses = OrderedDict(enumerate(course_ids))

    # print available courses
    print("Available courses for download are:")
    for course_id, course_name in courses.items():
        print("%s. %s" % (course_id, course_name))

    selection = input("Please select course ID:")
    assert selection.isdigit() and int(selection) in courses, \
        "Selection must be an integer and within the available course ids"

    selected_course = courses[int(selection)]
    # Create the output folder
    if not os.path.exists(selected_course):
        os.makedirs(selected_course)

    pool = Pool(processes=10)

    # Download all the videos with multiprocess
    course_videos = get_course_videos(selected_course)
    print("Downloading %s videos" % len(course_videos))
    args = ((selected_course, selected_course, video_name) for video_name in course_videos)
    pool.starmap(download_video, args)
    pool.close()

    print("Finished Downloading all videos")


