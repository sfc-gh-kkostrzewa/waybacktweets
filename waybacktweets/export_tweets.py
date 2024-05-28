import pandas as pd
import re
import datetime


def datetime_now():
    now = datetime.datetime.now()

    formatted_now = now.strftime("%Y%m%d%H%M%S")

    formatted_now = re.sub(r'\W+', '', formatted_now)

    return formatted_now


def transpose_matrix(data, fill_value=None):
    max_length = max(len(sublist) for sublist in data)
    filled_data = [
        sublist + [fill_value] * (max_length - len(sublist))
        for sublist in data
    ]

    data_transposed = [list(row) for row in zip(*filled_data)]

    return data_transposed


def response_tweets_csv(data, username):
    data_transposed = transpose_matrix(data)

    formatted_datetime = datetime_now()
    filename = f'{username}_tweets_{formatted_datetime}'

    df = pd.DataFrame(data_transposed,
                      columns=[
                          'archived_urlkey', 'archived_timestamp', 'tweet',
                          'archived_tweet', 'parsed_tweet',
                          'parsed_tweet_mimetype_json',
                          'parsed_archived_tweet', 'archived_mimetype',
                          'archived_statuscode', 'archived_digest',
                          'archived_length', 'available_tweet_content',
                          'available_tweet_is_RT', 'available_tweet_username'
                      ])

    csv_file_path = f'{filename}.csv'
    df.to_csv(csv_file_path, index=False)

    json_file_path = f'{filename}.json'
    df.to_json(json_file_path, orient='records', lines=False)

    print(f'Done. Check the files {filename}.csv and {filename}.json')
