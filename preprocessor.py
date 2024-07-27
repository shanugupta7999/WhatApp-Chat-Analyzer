import re
import pandas as pd
import numpy as np

def preprocess(data):
    # Regular expression pattern for matching date and time in WhatsApp chat format
    pattern = '\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\s?[apAP][mM] -'
    # Extract messages and dates
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # Adjust the format string to handle non-breaking space (\u202f)
    format_str = "%d/%m/%y, %I:%M\u202f%p -"
    # Convert 'message_date' to datetime format with adjusted format string
    df['message_date'] = pd.to_datetime(df['message_date'], format=format_str)
    # Rename the column 'message_date' to 'date'
    df.rename(columns={'message_date': 'date'}, inplace=True)
    # Extract users and messages
    users = []
    messages = []
    for message in df['user_message']:
        # Split the message at the first occurrence of colon and space
        entry = re.split(r':\s', message, maxsplit=1)
        if len(entry) >= 2:
            user = entry[0]
            message_text = entry[1]
            users.append(user)
            messages.append(message_text)
        else:
            users.append('group_notification')
            messages.append(message)
    # Add 'user' and 'message' columns to the DataFrame
    df['user'] = users
    df['message'] = messages
    # Drop the original 'user_message' column
    df.drop(columns=['user_message'], inplace=True)
    # Add date components
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour ==0:
            period.append(str(00) + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df