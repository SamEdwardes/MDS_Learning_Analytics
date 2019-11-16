from canvasapi import Canvas
import dotenv
import os
import pandas as pd


def get_canvas_posts(write_csv=False):
    """
    Queries canvas API to return discussion topics for selected course.
    For the script to work you must create a .evn file that contains:
        CANVAS_API_TOKEN=...
    In .. paste your token there

    Keyword Arguments:
        write_csv {bool} -- if True writes data to disk (default: {False})

    Returns:
        pd.DataFrame -- [description]

    Reference:
        https://canvasapi.readthedocs.io/en/latest/course-ref.html#canvasapi.course.Course.get_discussion_topics
    """
    ##############################################
    # API SET UP
    ##############################################
    dotenv.load_dotenv(dotenv.find_dotenv())
    API_URL = "https://ubc.instructure.com"
    API_KEY = os.environ.get('CANVAS_API_TOKEN')
    # Initialize a new Canvas object
    canvas = Canvas(API_URL, API_KEY)

    ##############################################
    # GET DATA
    ##############################################
    course = canvas.get_course(46341)
    print(f"{'#'*25}\nGETTING POSTS FROM:\n{'#'*25}\n{course}")
    topics = course.get_discussion_topics()

    ##############################################
    # PARSE AND CLEAN DATA
    ##############################################
    post_id = list()
    discussion_topic_title = list()
    discussion_topic_message = list()
    url = list()

    for i in topics:
        post_id.append(i.id)
        discussion_topic_title.append(i.title)
        discussion_topic_message.append(i.message)
        url.append(i.url)

    df = pd.DataFrame({"post_id": post_id,
                       "discussion_topic_title": discussion_topic_title,
                       "discussion_topic_message": discussion_topic_message,
                       "url": url})

    ##############################################
    # WRITE DATA
    ##############################################
    if write_csv:
        path_out = "data/canvas-discussion-posts.csv"
        print(f"{'#'*25}\nWriting posts to:\n{path_out}")
        df.to_csv(path_out, index=False)

    return df

if __name__ == "__main__":
    df = get_canvas_posts(write_csv=False)
    print("#"*25)
    print("DATA FRAME INFO:")
    print("#"*25)
    print(df.info())
